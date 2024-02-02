<!-- MapComponent.svelte -->
<div id="map">
  <!-- Tooltip element -->
  <div class="tooltip" style="display: none;"></div>
</div>

<script context="module">

import { writable, derived } from 'svelte/store';

export let minPopulation = writable(69);
export let maxPopulation = writable(4214);
export let selectedYearsValue = writable(null);
export let selectedState = writable(null);
 
</script>


<script >
  import { onMount } from 'svelte';
  import * as d3 from 'd3'; 
  import trafficData from '$lib/data/final_genesis_traffic.json';
  import { createEventDispatcher } from 'svelte';
  import { selectedYear } from '$lib/components/timeline.svelte'; // Import the selectedYear store
  import populationDensityData from '$lib/data/population_density.json';
  
  let width, height, geoPath, projection, normalizedOpacity, normalizedOpacity2;
  let svg, g, zoom; // Define zoom and SVG selections
  let centroidMatrix = [];
  let focused = null; // Store the currently focused element
  let isMapInitialized = false; // Flag to track if the map is initialized
  let PDOpacityMap = {};
  let year = 2017; // initial year for the map color coding

  const dispatch = createEventDispatcher();
  export const stateData = {...trafficData, data: trafficData.data.filter(v => v.Bundesland === 'Bayern')};

  $: if ($selectedYear && isMapInitialized) {
    year = $selectedYear;
    getPDByYear(year);
    updateMapOpacities();

    // Update value of that year for the scale
    selectedYearsValue.set(getDensity(pdMatrix, $selectedState, $selectedYear));

  }

  let opacityMatrix = calculateOpacityMatrix(populationDensityData);

  onMount(() => {

    updateMapOpacities();

    // reset for second switch from about page
    minPopulation.set(69);
    maxPopulation.set(4214);

    var parentDiv = document.getElementById('map-parent');
    width = parentDiv.clientWidth;
    height = parentDiv.clientHeight;
    
    svg = d3.select('#map').append('svg')
      .attr('width', width)
      .attr('height', height);

    g = svg.append('g');

    // Define the zoom behavior
    zoom = d3.zoom()
      .scaleExtent([1, 1])
      .translateExtent([[0, 0], [width, height]]) // disables dragging the map
      .on('zoom', (event) => {
        g.attr('transform', event.transform);
      })
      .filter(event => {
        // Only allow zoom interactions with mouse clicks (left/middle/right), not with scroll
        return event.button === 0 || event.button === 1 || event.button === 2;
      });

    // Apply the zoom behavior to the svg
    svg.call(zoom);

    import('$lib/data/dataBundesLander_right_hand_rule.json').then((collection) => {
      projection = getProjection(collection);
      geoPath = d3.geoPath().projection(projection);

      collection.features.forEach((feature, index) => {
        const centroid = geoPath.centroid(feature);
        centroidMatrix[index] = centroid; // Store the centroid as [x, y]
      });

    // Select the tooltip element
    const tooltip = document.querySelector('.tooltip');

    g.selectAll('path')
      .data(collection.features)
      .join('path')
      .attr('class', 'state')
      .attr('d', geoPath)
      .style('opacity', d => getStateOpacity(d.properties.NAME_1))
      .on('mouseover', (event, d) => { 
        if ($selectedYearsValue == null) {
          // Show tooltip on mouseover only when selectedYearsValue is not null
          const tooltip = document.querySelector('.tooltip');
          tooltip.style.display = 'block';
          tooltip.textContent = (d.properties.NAME_1 + ": " + getDensity(pdMatrix, d.properties.NAME_1, $selectedYear)); // Set tooltip content
          const rect = tt.node().getBoundingClientRect();
          ttw = rect.width;
          tth = rect.height;
          moveTooltip(event);
        }
      })
      .on('mousemove', function (event) {
        if ($selectedYearsValue == null) {
          tooltip.style.left = ('left', event.pageX + 10 + 'px'); 
          tooltip.style.top = ('top', event.pageY - 60 + 'px');
        }
        
      })
      .on('mouseout', () => {
        // Hide tooltip on mouseout
        tooltip.style.display = 'none';
      })
      .on('click', (event, d) => {
        const i = collection.features.indexOf(d);
        clickState(d, i);
      });
    });
    // After setting up the map, set the flag to true
    isMapInitialized = true;

    // Initial call to set opacities based on the default year
    getPDByYear(year);

  });

  function moveTooltip(event) {
		tooltip.style('left', `${event.pageX - ttw / 2}px`).style('top', `${event.pageY - tth - 10}px`);
	  }


  function getProjection(collection) {
    const bounds = d3.geoBounds(collection),
          bottomLeft = bounds[0],
          topRight = bounds[1],
          rotLong = -(topRight[0] + bottomLeft[0]) / 2,
          center = [(topRight[0] + bottomLeft[0]) / 2 + rotLong, (topRight[1] + bottomLeft[1]) / 2];

    const projection = d3.geoAlbers()
      .parallels([bottomLeft[1], topRight[1]])
      .rotate([rotLong, 0, 0])
      .translate([width / 2, height / 2])
      .center(center);

    const bottomLeftPx = projection(bottomLeft),
          topRightPx = projection(topRight),
          scaleFactor = 1.00 * Math.min(width / (topRightPx[0] - bottomLeftPx[0]), height / (-topRightPx[1] + bottomLeftPx[1]));

    return projection.scale(scaleFactor * 1000);
  }

  let isZoomedIn = false; // Track zoom state

  function clickState(d, i) {
    if (isZoomedIn) {

      // If already zoomed in, reset the zoom
      resetZoom();
      updateMapOpacities();

      // Update value of that year for the scale
      selectedYearsValue.set(null);

      minPopulation.set(69);
      maxPopulation.set(4214);
      selectedState.set(null);
      dispatch('stateClicked', { stateName: null });

      // Remove any existing state labels
      g.selectAll('.state-label').remove();
    } else {
      // Logic for zooming in
      focused = d;
      isZoomedIn = true;
      dispatch('stateClicked', { stateName: d.properties.NAME_1 });
      selectedState.set(d.properties.NAME_1);

      // Update map opacities
      updateMapOpacities();

      // Update value of that year for the scale
      selectedYearsValue.set(getDensity(pdMatrix, $selectedState, $selectedYear));

      // Update the domain of minPopulation and maxPopulation for the focused state
      const { stateRow } = createPDDataForState(populationDensityData, d.properties.NAME_1);
      minPopulation.set(Math.min(...stateRow.filter(val => val !== null)));
      maxPopulation.set(Math.max(...stateRow.filter(val => val !== null)));

      const centroid = centroidMatrix[i];
      const k = getZoomFactor(d.properties.NAME_1);
      const transform = d3.zoomIdentity.translate(width / 2, height / 2).scale(k).translate(-centroid[0], -centroid[1]);

      svg.transition()
        .duration(1000)
        .call(zoom.transform, transform);
            
          svg.on('.zoom', null);

      selectedYearsValue.set(getDensity(pdMatrix, $selectedState, $selectedYear));
    }    
  }


  function resetZoom() {
    // Reset opacity of all states
    g.selectAll('.state')
      // .transition().duration(500)
      .style('opacity', d => getStateOpacity(d.properties.NAME_1));

    focused = null;
    isZoomedIn = false;

    // Reset the zoom transform
    svg.transition()
      .duration(1000)
      .call(zoom.transform, d3.zoomIdentity);  

    // Remove any state labels
    g.selectAll('.state-label').remove();
      
    updateMapOpacities();

    
  }

  function getZoomFactor(stateName) {
    const zoomFactors = {
      'Baden-Württemberg': 2.3,
      'Bayern': 1.75,
      'Berlin': 10,
      'Brandenburg': 2.5,
      'Bremen': 15,
      'Hamburg': 10,
      'Hessen': 2.7,
      'Mecklenburg-Vorpommern': 2.8,
      'Niedersachsen': 2,
      'Nordrhein-Westfalen': 2.5,
      'Rheinland-Pfalz': 3,
      'Saarland': 7,
      'Sachsen': 2.7,
      'Sachsen-Anhalt': 3,
      'Schleswig-Holstein': 3,
      'Thüringen': 3.1
    };

    return zoomFactors[stateName] || 1; // Default zoom factor if state not listed
  }


  function getPDByYear(year) {
    const startYear = 2017;
    const endYear = 2022;

    selectedYearsValue.set(100);

    // Filter data for the specified year and within the range of 2017 to 2022
    let filteredData = populationDensityData.data.filter(entry => 
      entry.Jahr === year && entry.Jahr >= startYear && entry.Jahr <= endYear
    );

    // Sort the filtered data alphabetically by Bundesland
    const sortedData = filteredData.sort((a, b) => a.Bundesland.localeCompare(b.Bundesland));

    // Extract only the 'EW_per_sqkm' values from the sorted data
    const populationDensities = sortedData.map(entry => entry.EW_per_sqkm);


    populationDensities.forEach((populationDensity, index) => {
      normalizedOpacity = mappopulationDensityToMap(populationDensity);
      // Now, you have the populationDensity value and the corresponding opacity value
      PDOpacityMap[sortedData[index].Bundesland] = normalizedOpacity;
    });

    return populationDensities;
  }

  function createPDDataForState(populationDensityData, stateName) {
    const startYear = 2017;
    const endYear = 2022;
    
    // Filter years to include only those between 2017 and 2022
    const years = [...new Set(populationDensityData.data.map(entry => entry.Jahr))]
                    .filter(year => year >= startYear && year <= endYear)
                    .sort();

    // Create a row for the specified state with filtered years
    let stateRow = years.map(year => {
        let entry = populationDensityData.data.find(e => e.Bundesland === stateName && e.Jahr === year);
        return entry ? entry.EW_per_sqkm : null; // Use null for missing data
    });

    return { stateName, years, stateRow };
  }

  function getStateOpacity(stateName) {
    return PDOpacityMap[stateName] || 1; // Default opacity if state not in list or data not loaded yet
  }

  

  function updateMapOpacities() {
    if (g) {

      if (isZoomedIn && focused) {

        const { stateRow } = createPDDataForState(populationDensityData, focused.properties.NAME_1);


        // Find min and max values for the focused state
        const min = Math.min(...stateRow.filter(val => val !== null));
        const max = Math.max(...stateRow.filter(val => val !== null));

        g.selectAll('.state')
        .style('opacity', d => {
          if (d === focused) {
            // Find the population density for the focused state in the selected year
            const populationDensity = populationDensityData.data.find(entry => entry.Jahr === year && entry.Bundesland === d.properties.NAME_1)?.EW_per_sqkm || min; // Use min as a fallback
            const opacity = mappopulationDensityToState(populationDensity, min, max);

            return opacity;
          }
          return 0; // Other states remain transparent
        });

      } else {

        g.selectAll('.state')
          .each(function(d) {
            const opacity = opacityMatrix[d.properties.NAME_1][year];

          })
          .style('opacity', d => opacityMatrix[d.properties.NAME_1][year]);
      }
    } else {

    }
  }

  function mappopulationDensityToMap(populationDensity) {
    let minOpacity = 0.1;
    let maxOpacity = 1;
    return minOpacity + ((populationDensity - $minPopulation) * (maxOpacity - minOpacity)) / ($maxPopulation - $minPopulation);
  }

  function mappopulationDensityToState(populationDensity, min, max) {
    if (min === max) return 1; // Avoid division by zero if min and max are equal
    const minOpacity = 0.1;
    const maxOpacity = 1; 
    return minOpacity + ((populationDensity - min) * (maxOpacity - minOpacity)) / (max - min);
  }

  function calculateOpacityMatrix(populationDensityData) {
    const startYear = 2017;
    const endYear = 2022; // Adjust this if you have data for more years
    const states = Array.from(new Set(populationDensityData.data.map(entry => entry.Bundesland))).sort();
    const opacityMatrix = {};

    states.forEach(state => {
      opacityMatrix[state] = {};
      for (let year = startYear; year <= endYear; year++) {
        const entry = populationDensityData.data.find(e => e.Bundesland === state && e.Jahr === year);

        const populationDensity = entry ? entry.EW_per_sqkm : null; // Use null for missing data
        if (populationDensity !== null) {
          const opacity = mappopulationDensityToOpacity(populationDensity);
          opacityMatrix[state][year] = opacity;
        } else {
          opacityMatrix[state][year] = null; // No data for this state-year
        }
      }
    });

    return opacityMatrix;
  }

  function createPDMatrix(populationDensityData) {
    const startYear = 2017;
    const endYear = 2022;
    const states = [...new Set(populationDensityData.data.map(entry => entry.Bundesland))];
    const years = [...new Set(populationDensityData.data.map(entry => entry.Jahr))]
                    .filter(year => year >= startYear && year <= endYear)
                    .sort();

    let matrix = states.map(stateName => {
        let stateRow = years.map(year => {
            let entry = populationDensityData.data.find(e => e.Bundesland === stateName && e.Jahr === year);
            return entry ? entry.EW_per_sqkm : null; // Use null for missing data
        });
        return stateRow;
    });

    return { states, years, matrix };
}


  const pdMatrix = createPDMatrix(populationDensityData);

  function getDensity(matrixData, stateName, year) {
      const stateIndex = matrixData.states.indexOf(stateName);
      const yearIndex = matrixData.years.indexOf(year);
      if (stateIndex === -1 || yearIndex === -1) {
          return null; // State or year not found
      }
      return matrixData.matrix[stateIndex][yearIndex];
  }

  // Example query:
  const density = getDensity(pdMatrix, "Bayern", 2017);



  function mappopulationDensityToOpacity(populationDensity) {
    const minPopulation = 69;
    const maxPopulation = 4214;
    const minOpacity = 0.1;
    const maxOpacity = 1;
    let opacity = ((populationDensity - minPopulation) / (maxPopulation - minPopulation)) * (maxOpacity - minOpacity) + minOpacity;
    return Math.max(minOpacity, Math.min(maxOpacity, opacity)); // Clamping the value between minOpacity and maxOpacity
  }


</script>

<style>
  :global(.state) {
    fill: #003049 !important;
    stroke: #fff;
    stroke-width: 1.25px;
    transition: 0.5s;
    cursor: pointer;
  }
  
  /* Tooltip styles */
  
  .tooltip {
    position: absolute;
    background-color: #fff;
    color: #000;
    border: 1px solid #000;
    padding: 10px;
    border-radius: 8px;
    pointer-events: none; /* Allow interaction with underlying map elements */
    z-index: 9999; /* Ensure tooltip appears above the map */
  }

</style>

<!-- MapComponent.svelte -->
<div id="map"></div>

<script context="module">

import { writable, derived } from 'svelte/store';

export let minPercentage = writable(2.8);
export let maxPercentage = writable(11.2);

</script>


<script >
  import { onMount } from 'svelte';
  import * as d3 from 'd3'; 
  import trafficData from '$lib/data/final_genesis_traffic.json';
  import unemploymentData from '$lib/data/unemployment_rate.json';
  import { createEventDispatcher } from 'svelte';
  import { selectedYear } from '$lib/components/timeline.svelte'; // Import the selectedYear store
  
  let width, height, geoPath, projection, normalizedOpacity;
  let svg, g, zoom; // Define zoom and SVG selections
  let centroidMatrix = [];
  let focused = null; // Store the currently focused element
  let isMapInitialized = false; // Flag to track if the map is initialized
  let unemploymentOpacityMap = {};
  let year = 2017; // initial year for the map color coding

  const dispatch = createEventDispatcher();
  export const stateData = {...trafficData, data: trafficData.data.filter(v => v.Bundesland === 'Bayern')};

  $: if ($selectedYear && isMapInitialized) {
    year = $selectedYear;
    getUnemploymentPercentagesByYear(year);
    updateMapOpacities();
  }

  let opacityMatrix = calculateOpacityMatrix(unemploymentData);

  onMount(() => {

    

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

      g.selectAll('path')
        .data(collection.features)
        .join('path')
        .attr('class', 'state')
        .attr('d', geoPath)
        .style('opacity', d => getStateOpacity(d.properties.NAME_1))
        .on('click', (event, d) => {
          const i = collection.features.indexOf(d);
          clickState(d, i);
        });
    });
    // After setting up the map, set the flag to true
    isMapInitialized = true;

    // Initial call to set opacities based on the default year
    getUnemploymentPercentagesByYear(year);

  });

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
        minPercentage.set(2.8);
        maxPercentage.set(11.2);
        dispatch('stateClicked', { stateName: null });
    } else {
        // Logic for zooming in
        focused = d;
        isZoomedIn = true;
        dispatch('stateClicked', { stateName: d.properties.NAME_1 });

        const { stateRow } = createUnemploymentMatrixForState(unemploymentData, d.properties.NAME_1);
        minPercentage.set(Math.min(...stateRow.filter(val => val !== null)));
        maxPercentage.set(Math.max(...stateRow.filter(val => val !== null)));


        // Set opacity for the focused state based on the matrix
        const focusedOpacity = opacityMatrix[d.properties.NAME_1][year];
        g.selectAll('.state')
          .transition().duration(500)
          .style('opacity', (_, j) => i === j ? focusedOpacity : 0);

        const centroid = centroidMatrix[i];
        if (!centroid) {
            console.error('No centroid found for feature at index:', i);
            return;
        }

        const [x, y] = centroid;
        const k = getZoomFactor(d.properties.NAME_1);

        // Compute the translation and scale to center the centroid
        const transform = d3.zoomIdentity
            .translate(width / 2, height / 2)
            .scale(k)
            .translate(-x, -y);

        svg.transition()
            .duration(1000)
            .call(zoom.transform, transform);

        // Disable zoom and drag behavior when zoomed in
        svg.on('.zoom', null); // Remove existing zoom handlers
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

  function getUnemploymentPercentagesByYear(year) {
  const startYear = 2017;
  const endYear = 2022;

  // Filter data for the specified year and within the range of 2017 to 2022
  let filteredData = unemploymentData.data.filter(entry => 
    entry.Jahr === year && entry.Jahr >= startYear && entry.Jahr <= endYear
  );

  // Sort the filtered data alphabetically by Bundesland
  const sortedData = filteredData.sort((a, b) => a.Bundesland.localeCompare(b.Bundesland));

  // Extract only the 'Prozent' values from the sorted data
  const unemploymentPercentages = sortedData.map(entry => entry.Prozent);

  unemploymentPercentages.forEach((percentage, index) => {
    normalizedOpacity = mapPercentageToMap(percentage);
    // Now, you have the percentage value and the corresponding opacity value
    unemploymentOpacityMap[sortedData[index].Bundesland] = normalizedOpacity;
  });

  return unemploymentPercentages;
}



  function createUnemploymentMatrixForState(unemploymentData, stateName) {
    const startYear = 2017;
    const endYear = 2022;
    
    // Filter years to include only those between 2017 and 2022
    const years = [...new Set(unemploymentData.data.map(entry => entry.Jahr))]
                    .filter(year => year >= startYear && year <= endYear)
                    .sort();

    // Create a row for the specified state with filtered years
    let stateRow = years.map(year => {
        let entry = unemploymentData.data.find(e => e.Bundesland === stateName && e.Jahr === year);
        return entry ? entry.Prozent : null; // Use null for missing data
    });


    return { stateName, years, stateRow };
  }


  function getStateOpacity(stateName) {
    return unemploymentOpacityMap[stateName] || 1; // Default opacity if state not in list or data not loaded yet
  }

  function updateMapOpacities() {
    if (g) {
      if (isZoomedIn && focused) {
        const { stateRow } = createUnemploymentMatrixForState(unemploymentData, focused.properties.NAME_1);

        // Find min and max values for the focused state
        const min = Math.min(...stateRow.filter(val => val !== null));
        const max = Math.max(...stateRow.filter(val => val !== null));

        g.selectAll('.state')
        .style('opacity', d => {
          if (d === focused) {
            // Find the unemployment percentage for the focused state in the selected year
            const percentage = unemploymentData.data.find(entry => entry.Jahr === year && entry.Bundesland === d.properties.NAME_1)?.Prozent || min; // Use min as a fallback
            const opacity = mapPercentageToState(percentage, min, max);

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



  function mapPercentageToMap(percentage) {
    let minOpacity = 0.1;
    let maxOpacity = 1;
    return minOpacity + ((percentage - $minPercentage) * (maxOpacity - minOpacity)) / ($maxPercentage - $minPercentage);
  }

  function mapPercentageToState(percentage, min, max) {
    if (min === max) return 1; // Avoid division by zero if min and max are equal
    const minOpacity = 0.1;
    const maxOpacity = 1;
    return minOpacity + ((percentage - min) * (maxOpacity - minOpacity)) / (max - min);
  }

  

  function calculateOpacityMatrix(unemploymentData) {
  const startYear = 2017;
  const endYear = 2022; // Adjust this if you have data for more years
  const states = Array.from(new Set(unemploymentData.data.map(entry => entry.Bundesland))).sort();
  const opacityMatrix = {};

  states.forEach(state => {
    opacityMatrix[state] = {};
    for (let year = startYear; year <= endYear; year++) {
      const entry = unemploymentData.data.find(e => e.Bundesland === state && e.Jahr === year);
      const percentage = entry ? entry.Prozent : null; // Use null for missing data
      if (percentage !== null) {
        const opacity = mapPercentageToOpacity(percentage);
        opacityMatrix[state][year] = opacity;
      } else {
        opacityMatrix[state][year] = null; // No data for this state-year
      }
    }
  });

  

  

  return opacityMatrix;
}
function mapPercentageToOpacity(percentage) {
  const minPercentageValue = 2.8; // These values should come from your actual data or be calculated dynamically
  const maxPercentageValue = 11.2;
  const minOpacity = 0.1;
  const maxOpacity = 1;
  let opacity = ((percentage - minPercentageValue) / (maxPercentageValue - minPercentageValue)) * (maxOpacity - minOpacity) + minOpacity;
  return Math.max(minOpacity, Math.min(maxOpacity, opacity)); // Clamping the value between minOpacity and maxOpacity
}
console.log(opacityMatrix);




</script>

<style>
  :global(.state) {
    fill: #003049 !important;
    stroke: #fff;
    stroke-width: 1.25px;
    transition: 0.5s;
  }
  /* :global(.state.active) {
    fill: #003049 !important;
  } */


</style>

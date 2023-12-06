<!-- MapComponent.svelte -->
<div id="map"></div>

<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3'; 
  import trafficData from '$lib/data/final_genesis_traffic.json';
  import unemploymentData from '$lib/data/unemployment_rate.json';
  import { createEventDispatcher } from 'svelte';

  let width, height, geoPath, projection;
  let svg, g, zoom; // Define zoom and SVG selections
  let centroidMatrix = [];
  let focused = null; // Store the currently focused element

  const dispatch = createEventDispatcher();

  export const stateData = {...trafficData, data: trafficData.data.filter(v => v.Bundesland === 'Bayern')};

  let unemploymentOpacityMap = {};

  onMount(() => {
    // Load and process unemployment data for 2018
    getUnemploymentPercentagesByYear(2019);

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

    d3.json('src/lib/data/dataBundesLander_right_hand_rule.json').then((collection) => {
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

  function clickState(d, i) {
    const stateName = d.properties.NAME_1; 
    dispatch('stateClicked', { stateName });

    const centroid = centroidMatrix[i];
    if (!centroid) {
      console.error('No centroid found for feature at index:', i);
      return;
    }

    g.selectAll('.state').classed('active', false);
    d3.select(event.currentTarget).classed('active', true);
    
    if (focused !== d) {
      focused = d;
      
      const [x, y] = centroid;
      const k = 1.75; // Adjust the scaling factor as needed
      
      // Compute the translation and scale to center the centroid
      const transform = d3.zoomIdentity
        .translate(width / 2, height / 2)
        .scale(k)
        .translate(-x, -y);

      svg.transition()
        .duration(1000)
        .call(zoom.transform, transform);

      dispatch('stateClicked', { stateName: d.properties.NAME_1 }); // Dispatch the state name
    } else {
      focused = null;
      resetZoom();
      dispatch('stateClicked', { stateName: null }); // Dispatch null when no state is focused
    }
  }

  function resetZoom() {
    g.selectAll('.state').classed('active', false);
    focused = null;
    svg.transition()
      .duration(1000)
      .call(zoom.transform, d3.zoomIdentity);
    dispatch('stateClicked', { stateName: null }); // Dispatch null when zoom is reset
  }

  function getUnemploymentPercentagesByYear(year) {
    const filteredData = unemploymentData.data.filter(entry => entry.Jahr === year);
    
    // Sort the filtered data alphabetically by Bundesland
    const sortedData = filteredData.sort((a, b) => a.Bundesland.localeCompare(b.Bundesland));

    const unemploymentPercentages = sortedData.map(entry => ({
        Bundesland: entry.Bundesland,
        Prozent: entry.Prozent
    }));

    // Normalize and map percentages to opacity
    const maxPercentage = Math.max(...unemploymentPercentages.map(entry => entry.Prozent));
    unemploymentPercentages.forEach(entry => {
      // Normalize the percentage to a value between 0.3 and 1 for better visibility
      unemploymentOpacityMap[entry.Bundesland] = 0.3 + (entry.Prozent / maxPercentage) * 0.7;
    });

    // console.log('Sorted Unemployment Percentages:', unemploymentPercentages);
    return unemploymentPercentages;
  }

  function getStateOpacity(stateName) {
    return unemploymentOpacityMap[stateName] || 1; // Default opacity if state not in list or data not loaded yet
  }
</script>

<style>
  :global(.state) {
    fill: #FCBF49;
    stroke: #fff;
    stroke-width: 1.25px;
    transition: 0.5s;
  }
  :global(.state:hover) {
    fill: #F77F00;
    opacity: 100 !important;
  }
  :global(.state.active) {
    fill: #F77F00 !important;
    opacity: 100 !important;
  }
</style>

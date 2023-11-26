<!-- MapComponent.svelte -->
<div id="map"></div>

<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3'; 

  let width, height, geoPath, projection;
  let svg, g, zoom; // Define zoom and SVG selections
  let centroidMatrix = [];
  let focused = null; // Store the currently focused element

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
      .scaleExtent([1, 8])
      .on('zoom', (event) => {
        g.attr('transform', event.transform);
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

    // const stateName = d.properties.NAME_1; // This should be the property that identifies the state
    // const stateID = d.properties.ID_1;

    // console.log("Bundesstaaten: ", stateID, stateName);

    // switch (stateName) {
    //   case 'Baden-Württemberg':
    //     handleState1Click(d);
    //     break;
    //   case 'Bayern':
    //     handleState2Click(d);
    //     break;
    //   case 'Berlin':
    //     handleState3Click(d);
    //     break;
    //   default:
    //     // Optionally handle any other cases
    //     break;
    // }


    // zoom in functionality

    // // Remove active class from all states
    // g.selectAll('.state').classed('active', false);

    // // Add active class to the clicked state
    // d3.select(d).classed('active', true);

    const centroid = centroidMatrix[i];
    if (!centroid) {
      console.error('No centroid found for feature at index:', i);
      return;
    }
    
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
    } else {
      resetZoom();
    }
  }

  function resetZoom() {
    focused = null;
    // g.selectAll('.state').classed('active', false);
    svg.transition()
      .duration(1000)
      .call(zoom.transform, d3.zoomIdentity);
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
  }
  :global(.state.active) {
    fill: #F77F00;
  }
</style>

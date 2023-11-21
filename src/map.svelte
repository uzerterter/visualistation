<!-- MapComponent.svelte -->
<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3'; 

  let width, height, geoPath, focused = null;
  let g; 

  // onMount is used to ensure the DOM is ready before trying to select and manipulate elements
  onMount(() => {
    width = window.innerWidth;
    height = window.innerHeight;
  
      
  const svg = d3.select("#map")
    .append("svg")
    .attr("width", "100vw")
    .attr("height", "100vh")
    .style("background", "#EAE2B7");

  g = svg.append("g").attr("id", "states");

  // draws the outlines of the federal states from coordinates
  d3.json("./dataBundesLander.json").then((collection) => {
    const projection = getProjection(collection);
    geoPath = d3.geoPath().projection(projection);

    g.selectAll("path")
      .data(collection.features)
      .enter()
      .append("path")
      .attr("class", "state")
      .attr("d", geoPath)
      .on("click", clickState);
    });
  });

  // implements the map in Albers projection
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
  
  // zooms in when a federal state is clicked
  function clickState(d) {
    const stateId = d.properties.ID_1;

    if (focused === d) {
      resetZoom();
    } else {
      const centroid = geoPath.centroid(d),
        x = centroid[0],
        y = centroid[1],
        k = 1.5;

      focused = d;

      g.transition()
        .duration(750)
        .attr("transform", `translate(${width / 2},${height / 2})scale(${k})translate(${-x},${-y})`)
        .style("stroke-width", 1.5 / k + "px");

      handleStateClick(stateId);
    }

    g.selectAll("path").classed("active", (d) => d === focused);
  }
  
  // resets the zoom after clicked on an active federal state
  function resetZoom() {
    focused = null;
    g.transition()
      .duration(750)
      .attr("transform", "")
      .style("stroke-width", "1.5px");

    g.selectAll("path").classed("active", false);
  }

  // calls specific functions when a state is clicked
  function handleStateClick(stateId) {
    const stateFunctionMap = {
      1: function1,
      2: function2,
      // Add additional state IDs and functions as needed
    };

    if (stateFunctionMap[stateId]) {
      stateFunctionMap[stateId]();
    } else {
      console.log("No specific function for state ID " + stateId);
    }
  }
  
  // Define your specific functions for each state here
  function function1() {
    console.log("Function for state 1 called");
    // Implement functionality for state 1
  }

  function function12() {
    console.log("Function for state 12 called");
    // Implement functionality for state 12
  }
  
</script>
  
<style>

  /* possible styles for default, hover and active federal states*/
  .state {
    fill: #FCBF49;
    stroke: #fff;
    stroke-width: 1.25px;
    opacity: 0.85;
  }

  .state:hover {
    fill: #F77F00;
  }

  .state.active {
    fill: #F77F00;
  }
</style>

<div id="map"></div>
  
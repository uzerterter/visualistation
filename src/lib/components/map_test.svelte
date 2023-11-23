<!-- MapComponent.svelte -->
<div id="map"></div>

<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3'; 

  export let data = []
  
  let width, height, geoPath, focused = null;
  let g; 

  // onMount is used to ensure the DOM is ready before trying to select and manipulate elements
  onMount(() => {
  
  var parentDiv = document.getElementById("map-parent");
      width = parentDiv.clientWidth;
      height = parentDiv.clientHeight - 100;
      
  const svg = d3.select("#map")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  g = svg.append("g").attr("id", "states");

  // draws the outlines of the federal states from coordinates
  d3.json("src/lib/data/dataBundesLander_right_hand_rule.json").then((collection) => {
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

  // draws the map in Albers projection
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

  function clickState(d) {
    console.log("Clicked feature:", d);
    
      if (focused === d) {
          // If the same state is clicked again, reset the zoom
          // resetZoom();
      } else {
          // Calculate the new scale and translate values
          var centroid = geoPath.centroid(d),
              x = +centroid[0],
              y = +centroid[1],
              k = 1.4;   // scaling factor
          focused = d;
          console.log("Centroid:", centroid); 
          console.log("Translate and scale values:", x, y, k); 

          // Apply the zoom transform to the map
          g.transition()
              .duration(1000)
              .attr("transform", "translate(" + (width / 2) + "," + (height / 2) + ")scale(" + k + ")translate(" + (-x) + "," + (-y) + ")")
              .style("stroke-width", 1.75 / k + "px");
      }
      

      // Handle other actions related to the state click here
      g.selectAll("path")
      .classed("active", focused && function (d) { return d === focused; });
  }
  
</script>
  
<style>
  :global(#states) {
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

<div id="map"></div>
  
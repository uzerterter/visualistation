import * as d3 from 'd3';

// Width and height of the SVG container
var width = 800;
var height = 600;

// Create an SVG element
var svg = d3.select("#map-svg")
    .attr("width", width)
    .attr("height", height);

// Define a projection for the map (you can choose different projections)
var projection = d3.geoMercator()
    .center([10, 51])
    .scale(750)
    .translate([width / 2, height / 2]);

// Create a path generator
var path = d3.geoPath().projection(projection);

// Load the GeoJSON file for Germany's state boundaries
d3.json("germany-states.geojson").then(function(germany) {
    // Bind data and create path elements for each state
    svg.selectAll("path")
        .data(germany.features)
        .enter()
        .append("path")
        .attr("d", path)
        .style("fill", "lightblue")
        .style("stroke", "gray");
});

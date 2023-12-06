<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
  
    // Dummy data
    let data = {
      'Baden-Württemberg': { male: 1000, female: 3000, both: 3250 },
      'Bavaria': { male: 3400, female: 2900, both: 3150 },
      'Berlin': { male: 3300, female: 2800, both: 3050 },
      'Brandenburg': { male: 3200, female: 2700, both: 2950 },
      'Bremen': { male: 3100, female: 2600, both: 2850 },
      'Hamburg': { male: 3000, female: 2500, both: 2750 },
      'Hesse': { male: 2900, female: 8000, both: 2650 },
      'Lower Saxony': { male: 2800, female: 2300, both: 2550 },
      'Mecklenburg-Vorpommern': { male: 2700, female: 2200, both: 2450 },
      'North Rhine-Westphalia': { male: 3600, female: 3100, both: 3350 },
      'Rhineland-Palatinate': { male: 3500, female: 3000, both: 3250 },
      'Saarland': { male: 3400, female: 2900, both: 9000 },
      'Saxony': { male: 3300, female: 2800, both: 3050 },
      'Saxony-Anhalt': { male: 3200, female: 2700, both: 2950 },
      'Schleswig-Holstein': { male: 3100, female: 2600, both: 2850 },
      'Thuringia': { male: 3000, female: 2500, both: 2750 }
    };
    let currentView = 'both'; // Default view set to 'both'
  
    onMount(() => {
      drawDoughnutChart(currentView);
    });
  
    // Function to draw the doughnut chart
    function drawDoughnutChart(view) {
      // Clear previous chart
      d3.select("#doughnut-chart").selectAll("*").remove();
  
      // Prepare data for D3
      const pieData = d3.pie().value(d => d[1][view])(Object.entries(data));
  
      // Define dimensions and radii
      const width = 250;  // Increased width for better label space
      const height = 250; // Increased height for better label space
      const radius = Math.min(width, height) / 2;
      const innerRadius = radius / 2;
  
      // Create an SVG container
      const svg = d3.select("#doughnut-chart")
                    .attr("width", width)
                    .attr("height", height)
                    .append("g")
                    .attr("transform", `translate(${width / 2}, ${height / 2})`);
  
      // Create a unique color scale
      const color = d3.scaleOrdinal(d3.schemeSet3);
  
      // Define the arc generator for doughnut chart
      const arc = d3.arc().innerRadius(innerRadius).outerRadius(radius);
  
      // Draw the doughnut chart
      svg.selectAll("path")
         .data(pieData)
         .enter()
         .append("path")
         .attr("d", arc)
         .attr("fill", (d, i) => color(i));
  
      // Define outer arc for label positioning
      const labelRadius = radius * 1.3;
      const outerArc = d3.arc().innerRadius(labelRadius).outerRadius(labelRadius);
  
      // Add labels
      svg.selectAll("text")
         .data(pieData)
         .enter()
         .append("text")
         .attr("transform", d => {
           const pos = outerArc.centroid(d);
           pos[0] = labelRadius * (midAngle(d) < Math.PI ? 1 : -1);
           return `translate(${pos})`;
         })
         .attr("dy", ".35em")
         .style("text-anchor", d => midAngle(d) < Math.PI ? "start" : "end")
         .text(d => d.data[0]) // Using state names as labels
         .style("font-size", "10px");
  
      // Add lines
      svg.selectAll("polyline")
         .data(pieData)
         .enter()
         .append("polyline")
         .attr("points", d => {
           const pos = outerArc.centroid(d);
           pos[0] = labelRadius * (midAngle(d) < Math.PI ? 1 : -1);
           return [arc.centroid(d), outerArc.centroid(d), pos]
         })
         .style("fill", "none")
         .style("stroke", "black")
         .style("stroke-width", 1);
  
      // Calculate mid angle
      function midAngle(d) {
        return d.startAngle + (d.endAngle - d.startAngle) / 2;
      }
    }
  
    // Function to update the chart
    function updateChart(view) {
      currentView = view;
      drawDoughnutChart(currentView);
    }
  </script>
  
  <svg id="doughnut-chart"></svg>
  
  <div style="text-align: center; margin-top: 10px;">
    <button on:click={() => updateChart('male')}>Male</button>
    <button on:click={() => updateChart('female')}>Female</button>
    <button on:click={() => updateChart('both')}>Both</button>
  </div>
  
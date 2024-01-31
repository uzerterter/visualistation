<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { minPopulation } from '$lib/components/map.svelte';
    import { maxPopulation } from '$lib/components/map.svelte';
    import { selectedYearsValue } from '$lib/components/map.svelte';
  
    let newMinPopulation, newMaxPopulation;
    let svg, colorScale, axisScale, gradient;
  
    let currentValue = null;
  
    const width = 300; // Width of the color legend
    const height = 50; // Height of the color legend
    const margin = { top: 10, right: 20, bottom: 30, left: 20 };
  
    // Define colorScale and axisScale outside of onMount
    colorScale = d3.scaleLinear().range(["#e5e5de", "#003049"]);
    axisScale = d3.scaleLinear();
  
    // Define the gradient once in onMount()
    onMount(() => {
  
        svg = d3.select("#color-legend")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);
  
        colorScale = d3.scaleLinear()
            .domain([newMinPopulation, newMaxPopulation])
            .range(["#e5e5de", "#003049"]);
  
        axisScale = d3.scaleLinear()
            .domain([newMinPopulation, newMaxPopulation])
            .range([0, width]);
  
        gradient = svg.append("defs")
            .append("linearGradient")
            .attr("id", "gradient");
  
        gradient.append("stop").attr("offset", "0%").attr("stop-color", colorScale(newMinPopulation));
        gradient.append("stop").attr("offset", "100%").attr("stop-color", colorScale(newMaxPopulation));
  
        svg.append("rect")
            .attr("width", width)
            .attr("height", 20)
            .style("fill", "url(#gradient)");
  
        const axisBottom = d3.axisBottom(axisScale);
  
        svg.append("g")
            .attr("class", "axis")
            .attr("transform", `translate(0,20)`)
            .call(axisBottom);
  
        svg.append("text")
            .attr("x", width / 2)
            .attr("y", 55)
            .style("text-anchor", "middle")
            .text("Inhabitants per square kilometer");
  
        updatepointer(currentValue);
    });
  
    minPopulation.subscribe(value => {
        newMinPopulation = value;
        if (typeof window !== 'undefined') {
            foo();
            colorScale.domain([newMinPopulation, newMaxPopulation]);
  
        }
    });
  
    maxPopulation.subscribe(value => {
        newMaxPopulation = value;
        if (typeof window !== 'undefined') {
            foo();
            colorScale.domain([newMinPopulation, newMaxPopulation]);
        }
    });
  
    selectedYearsValue.subscribe(value => {
        currentValue = value;
        if (typeof window !== 'undefined') {
            updateSelectedYear();
        }
    });
  
    function foo() {
    if (!svg || !colorScale || !axisScale) return;
  
    // Remove the old legend elements
    svg.select(".axis").remove();
  
    // Update the domain of the axis scale
    axisScale.domain([newMinPopulation, newMaxPopulation]);
  
    // Define the axis with custom tick values
    const axisBottom = d3.axisBottom(axisScale)
                         .tickFormat(d3.format(".0f"));
  
    if (currentValue != null) { // Aka if it is zoomed in on a federal state
  
      // Only show min and max values when currentValue is null
      axisBottom.tickValues([newMinPopulation, newMaxPopulation]);
    }
  
    // Redraw the axis with the new settings
    svg.append("g")
        .attr("class", "axis")
        .attr("transform", `translate(0,20)`)
        .call(axisBottom);
  
    updatepointer();
  }
  
  
  
    function updateSelectedYear() {
      if (!svg || currentValue === undefined) return;
  
      // Additional logic if needed when selectedYear changes
      updatepointer();
    }
  
    function updatepointer() {
    if (!svg || currentValue === undefined) return;
  
    // Remove the old pointer line and text
    svg.selectAll(".pointer, .pointer-text").remove();
  
    if (currentValue != null) {
      const pointerX = axisScale(currentValue);
      const pointerHeight = height - 48; // Adjust as needed to make the line shorter
      const offset = (height - pointerHeight) / 2; // Center the line vertically
  
      // Add the new pointer line
      svg.append("line")
          .attr("class", "pointer")
          .attr("x1", pointerX)
          .attr("x2", pointerX)
          .attr("y1", 0) // Start the line a bit lower
          .attr("y2", offset + pointerHeight) // End the line before the bottom edge
          .style("stroke", "red") // Change the pointer color as needed
          .style("stroke-width", 2);
  
      if (currentValue !== newMinPopulation && currentValue !== newMaxPopulation) {
          // Add text label for the current value
          svg.append("text")
              .attr("class", "pointer-text")
              .attr("x", pointerX)
              .attr("y", offset + pointerHeight + 9) // Position below the line
              .text(currentValue)
              .attr("text-anchor", "middle") // Center the text on the line
              .attr("font-size", "10px")
              .attr("fill", "black"); // Or any color you prefer
      }
    }
  }
  
  
  </script>
  
  <svg id="color-legend"></svg>
  
  <style>
    /* Styles for the color legend */
    #color-legend {
        /* Center the legend */
        display: block;
        margin: auto;
    }
  </style>
  
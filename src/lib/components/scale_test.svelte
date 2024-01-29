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
  colorScale = d3.scaleLinear().range(["#eeeff0", "#003049"]);
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
          .range(["#eeeff0", "#003049"]);

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

      updateIndicator(currentValue);
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

    // Define a format with no decimal points
    const tickFormat = d3.format(".0f");

    // Redraw the axis with the new format
    svg.append("g")
        .attr("class", "axis")
        .attr("transform", `translate(0,20)`)
        .call(d3.axisBottom(axisScale).tickFormat(tickFormat));

    updateIndicator();
  }

  function updateSelectedYear() {
    if (!svg || currentValue === undefined) return;

    // Additional logic if needed when selectedYear changes
    updateIndicator();
  }

  function updateIndicator() {

    if (currentValue == null) {
      // Remove the old indicator line
      svg.selectAll(".indicator").remove();
    } else {
      // Remove the old indicator line
      svg.selectAll(".indicator").remove();

      // Add the new indicator line with adjusted height
      const indicatorHeight = height - 48; // Adjust as needed to make the line shorter
      const offset = (height - indicatorHeight) / 2; // Center the line vertically


      // Add the new indicator line
      svg.append("line")
          .attr("class", "indicator")
          .attr("x1", axisScale(currentValue))
          .attr("x2", axisScale(currentValue))
          .attr("y1", 0) // Start the line a bit lower
          .attr("y2", offset + indicatorHeight) // End the line before the bottom edge
          .style("stroke", "red") // Change the pointer color as needed
          .style("stroke-width", 2);
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

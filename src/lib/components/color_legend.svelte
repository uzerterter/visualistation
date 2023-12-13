<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';

    onMount(() => {
        const width = 300; // Width of the color legend
        const height = 50; // Height of the color legend
        const margin = { top: 10, right: 20, bottom: 30, left: 20 };

        const svg = d3.select("#color-legend")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        const colorScale = d3.scaleLinear()
            .domain([2.8, 11.2])
            .range(["#eeeff0", "#003049"]);

        const gradient = svg.append("defs")
            .append("linearGradient")
            .attr("id", "gradient");

        gradient.append("stop").attr("offset", "0%").attr("stop-color", colorScale(2.8));
        gradient.append("stop").attr("offset", "100%").attr("stop-color", colorScale(11.2));

        svg.append("rect")
            .attr("width", width)
            .attr("height", 20)
            .style("fill", "url(#gradient)");

        const axisScale = d3.scaleLinear()
            .domain([2.8, 11.2])
            .range([0, width]);

        const axisBottom = d3.axisBottom(axisScale);

        svg.append("g")
            .attr("transform", `translate(0,20)`)
            .call(axisBottom);

        svg.append("text")
            .attr("x", width / 2)
            .attr("y", 55) 
            .style("text-anchor", "middle")
            .text("Unemployment rate in %");
    });
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

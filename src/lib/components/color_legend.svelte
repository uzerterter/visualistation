<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { minPercentage } from '$lib/components/map.svelte';
    import { maxPercentage } from '$lib/components/map.svelte';

    let newMinPercentage, newMaxPercentage;
    let svg, colorScale, axisScale, gradient;

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
            .domain([newMinPercentage, newMaxPercentage])
            .range(["#eeeff0", "#003049"]);

        axisScale = d3.scaleLinear()
            .domain([newMinPercentage, newMaxPercentage])
            .range([0, width]);

        gradient = svg.append("defs")
            .append("linearGradient")
            .attr("id", "gradient");

        gradient.append("stop").attr("offset", "0%").attr("stop-color", colorScale(newMinPercentage));
        gradient.append("stop").attr("offset", "100%").attr("stop-color", colorScale(newMaxPercentage));

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
            .text("Unemployment rate in %");
    });

    minPercentage.subscribe(value => {
        newMinPercentage = value;
        if (typeof window !== 'undefined') {
            foo();
            colorScale.domain([newMinPercentage, newMaxPercentage]);

        }
    });

    maxPercentage.subscribe(value => {
        newMaxPercentage = value;
        if (typeof window !== 'undefined') {
            foo();
            colorScale.domain([newMinPercentage, newMaxPercentage]);
        }
    });

    function foo() {
        if (!svg || !colorScale || !axisScale) return;

        // Remove the old legend elements
        svg.select(".axis").remove();

        // Update the domain of the axis scale
        axisScale.domain([newMinPercentage, newMaxPercentage]);

        // Redraw the axis
        svg.append("g")
            .attr("class", "axis")
            .attr("transform", `translate(0,20)`)
            .call(d3.axisBottom(axisScale));
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

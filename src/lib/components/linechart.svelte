<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';

    const data = {
        "years": [2017, 2018, 2019, 2020, 2021, 2022],
        "man": [6368, 7158, 8608, 7927, 5473, 9738],
        "woman": [6901, 9539, 7600, 9070, 6026, 5599],
        "both": [6634, 8348, 8104, 8498, 5749, 7668]
    };

    function createLineChart(data) {

        // var parentDiv = document.getElementById("linechart-parent");
        // var width = parentDiv.clientWidth;
        // var height = parentDiv.clientHeight;
        
        const margin = {top: 30, right: 30, bottom: 30, left: 30},
        width = 300 - margin.left - margin.right, // Adjusted width to 300px
        height = 300 - margin.top - margin.bottom; // Adjusted height to 300px

        const svg = d3.select('#linechart')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom)
            .append('g')
            .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

        const x = d3.scaleBand()
            .range([0, width])
            .domain(data.years)
            .padding(0.1);

        svg.append('g')
            .attr('transform', 'translate(0,' + height + ')')
            .call(d3.axisBottom(x));

        const y = d3.scaleLinear()
            .domain([0, 10000])
            .range([height, 0]);

        svg.append('g')
            .call(d3.axisLeft(y));

        const createLine = d3.line()
            .x((d, i) => x(data.years[i]))
            .y(d => y(d));

        ['man', 'woman', 'both'].forEach(key => {
            svg.append('path')
                .datum(data[key])
                .attr('fill', 'none')
                .attr('stroke', key === 'man' ? 'blue' : key === 'woman' ? 'pink' : 'green')
                .attr('stroke-width', 2.5) // Maintaining the thicker line
                .attr('d', createLine);
        });
    }

    onMount(() => {
        createLineChart(data);
    });
</script>

<svg id="linechart" style="width: 300px; height: 300px;"></svg> <!-- Adjusted to 300px -->

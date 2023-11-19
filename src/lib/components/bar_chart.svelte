<!-- DROPDOWN -->
<select bind:value={selected}>
    {#each dd as d}
        <option value={d}>
            {d.label}
        </option>
    {/each}
</select>
<p/>
<!-- BAR CHART -->
<svg bind:this={svgLocal} class="bar-chart"/>
<p/>
<!-- CHECKBOXES-->
{#each cc as c, i (c.id)}
	<label>
		<input
			type="checkbox"
			value={c}
            disabled={ccr.length===1 && ccr[0]===c}
			bind:group={ccr}
		/>
		{c.label}
	</label>
{/each}

<p>{selected.id + ": " + selected.label}</p>
<p>Checkbox selected: {ccr.map(x=>x.id + ": " + x.label).join(", ")}</p>

<script>    
    export let data = []
    let d = data
    let svgLocal
    
    let cc = [
        {id: 6, label: "Nahverkehr Tram"},
        {id: 7, label: "Nahverkehr Bus"},
        {id: 8, label: "Nahverkehr Bahn"},
        {id: 9, label: "gesamt"},
    ]
    let ccr = [cc[0]];

    let dd = [
        {id: 3, label: "Anzahl Unternehmen"}, 
        {id: 4, label: "Beförderte Personen"}, 
        {id: 5, label: "Personenkilometer"}
    ]
    let selected = dd[0]

    import * as d3 from 'd3'
	import { onMount } from 'svelte';

    onMount(() => {
        const width = 300
        const height = 300
        
        const svg = d3.select(svgLocal) //const svg = d3.select("svg.bar-chart")        
            .attr("width", width)
            .attr("height", height);

        //let d = [{y:2010, v: 3},{y:2011, v: 4},{y:2012, v: 5},{y:2013, v: 6}]
        //d = [{y:2011, v: 4},{y:2012, v: 5},{y:2013, v: 6}]
        const years = d.map(d=>d.y)

        //const years = [2010, 2011, 2012, 2013]
        const values = [1,2,3,4,5,6,7]
        const scaleYears = d3.scaleBand()
                    .domain(years)
                    .range([0, width]).padding(0.5)
        const scaleValues = d3.scaleLinear()
                    .domain([d3.max(values), 0])
                    .range([0, height-40])
                    
        const axisYears = d3.axisBottom(scaleYears);   
        const axisValues = d3.axisLeft(scaleValues);             

        svg.append("g")            
            .attr("transform", `translate(30, ${height-30})`)
            .call(axisYears)
        svg.append("g")
            .attr("transform", "translate(30, 10)")
            .call(axisValues)

        svg.selectAll(".bar")
            .data(d)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("transform", `translate(30, 0)`)
            .attr("x", function(d) { return scaleYears(d.y)  })
            .attr("y", function(d) { return scaleValues(d.v) })
            .attr("width", scaleYears.bandwidth())
            .attr("height", function(d) { return height - scaleValues(d.v) - 30 });
    })
</script>
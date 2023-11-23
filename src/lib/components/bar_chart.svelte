<div id="barchart-dropdown">
    <!-- DROPDOWN -->
    <select bind:value={selected}>
        {#each dd as d}
            <option value={d}>
                {d.label}
            </option>
        {/each}
    </select>
    <p/>
</div>
<div id="barchart-diagram">
    <!-- BAR CHART -->
    <svg bind:this={svgLocal} id="bar-chart"/>
    <p/>
</div>
<div id="barchart-checkboxes">
    <!-- CHECKBOXES-->
    {#each cc as c, i (c.id)}
    <label style="color:{colors[c.color]}">
        <input
            type="checkbox"
            value={c}            
            disabled={ccr.length===1 && ccr[0]===c}
            bind:group={ccr}
        />
        {c.label}
    </label>
{/each}
<!--
<p>{selected.id + ": " + selected.label}</p>
<p>Checkbox selected: {ccr.map(x=>x.id + ": " + x.label).join(", ")}</p>
<p>a: {a}</p>
<p><b>stats:</b> {stats}</p>
-->
</div>



<script>    
let a = 0
    export let data = []
    //let d = data.data
    let stats = null

    let svgLocal
    
    // Linienfernverkehr mit Eisenbahnen
    // Linienfernverkehr mit Omnibussen
    // Liniennahverkehr insgesamt
    // Liniennahverkehr mit Eisenbahnen
    // Liniennahverkehr mit Omnibussen
    // Liniennahverkehr mit Straßenbahnen
    const colors = { 1:'#d62828', 2:'#f77f00', 3: '#003049', 4:'#fcbf49' }
    let cc = [
        {id: 6, label: "Tram", orig: "Liniennahverkehr mit Straßenbahnen", color: 1},
        {id: 7, label: "Bus", orig: "Liniennahverkehr mit Omnibussen", color: 2},
        {id: 8, label: "Train", orig: "Liniennahverkehr mit Eisenbahnen", color: 3},
        {id: 9, label: "Total", orig: "Liniennahverkehr insgesamt", color: 4},
    ]
    let ccr = [cc[0]];

    // Anzahl_Unternehmen
    // Befoerderte_Personen_in_1000
    // Personenkilometer_in_1000
    let dd = [
        {id: 3, label: "Anzahl Unternehmen", orig: "Anzahl_Unternehmen"}, 
        {id: 4, label: "Beförderte Personen in 1000", orig: "Befoerderte_Personen_in_1000"}, 
        {id: 5, label: "Personenkilometer in 1000", orig: "Personenkilometer_in_1000"}
    ]
    let selected = dd[0]

    //const sel = cc.map(c=>c.orig)
    //const maxVal = d.reduce((agg, v) => Math.max(agg, v["Liniennahverkehr insgesamt"] ?? 0), 0)    
    //alert(maxVal)

    import * as d3 from 'd3'
	import { onMount } from 'svelte';
    import {afterUpdate } from 'svelte';
    
    $: data, selected, ccr, updateGraph();

    let ready = false
    function updateGraph() {
        if (!ready) return

        let d = data.data


        // Filter data for years starting from 2016
        d = d.filter((entry) => entry.Jahr >= 2016);

        //  "Befoerderte_Personen_in_1000"}, Liniennahverkehr mit Straßenbahnen
        //let xxx = d.filter(d=>d.Art === "Liniennahverkehr mit Straßenbahnen")
        //xxx = xxx.filter(d=>d.Jahr === 2004)
        //alert(JSON.stringify(xxx))
        //stats = xxx.reduce((agg,d)=>agg+xxx.Befoerderte_Personen_in_1000, 0)

        a++
        //stats = selected.orig
        //const sel = cc.map(c=>c.orig)
        //const maxVal = d.reduce((agg, v) => Math.max(agg, v["Liniennahverkehr insgesamt"] ?? 0), 0)    
        let maxVal = 0;
        for(const x of d) {
            //if (x.Art !== "Liniennahverkehr insgesamt") continue
            maxVal = Math.max(x[selected.orig], maxVal)
        }
        //stats = maxVal
        var parentDiv = document.getElementById("barchart-parent");
        var checkboxHeight = document.getElementById("barchart-checkboxes").clientHeight;
        var dropdownHeight = document.getElementById("barchart-dropdown").clientHeight;
        var width = parentDiv.clientWidth;
        var height = parentDiv.clientHeight - (checkboxHeight + dropdownHeight);

        // var width = 410
        // var height = 280


        // const width = $("svg").parent().width();
        // const height = $("svg").parent().height();

        d3.select(svgLocal).selectAll("*").remove();
        
        const svg = d3.select(svgLocal) //const svg = d3.select("svg.bar-chart")        
            .attr("width", width)
            .attr("height", height);

        //let d = [{y:2010, v: 3},{y:2011, v: 4},{y:2012, v: 5},{y:2013, v: 6}]
        //d = [{y:2011, v: 4},{y:2012, v: 5},{y:2013, v: 6}]
        const years = d.map(d=>d.Jahr)

        //const years = [2010, 2011, 2012, 2013]
        //const values = [1,2,3,4,5,6,7]
        const scaleYears = d3.scaleBand()
                    .domain(years)
                    .range([0, width-80]).padding(0.1)
        const scaleValues = d3.scaleLinear()
                    .domain([maxVal/*d3.max(values)*/, 0])
                    .range([0, height-40])
                    
        const axisYears = d3.axisBottom(scaleYears);   
        const axisValues = d3.axisLeft(scaleValues);             

        svg.append("g")            
            .attr("transform", `translate(70, ${height-30})`)
            .call(axisYears)
        svg.append("g")
            .attr("transform", "translate(70,10)")
            .call(axisValues)

        //alert(ccr.map(c=>c.label).join("+"))
        /*
        svg.selectAll(".bar")
            .data(d)
            .enter().append("rect")
            .attr("class", "bar")
            .attr("fill", colors[cc[0].color])
            .attr("transform", `translate(70, 0)`)
            .attr("x", function(d) { return scaleYears(d.Jahr)  })
            .attr("y", function(d) { return scaleValues(300)+10 })
            .attr("width", scaleYears.bandwidth())
            .attr("height", function(d) { return height - scaleValues(300) - 40 });
        */

        //let maxxx = 0
        function getValue(d) {
            //maxxx = Math.max(0, d[selected.orig])
            //stats = maxxx
            return d[selected.orig]
        }        
        
        for(const [i, c] of ccr.entries()) {
            const g = svg.append("g")
            //stats = scaleYears.bandwidth()

            const ww = scaleYears.bandwidth()/4
            g.selectAll(".bar")
                .data(d)                
                .enter()
                .filter(d=>d.Art===c.orig)
                .append("rect")                
                .attr("class", "bar")
                .attr("fill", colors[c.color])
                .attr("transform", `translate(70, 0)`)
                .attr("x", function(d) {
                    const x = scaleYears(d.Jahr)
                    const w = scaleYears.bandwidth()
                    //return x+w/2 - ww/2                    
                    //return x + w/2 * (i+1)
                    return x + w/2 + (i*ww) - ccr.length*ww/2
                })
                .attr("y", function(d) { return scaleValues(getValue(d))+10 })
                .attr("width", ww)
                .attr("height", function(d) { return height - scaleValues(getValue(d)) - 40 });
        }
    }

    onMount(() => {
        ready = true;
        updateGraph();
    })
</script>

<style>
    #bar-chart {
        width: 100%;
        height: 100%;
    }

  /* Style for checkboxes */
  #barchart-checkboxes label {
    display: inline-block;
    margin-right: 15px; /* Adjust as needed for spacing between checkboxes */
  }

  input {
    margin-right: 5px; /* Adjust as needed for spacing between checkbox and label text */
  }
</style>
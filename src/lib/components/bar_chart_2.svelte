<script>
	export let stateName = 'Deutschland';
	export let data = [];
    export let year = null;

	let svgLocal;
	let tooltip;

	let radioButtons = [
		{ id: 6, label: 'Tram', orig: 'Liniennahverkehr mit Straßenbahnen', color: 'var(--colorscheme-red)' },
		{ id: 7, label: 'Bus', orig: 'Liniennahverkehr mit Omnibussen', color: 'var(--colorscheme-orange)' },
		{ id: 8, label: 'Train', orig: 'Liniennahverkehr mit Eisenbahnen', color: 'var(--colorscheme-blue)' },
		{ id: 9, label: 'Total', orig: 'Liniennahverkehr insgesamt', color: 'var(--colorscheme-yellow)' }
	];
	let selectedRadioButton = radioButtons[0];
    $: selectedRadioButton, console.log("radio", selectedRadioButton)

	import * as d3 from 'd3';
	import { onMount } from 'svelte';

	// update graph reactively
	$: data, selectedRadioButton, updateGraph();

	let ready = false;
	async function updateGraph() {
		if (!ready) return;
        await tick(); // otherwise layout does weird stuff?

        const bl = [
            { abbr: 'BW', full: 'Baden-Württemberg' },
            { abbr: 'BY', full: 'Bayern' },
            { abbr: 'BE', full: 'Berlin' },
            { abbr: 'BB', full: 'Brandenburg' },
            { abbr: 'HB', full: 'Bremen' },
            { abbr: 'HH', full: 'Hamburg' },
            { abbr: 'HE', full: 'Hessen' },
            { abbr: 'MV', full: 'Mecklenburg-Vorpommern' },
            { abbr: 'NI', full: 'Niedersachsen' },
            { abbr: 'NW', full: 'Nordrhein-Westfalen' },
            { abbr: 'RP', full: 'Rheinland-Pfalz' },
            { abbr: 'SL', full: 'Saarland' },
            { abbr: 'SN', full: 'Sachsen' },
            { abbr: 'ST', full: 'Sachsen-Anhalt' },
            { abbr: 'SH', full: 'Schleswig-Holstein' },
            { abbr: 'TH', full: 'Thüringen' },
        ];

        // size
        var parentDiv = document.getElementById('barchart2-parent') ?? document.getElementById('barchart2-leftViz-parent');
		var radioButtonsHeight = document.getElementById('barchart-radio-buttons').clientHeight;
		var width = parentDiv.clientWidth;
		var height = 0.95 * parentDiv.clientHeight - (radioButtonsHeight) - 70;

		d3.select(svgLocal).selectAll('*').remove();
        if(!stateName || stateName === "Deutschland") return;

		const svg = d3
			.select(svgLocal)
            .style("background-color", "transparent")
			.attr('width', width)
			.attr('height', height);

        let pad = ({top: 0, right: 10, bottom: 30, left: 140});
        const scaleBL = d3
			.scaleBand()
			.domain(bl.map(x=>x.full))
			.range([0, height-pad.bottom-pad.top])
			.padding(0.1);

        //const dummySelf = 0;
        const dummyValues = [-80, -70, -60, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 60, 70, 80];
        //const dummyConcat = [].concat(dummySelf, dummyValues);
        const blIndex = bl.findIndex(x => x.full === stateName);
        dummyValues[blIndex] = 0;

        const scaleValues = d3
            .scaleLinear()
			.domain([d3.min(dummyValues), d3.max(dummyValues)])
			.range([0, width-pad.left-pad.right]);
            
        const axisBL = d3.axisLeft(scaleBL);
		const axisValues = d3.axisBottom(scaleValues);

        svg.append('g')
           .attr('transform', `translate(${pad.left}, ${pad.top})`)
		   .call(axisBL);

        svg.append('g')
           .attr('transform', `translate(${pad.left}, ${height-pad.bottom})`)
		   .call(axisValues);

        const g = svg.append('g');
        g.selectAll('.bar')
            .data(bl)
            .enter()
            .append('rect')
            .attr('class', 'bar')
            .attr('fill', 'red')
            .attr('transform', `translate(${pad.left}, 0)`)           
            .attr('x', function(d) {
                const val = dummyValues[bl.indexOf(d)];
                return val < 0 ? scaleValues(dummyValues[bl.indexOf(d)]) : scaleValues(0);
            })
            .attr('y', function(d) {
                return scaleBL(d.full)
            })
            .attr('width', function(d) {
                return Math.abs(scaleValues(0) - scaleValues(dummyValues[bl.indexOf(d)]));
            })
            .attr('height', function(d) {
                return scaleBL.bandwidth();
            });
        g.append('circle')
         .attr('cx', scaleValues(0) + pad.left)
         .attr('cy', scaleBL(bl[blIndex].full) + scaleBL.bandwidth()/2)
         .attr('r', 8)
         .style('fill', 'var(--colorscheme-orange)')

        g.append("text")
        .attr("x", 30+scaleValues(0) + pad.left)
        .attr("y", scaleBL(bl[blIndex].full) + scaleBL.bandwidth()/2)
        .attr("dy", "0.35em")
        .attr("text-anchor", "middle")
        .style("fill", "#000")
        .text(year);

        
	}

    function handleResize() {
		updateGraph();
	}

	onMount(() => {
		ready = true;
		updateGraph();

        window.addEventListener('resize', handleResize);
		return () => {
			window.removeEventListener('resize', handleResize);
		};
	});

    // react to year update
    let yearPrev = null;
	function yearUpdated() {
		if (!ready) return;
		if (yearPrev === year) return;
		yearPrev = year;
	}
	$: year, yearUpdated();
    $: yearPrev, updateGraph();

    import { tick } from 'svelte';
    /*async function ticked() {
        
        updateGraph();
    }*/
    $: stateName, updateGraph();

    export async function updateLayout() {
        await updateGraph();
    }
	
</script>

<div style="display: {stateName!=='Deutschland'?'block':'none'}">
    <div id="barchart-diagram">
        <!-- BAR CHART -->
        <svg bind:this={svgLocal} id="bar-chart" />
    </div>
    <div id="barchart-radio-buttons">
        <!-- CHECKBOXES-->
        {#each radioButtons as c, i (c.id)}
            <label>
                <input
                    type="radio"
                    value={c}
                    bind:group={selectedRadioButton}
                    style="accent-color:{c.color};"
                />
                {c.label}
            </label>
        {/each}
    </div>
</div>

<div style="height:100%;align-items:center; justify-content:center; display: {stateName==='Deutschland'?'flex':'none'}">
Bitte Bundesland auf der Karte auswählen.
</div>

<!--<div style="height:100%;align-items:center; justify-content:center; display: {stateName!=='Deutschland'?'flex':'none'}">
    {year}
</div>-->

<style>

	.tooltip {
		position: absolute;
		opacity: 0;
		pointer-events: none;
		background-color: #fff;
		border: 1px solid #000;
		padding: 10px;
	}

	#bar-chart {
		width: 100%;
		height: 100%;
	}

	#barchart-diagram {
		width: 100%;
		height: 85%;
	}

	#barchart-radio-buttons {
		width: 100%;
		height: 5%;
	}

	/* Style for radio buttons */
	#barchart-radio-buttons label {
		display: inline-block;
		margin-right: 15px; /* Adjust as needed for spacing between radio buttons */
	}

	input {
		margin-right: 1px;
	}

	
</style>

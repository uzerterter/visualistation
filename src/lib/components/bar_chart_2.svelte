<script>
	export let stateName = 'Deutschland';
	export let data = [];
    export let year = null;
    export let parentId

	let svgLocal;
	let tooltip;

    export let dropdownItems = null
    export let selectedDropdownItem = null

	let radioButtons = [
		{ id: 6, label: 'Tram', orig: 'Liniennahverkehr mit Straßenbahnen', color: 'var(--colorscheme-red)' },
		{ id: 7, label: 'Bus', orig: 'Liniennahverkehr mit Omnibussen', color: 'var(--colorscheme-orange)' },
		{ id: 8, label: 'Train', orig: 'Liniennahverkehr mit Eisenbahnen', color: 'var(--colorscheme-blue)' },
		{ id: 9, label: 'Total', orig: 'Liniennahverkehr insgesamt', color: 'var(--colorscheme-yellow)' }
	];
	let selectedRadioButton = radioButtons[0];
    //$: selectedRadioButton, console.log("radio", selectedRadioButton)

	import * as d3 from 'd3';
	import { onMount } from 'svelte';

	// update graph reactively
	$: data, selectedRadioButton, selectedDropdownItem, dropdownItems, updateGraph();

	let ready = false;
	async function updateGraph() {
		if (!ready) return;
        await tick(); // otherwise layout does weird stuff?
                
        if (!stateName || stateName === "Deutschland") return
        if (!selectedDropdownItem) return
        if (!dropdownItems) return        
        if (!year) return

        let bl = [
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
        bl = bl.filter(x=>x.full !== stateName)

        const dOth = {...data, data: data.data.filter(item => 
            item.Bundesland !== stateName && item.Bundesland !== "Deutschland" &&
            item.Jahr === year &&
            item.Art === selectedRadioButton.orig)
        }        
        const dBl = {...data, data: data.data.filter(item =>
            item.Bundesland === stateName &&
            item.Jahr === year &&
            item.Art === selectedRadioButton.orig)
        }

        const dOth2 = dOth.data.reduce((acc,item) => {
            if (!acc[item.Bundesland]) acc[item.Bundesland] = 0;
            acc[item.Bundesland] += item[selectedDropdownItem.orig];
            return acc;
        }, {})
        const dBl2 = dBl.data.reduce((acc,cur) => acc + cur[selectedDropdownItem.orig], 0)

        for(let x of Object.values(bl)) {
            if (!dOth2[x.full]) dOth2[x.full] = 0
        }

        const bl2 = []        
        for(const d of Object.keys(dOth2)) {
            const clicked = dBl2;
            const other = dOth2[d];
            const val = -(100 - other/clicked*100)
            bl2.push({...bl.filter(x=>x.full === d)[0], dataVal: val})
        }

        bl = bl2        
        bl.sort((a,b)=>a.full>b.full)
        const dataValues = bl.map(x=>x.dataVal)

        // push center clicked value
        bl.push(0)
        dataValues.push(0)

        // decide if we need to equalize left and right side
        const min = dataValues.reduce((acc,cur)=>Math.min(acc,cur), Infinity)
        const max = dataValues.reduce((acc,cur)=>Math.max(acc,cur), -Infinity)
        let equalized = (() => {
            if (Math.abs(min) > Math.abs(max)) {
                bl.push(-min)
                dataValues.push(-min)
            } else if (Math.abs(max) > Math.abs(min)) {
                bl.push(-max)
                dataValues.push(-max)
            } else { return false }
            return true
        })()

        // size
        var parentDiv = document.getElementById(parentId)
		var radioButtonsHeight = document.getElementById('barchart-radio-buttons').clientHeight;
		var width = parentDiv.clientWidth;
		var height = 0.95 * parentDiv.clientHeight - (radioButtonsHeight) - 70;

        //console.log(parentDiv.clientWidth, parentDiv.clientHeight)

		d3.select(svgLocal).selectAll('*').remove();
        //if(!stateName || stateName === "Deutschland") return; doppelt?

        if (dBl2 === 0) {
            // do something else if clicked element has no value
        }

		const svg = d3
			.select(svgLocal)
            .style("background-color", "transparent")
			.attr('width', width)
			.attr('height', height);

        bl.pop() // remove clicked Bundesland
        if (equalized) bl.pop() // remove equalizer

        let pad = ({top: 0, right: 10, bottom: 30, left: 140});
        const scaleBL = d3
			.scaleBand()
			.domain(bl.map(x=>x.full))
			.range([0, height-pad.bottom-pad.top])
			.padding(0.1);

        const scaleValues = d3
            .scaleLinear()
			.domain([d3.min(dataValues), d3.max(dataValues)])
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
            .attr('fill', selectedRadioButton.color)
            .attr('transform', `translate(${pad.left}, 0)`)           
            .attr('x', function(d) {
                const val = dataValues[bl.indexOf(d)];
                return val < 0 ? scaleValues(dataValues[bl.indexOf(d)]) : scaleValues(0);
            })
            .attr('y', function(d) {
                return scaleBL(d.full)
            })
            .attr('width', function(d) {
                return Math.abs(scaleValues(0) - scaleValues(dataValues[bl.indexOf(d)]));
            })
            .attr('height', function(d) {
                return scaleBL.bandwidth();
            });
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

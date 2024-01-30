<script>
	export let stateName = 'Deutschland';
	export let data = [];
    export let year = null;
    export let parentId

	let svgLocal;
	let tooltip;

    export let dropdownItems = null
    export let selectedDropdownItem = null

	export let radioButtons
    let radioButtonsDivs

	let selectedRadioButton = radioButtons[0];
    //$: selectedRadioButton, console.log("radio", selectedRadioButton)

	import * as d3 from 'd3';
	import { onMount } from 'svelte';

	// update graph reactively
	$: data, selectedRadioButton, selectedDropdownItem, /*dropdownItems,*/ updateGraph();

	let ready = false;
	async function updateGraph() {
		if (!ready) return;
        if (radioButtons.length === 1) {
            document.getElementById('barchart-radio-buttons').style.opacity=0
        }
        radioButtons = radioButtons // update for gray
        await tick(); // otherwise layout does weird stuff?
                
        if (!stateName || stateName === "Deutschland") return
        if (!selectedDropdownItem) return
        //if (!dropdownItems) return        
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
            (!selectedRadioButton.orig ? true : (item.Art === selectedRadioButton.orig)))
        }        
        const dBl = {...data, data: data.data.filter(item =>
            item.Bundesland === stateName &&
            item.Jahr === year &&
            (!selectedRadioButton.orig ? true : (item.Art === selectedRadioButton.orig)))
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
		var radioButtonsHeight = radioButtonsDivs.clientHeight;
		var width = parentDiv.clientWidth;
		var height = 0.95 * parentDiv.clientHeight - 20;

        //console.log(parentDiv.clientWidth, parentDiv.clientHeight)

		d3.select(svgLocal).selectAll('*').remove();
        //if(!stateName || stateName === "Deutschland") return; doppelt?

        let pad = ({top: 0, right: 15, bottom: 30, left: 45});

        if (dBl2 === 0) {
            const label = selectedRadioButton.label;
            d3.select(svgLocal).append("text")
            .attr("x", pad.left + (width-pad.left-pad.right)/2)
            .attr("y", (height-pad.bottom)/2)
            .attr("text-anchor", "middle")
            .style('opacity', 0.75)
            .text(`No ${label?label+" data":"data"}`);
        }

        function moveTooltip(event) {
			tt.style('left', `${event.pageX - ttw / 2}px`).style('top', `${event.pageY - tth - 10}px`);
		}

        const tt = d3.select(tooltip);
        let [ttw, tth] = [null, null];

		const svg = d3
			.select(svgLocal)
            .style("background-color", "transparent")
			.attr('width', width)
			.attr('height', height);

        bl.pop() // remove clicked Bundesland
        if (equalized) bl.pop() // remove equalizer
        
        const scaleBL = d3
			.scaleBand()
			.domain(bl.map(x=>x.full))
			.range([0, height-pad.bottom-pad.top])
			.padding(0.1);

        const scaleValues = d3
            .scaleLinear()
			.domain([d3.min(dataValues), d3.max(dataValues)])
			.range([0, width-pad.left-pad.right]);
            
        const axisBL = d3.axisLeft(scaleBL)
            .tickSizeOuter(0)
            .tickFormat((d) => {
                const abbreviation = bl.find((item) => item.full === d)?.abbr;
                return abbreviation || d; // Use abbreviation if found, else use full name
            });
		const axisValues = d3.axisBottom(scaleValues).tickSizeOuter(0);
        axisValues.tickFormat(x=>(x>0?`+${x}`:x)+"%");

        function adjustLabelFrequency(axis) {
            const axisNode = svg.append('g').call(axis);
            let tickWidth = 0;
            axisNode.selectAll('.tick').each(function() {
                tickWidth = Math.max(tickWidth, this.getBBox().width);
            });
            const w = width - pad.left - pad.right;
            const _numberOfTicks = Math.floor(w / (tickWidth*1.3));
            const numberOfTicks = Math.floor(_numberOfTicks);
            axis.ticks(numberOfTicks);
            axisNode.remove();
        }
        adjustLabelFrequency(axisValues)

        svg.append('g')
           .attr('transform', `translate(${pad.left}, ${pad.top})`)
		   .call(axisBL);

        svg.append('g')
           .attr('transform', `translate(${pad.left}, ${height-pad.bottom})`)
		   .call(axisValues)
           // Extend tick lines to the right edge
           .call((g) => g.selectAll('.tick line').attr('y2', -height+pad.bottom+pad.top));

        // Set opacity for the axis line
		svg.selectAll('.domain')
		   .style('opacity', 0.5)
		   .style('stroke', 'rgb(114, 119, 123)');

        // Set opacity for the tick lines
        svg.selectAll('.tick line')
		   .style('opacity', 0.5)
		   .style('stroke', 'rgb(114, 119, 123)');

        // Set opacity for the tick text
		svg.selectAll('.tick text').style('opacity', 0.75)

        const g = svg.append('g');
        const bar = g.selectAll('.bar')

        bar.data(bl)
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
            })

        // make small areas hover-able
        const hoverPad = 16
        bar.data(bl)
            .enter()
            .append('rect')
            .attr('class', 'bar')
            .attr('fill', "transparent")
            .attr('transform', `translate(${pad.left}, 0)`)
            .attr('x', function(d) {
                const val = dataValues[bl.indexOf(d)];
                const w = Math.abs(scaleValues(0) - scaleValues(val));
                const hp = w <= hoverPad ? hoverPad : 0
                return (val < 0 ? scaleValues(val) : scaleValues(0)) - hp/2;
            })
            .attr('y', function(d) {
                return scaleBL(d.full)
            })
            .attr('width', function(d) {
                const val = dataValues[bl.indexOf(d)];
                const w = Math.abs(scaleValues(0) - scaleValues(val));
                const hp = w <= hoverPad ? hoverPad : 0
                return w + hp
            })
            .attr('height', function(d) {
                return scaleBL.bandwidth();
            })
            .on('mouseover', function (event, x) {
                // const stateAbbreviation = bl.find((item) => item.full === x.full)?.abbr;
                const stateName = x.full;
                const val = dataValues[bl.indexOf(x)];
                const color = selectedRadioButton.color;

                tt.transition().duration(0).style('opacity', 1).style('color', color);

                const t = d3.format(',')(val.toFixed(2)) + "%";
                const tooltipText = `${stateName}: ${val > 0 ? `+${t}` : t}`;

                tt.html(tooltipText);

                const rect = tt.node().getBoundingClientRect();
                ttw = rect.width;
                tth = rect.height;
                moveTooltip(event);
            })
            .on('mousemove', function (event) {
                moveTooltip(event);
            })
            .on('mouseout', function () {
                tt.transition().duration(100).style('opacity', 0);
            });
	}

    function handleResize() {
		updateGraph();
        updateGraph(); // two better for some reason
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

    function getDbl2(radioButton) {
        const dBl = {...data, data: data.data.filter(item =>
            item.Bundesland === stateName &&
            item.Jahr === year &&
            (!radioButton.orig ? true : (item.Art === radioButton.orig)))
        }
        const dBl2 = dBl.data.reduce((acc,cur) => acc + cur[selectedDropdownItem.orig], 0)
        return dBl2
    }
	
</script>

<div bind:this={tooltip} class="tooltip" style="display: block"/>
<div style="height:100%;display: {stateName!=='Deutschland'?'block':'none'}">
    <div id="barchart-diagram">
        <!-- BAR CHART -->
        <svg bind:this={svgLocal} id="bar-chart" />
    </div>
    <div id="barchart-radio-buttons" bind:this={radioButtonsDivs}>
        <!-- CHECKBOXES-->
        {#each radioButtons as c, i (c.id)}
            <label style="opacity:{getDbl2(c)===0?0.5:1}">
                <input
                    _disabled={getDbl2(c)===0}
                    type="radio"
                    value={c}
                    bind:group={selectedRadioButton}
                    style="accent-color:{getDbl2(c)===0?"gray":c.color};"
                />
                {c.label}
            </label>
        {/each}
    </div>
</div>

<div style="height:100%;align-items:center; justify-content:center; display: {stateName==='Deutschland'?'flex':'none'}">
Please select a federal state on the map.
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
		height: 90%;
	}

	#barchart-radio-buttons {
		width: 100%;
		height: 10%;
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

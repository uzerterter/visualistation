<script>
	export let stateName = 'Deutschland';
	export let data = [];
	export let selectedYearValue = 2017;
	export let year;
	let svgLocal;
	let tooltip;
  
	import * as d3 from 'd3';
	import { onMount } from 'svelte';
  
	// update graph reactively
	$: data, stateName, filterData(), updateGraph();
  
	let filteredData = null;
	function filterData() {
		filteredData = {
			...data,
			data: data.data
				.filter(item => item.Bundesland === stateName && (item.Jahr >= 2017 && item.Jahr <= 2022))
				.sort((a, b) => a.Jahr - b.Jahr) // Sort data by Jahr in ascending order
		};
	}
  
	let ready = false;
	function updateGraph() {
	  if (!ready) return;
  
	  let d = filteredData.data;
  
	  // Filter data for years starting from 2017
	  d = d.filter((entry) => entry.Jahr >= 2017);

	  let maxVal = d3.max(d, entry => entry.Prozent);
  
	  var parentDiv = document.getElementById('barchart-leftViz-parent');
		var width = parentDiv.clientWidth;
		var height = 0.95 * parentDiv.clientHeight - 20; 
  
	  d3.select(svgLocal).selectAll('*').remove();
  
	  const svg = d3
		.select(svgLocal)
		.attr('width', width)
		.attr('height', height);
  
	  const years = d.map((d) => d.Jahr);
  
	  const scaleYears = d3
		.scaleBand()
		.domain(years)
		.range([0, width - 60])
		.padding(0.1);
  
		const scaleValues = d3
            .scaleLinear()
            .domain([maxVal, 0])
            .range([0, height - 40]);
  
	  const axisYears = d3.axisBottom(scaleYears).tickSizeOuter(0); // Remove outer ticks
	  const axisValues = d3.axisLeft(scaleValues).tickSizeOuter(0).tickFormat(d => d + '%'); // Remove outer ticks
  
	  function moveTooltip(event) {
		tt.style('left', `${event.pageX - ttw / 2}px`).style('top', `${event.pageY - tth - 10}px`);
	  }
  
	  // mouse move in between bars to avoid jumpy behavior (optional)
	  svg
		.append('g')
		.append('rect')
		.attr('width', width)
		.attr('height', height)
		.style('opacity', 0)
		.on('mousemove', function (event) {
		  moveTooltip(event);
		});
  
	  svg
		.append('g')
		.attr('transform', `translate(50, ${height - 30})`)
		.call(axisYears)
		.selectAll('.tick text') // Select the text elements
		.attr('class', (d) => `tick-text ${getClassForYear(d)}`);
  
	  svg
		.append('g')
		.attr('transform', 'translate(50,10)')
		.call(axisValues)
		.call((g) => g.selectAll('.tick line').attr('x2', width - 60)); // Extend tick lines to the right edge
  
	  // Set opacity for the axis line
	  svg
		.selectAll('.domain')
		.style('opacity', 0.5) // Set opacity for the axis line
		.style('stroke', 'rgb(114, 119, 123)'); // Set color for the axis line
  
	  // Set opacity for the tick lines
	  svg
		.selectAll('.tick line')
		.style('opacity', 0.5) // Set opacity for the tick lines
		.style('stroke', 'rgb(114, 119, 123)'); // Set color for the tick lines
  
	  // Set opacity for the tick text
	  svg.selectAll('.tick text').style('opacity', 0.75); // Set higher opacity for text
  
	  function getValue(d) {
		return d.Prozent;
	  }
  
	  const tt = d3.select(tooltip);
	  let [ttw, tth] = [null, null];
  
	  // Create a class string for bars of the selected year
	  function getClassForYear(year) {
		const className = `year-${year}`;
		return className;
	  }
  
	  const g = svg.append('g');
  
	  const ww = scaleYears.bandwidth();
	  g.selectAll('.bar')
		.data(d)
		.enter()
		.append('rect')
		.attr('fill', 'var(--colorscheme-left2)')
		.attr('transform', `translate(50, 0)`)
		.on('mouseover', function (event, x) {
		  const color = 'var(--colorscheme-blue)';
		  tt.transition().duration(0).style('opacity', 1).style('color', color);
		  tt.html(d3.format(',')(x.Prozent)  + '%');
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
		})
		.attr('x', function (d) {
		  return scaleYears(d.Jahr);
		})
		.attr('y', function (d) {
		  return scaleValues(d.Prozent) + 10;
		})
		.attr('width', ww)
		.attr('height', function (d) {
		  return height - scaleValues(d.Prozent) - 40
		});
  
	  // Apply styling to the current year when updating graph
	  applyStylingToCurrentYear(selectedYearValue);
	}
  
	function handleResize() {
	  updateGraph();
	}
  
	onMount(() => {
	  filterData();
	  ready = true;
	  updateGraph();
	  applyStylingToCurrentYear(selectedYearValue);
  
	  window.addEventListener('resize', handleResize);
	  return () => {
		window.removeEventListener('resize', handleResize);
	  };
	});
  
	// Use a reactive statement to apply styling when selectedYearValue changes
	$: {
	  applyStylingToCurrentYear(selectedYearValue);
	}
  
	let selectedYearClass = "";
  
	function applyStylingToCurrentYear(selectedYearValue) {
	  if (!ready) return;
  
	  if (selectedYearValue === undefined) return;
  
	  // Remove styling from all years except the current one
	  const allYearClasses = [2017, 2018, 2019, 2020, 2021, 2022];
	  allYearClasses.forEach(year => {
		if (year !== selectedYearValue) {
		  const yearElements = document.querySelectorAll(`.year-${year}`);
		  yearElements.forEach(element => {
			// Remove the styling or update it as needed
			element.style.cssText = "";
		  });
		}
	  });
  
	  // Update the selectedYearClass when selectedYearValue changes
	  selectedYearClass = selectedYearValue ? `year-${selectedYearValue}` : "";
  
	  // Apply styling to the current selected year class
	  const currentYearElements = document.querySelectorAll(`.${selectedYearClass}`);
	  currentYearElements.forEach(element => {
		// Apply the styling as needed
		element.style.cssText += "opacity:1; font-weight: bold; color: var(--colorscheme-orange); ";
	  });
	}
  
	// react to year update
	let yearPrev = null;
	function yearUpdated() {
	  if (!ready) return;
	  if (yearPrev === year) return;
	  yearPrev = year;
	}
  
	$: year, yearUpdated();
	$: yearPrev, null; // todo highlight
  
	// tabs
	import { tick } from 'svelte';
	let activeTabId = 'barchart1';
	let tabs;
	let barChart2;
	async function openTab(_, id) {
	  activeTabId = id;
  
	  await tick();
	  updateGraph();
	  await barChart2.updateLayout();
  
	  // otherwise click on button again resizes again for some reason?
	  await tick();
	  updateGraph();
	  await barChart2.updateLayout();
	}
  </script>
  
  <!-- <div bind:this={tabs} class="tabs">
	<button class="tab {activeTabId==='barchart1'?'active':''}" on:click={e=>openTab(e, 'barchart1')}>
	  Jahre (absolut)
	</button>
	<button class="tab {activeTabId==='barchart2'?'active':''}" on:click={e=>openTab(e, 'barchart2')}>
	  Bundesländer (relativ)
	</button>
  </div> -->
  
  <!-- BAR CHART 1 -->
  <div bind:this={tooltip} class="hover-tooltip" style="display: {'barchart1'===activeTabId?'block':'none'}"/>
  <div id="barchart-diagram" style="display: {'barchart1'===activeTabId?'block':'none'}">
	<!-- BAR CHART -->
	<svg bind:this={svgLocal} id="bar-chart" />
  </div>

  <div id="barchart-checkboxes" style="display: {'barchart1'===activeTabId?'block':'none'}">
</div>
  
  <style>
	/* .tabs {           
	  margin-top:10px;
	  margin-bottom:0px;
	  width:100%;
	  overflow: hidden;
	}
  
	.tabs button {
	  width:50%;
	  background-color: inherit;
	  float: left;
	  border: none;
	  outline: none;
	  cursor: pointer;
	  margin-top:0px;
	  margin-bottom: 2px;
	  padding: 2px 16px;
	  transition: 0.3s;
	  border-bottom: 2px solid transparent;
	}
  
	.tabs button:hover {
	  background-color: #ddd;
	}
  
	.tabs button.active {
	  border-bottom-color: #444;
	} */
  
	.hover-tooltip {
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

	#barchart-checkboxes {
		width: 100%;
		height: 10%;
	}
  </style>
  
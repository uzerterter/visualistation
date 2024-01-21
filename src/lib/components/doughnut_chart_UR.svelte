<script>
	import { onMount } from 'svelte';
	import * as d3 from 'd3';
	import { selectedYear } from '$lib/components/timeline.svelte';

	export let stateName = 'Deutschland';
	let highlightedState = '';

	export let realData = [];

	export let isActive = false;
	let ready = false;

	function transformData(inputData) {
		const years = ['2017', '2018', '2019', '2020', '2021', '2022'];
		console.log(years);
		let transformedData = [];

		// Create a map to hold temporary data
		let tempData = new Map();

		inputData.data.forEach((item) => {
			if (years.includes(item.Jahr.toString()) && item.Bundesland !== 'Deutschland') {
				if (!tempData.has(item.Bundesland)) {
					tempData.set(item.Bundesland, {});
				}
				tempData.get(item.Bundesland)[item.Jahr] = item.Prozent; // Update to use 'Prozent'
			}
		});

		// Convert map to the required format
		tempData.forEach((value, key) => {
			let dataEntry = { state: key, ...value };
			transformedData.push(dataEntry);
		});

		return transformedData;
	}

	let formattedData = transformData(realData);
	let data = formattedData;

	const customColors = [
		'#1f77b4',
		'#ff7f0e',
		'#2ca02c',
		'#d62728',
		'#9467bd',
		'#8c564b',
		'#e377c2',
		'#7f7f7f',
		'#bcbd22',
		'#17becf',
		'#393b79',
		'#637939',
		'#8c6d31',
		'#843c39',
		'#7b4173',
		'#bd9e39',
		'#ad494a',
		'#d6616b'
	];

	let currentYear = '2017';

	let selectedYearValue = currentYear;

	selectedYear.subscribe((value) => {
		selectedYearValue = value.toString();
		if (typeof window !== 'undefined') {
			updateChart(selectedYearValue);
		}
	});

	onMount(() => {
		ready = true;
		if (typeof window !== 'undefined') {
			createDoughnutChart(data, currentYear);
		}

		window.addEventListener('resize', handleResize);
		return () => {
			window.removeEventListener('resize', handleResize);
			//unsubscribe();
		};
	});

	$: {
		if (stateName !== 'Deutschland') {
			highlightedState = stateName;
		} else {
			highlightedState = '';
		}
		if (typeof window !== 'undefined') {
			createDoughnutChart(data, currentYear, highlightedState);
		}
	}

	function handleResize() {
		if (typeof window !== 'undefined') {
			createDoughnutChart(data, currentYear);
		}
	}

	// Update chart when year changes
	function updateChart(year) {
		currentYear = year;
		if (typeof window !== 'undefined') {
			createDoughnutChart(data, currentYear, highlightedState);
		}
	}

	function createDoughnutChart(data, year, highlightState) {
		if (isActive === false) {
			return;
		}

		if (!ready) return;

		// Clear existing SVG if any
		d3.select('#chart').selectAll('*').remove();

		// Mapping states to their abbreviations
		const abbreviations = {
			'Baden-Württemberg': 'BW',
			Bayern: 'BY',
			Berlin: 'BE',
			Brandenburg: 'BB',
			Bremen: 'HB',
			Hamburg: 'HH',
			Hessen: 'HE',
			Niedersachsen: 'NI',
			'Mecklenburg-Vorpommern': 'MV',
			'Nordrhein-Westfalen': 'NW',
			'Rheinland-Pfalz': 'RP',
			Saarland: 'SL',
			Sachsen: 'SN',
			'Sachsen-Anhalt': 'ST',
			'Schleswig-Holstein': 'SH',
			Thüringen: 'TH'
		};

		var parentDiv = document.getElementById('doughnutchart-parent');
		var width = 0.8 * parentDiv.clientWidth;
		var height = 0.8 * parentDiv.clientHeight;

		var radius = Math.min(width, height) / 2;
		const color = d3.scaleOrdinal(customColors);

		const svg = d3
			.select('#chart')
			.append('svg')
			.attr('width', width)
			.attr('height', height)
			.append('g')
			.attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')');

		const arc = d3
			.arc()
			.outerRadius((d) => (d.data.state === highlightState ? radius : radius - 10))
			.innerRadius((d) => (d.data.state === highlightState ? radius - 70 - 10 : radius - 70));

		const pie = d3
			.pie()
			.sort(null)
			.value((d) => d[year]);

		const g = svg.selectAll('.arc').data(pie(data)).enter().append('g').attr('class', 'arc');

		// Append paths for the pie pieces
		g.append('path')
			.attr('d', arc)
			.style('fill', (d) => color(d.data.state));

		// Label positioning
		const label = d3
			.arc()
			.outerRadius(radius - 40)
			.innerRadius(radius - 40);

		// Append text labels
		g.append('text')
			.attr('transform', (d) => 'translate(' + label.centroid(d) + ')')
			.attr('dy', '0.35em')
			.text((d) => abbreviations[d.data.state])
			.style('text-anchor', 'middle')
			.style('fill', '#fff');

		// Append title with dynamic content
		const titleText = highlightState
			? `${[highlightState]}:\n${data.find((d) => d.state === highlightState)[year]}%`
			: 'Unemployment Rate\nin %';

		svg
			.append('text')
			.attr('text-anchor', 'middle')
			.attr('x', 0)
			.attr('y', '0')
			.style('font-size', '18px')
			.style('fill', '#333')
			.selectAll('tspan')
			.data(titleText.split('\n'))
			.enter()
			.append('tspan')
			.attr('x', 0) // center horizontally
			.attr('dy', (d, i) => `${i * 1.2}em`) // adjust line spacing
			.text((d) => d);

		// Tooltip setup
		const tooltip = d3.select('#chart').append('div').attr('class', 'tooltip').style('opacity', 0);

		// Tooltip mouseover event
		g.on('mouseover', (event, d) => {
			tooltip.transition().duration(200).style('opacity', 0.9);
			tooltip
				.html(d.data.state + ': ' + d.data[year])
				.style('left', event.pageX + 'px')
				.style('top', event.pageY - 28 + 'px');
		}).on('mouseout', () => {
			tooltip.transition().duration(500).style('opacity', 0);
		});
	}
</script>

<div>
	<div id="chart" />
	<div class="year-container">
		<span class="selected-year">{currentYear}</span>
	</div>
</div>

<style>
	.year-container {
		margin-top: 10px;
		text-align: center;
	}

	.selected-year {
		color: var(--colorscheme-blue);
		font-size: 20px; /* You can adjust the font size as needed */
		margin: 4px 2px;
	}

	:global(.tooltip) {
		position: absolute;
		text-align: center;
		width: 60px;
		height: 28px;
		padding: 2px;
		font: 12px sans-serif;
		background: lightsteelblue;
		border: 0px;
		border-radius: 8px;
		pointer-events: none;
	}
</style>

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
		let transformedData = [];

		// Create a map to hold temporary data
		let tempData = new Map();

		inputData.data.forEach((item) => {
			if (years.includes(item.Jahr.toString()) && item.Bundesland !== 'Deutschland') {
				if (!tempData.has(item.Bundesland)) {
					tempData.set(item.Bundesland, {});
				}
				tempData.get(item.Bundesland)[item.Jahr] = item.Income;
			}
		});

		// Convert map to the required format
		tempData.forEach((value, key) => {
			let dataEntry = { state: key, ...value };
			transformedData.push(dataEntry);
		});

		return transformedData;
	}

	// Example usage with your real data
	let formattedData = transformData(realData);
	let data = formattedData;

	let currentYear = '2017';

	let selectedYearValue = currentYear;

	selectedYear.subscribe((value) => {
		selectedYearValue = value.toString();
		if (typeof window !== 'undefined') {
			updateChart(selectedYearValue);
		}
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
			createDoughnutChart(data, currentYear, highlightedState);
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

		const outlineColor = 'var(--colorscheme-blue)';
		const backgroundColor = 'var(--colorscheme-sand)';
		const highlightedOutlineColor = 'var(--colorscheme-sand)';
		const highlightedBackgroundColor = 'var(--colorscheme-blue)';

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
			.attr('fill', (d) =>
				d.data.state === highlightedState ? highlightedBackgroundColor : backgroundColor
			)
			.attr('stroke', (d) =>
				d.data.state === highlightedState ? highlightedOutlineColor : outlineColor
			)
			.attr('stroke-width', 2); // Adjust the outline thickness if needed

		// Label positioning
		const label = d3
			.arc()
			.outerRadius(radius - 40)
			.innerRadius(radius - 40);

		// Append text labels
		g.append('text')
			.attr('transform', (d) => `translate(${arc.centroid(d)})`)
			.attr('dy', '0.35em')
			.attr('text-anchor', 'middle')
			.style('fill', (d) =>
				d.data.state === highlightedState ? highlightedOutlineColor : outlineColor
			)
			.text((d) => abbreviations[d.data.state]);

		// Append title with dynamic content
		const titleText = highlightState
			? `${[highlightState]}:\n${data.find((d) => d.state === highlightState)[year]}€`
			: 'Income Distribution\n in €';

		svg
			.append('text')
			.attr('text-anchor', 'middle')
			.attr('x', 0)
			.attr('y', '0')
			.style('font-size', '16px')
			.style('fill', '#333')
			.selectAll('tspan')
			.data(titleText.split('\n'))
			.enter()
			.append('tspan')
			.attr('x', 0) // center horizontally
			.attr('dy', (d, i) => `${i * 1.2}em`) // adjust line spacing
			.text((d) => d);

		// ... (existing code)

		// Tooltip setup
		const tooltip = d3.select('#chart').append('div').attr('class', 'hover-tooltip').style('opacity', 0);

		// Tooltip mouseover event
		g.on('mouseover', (event, d) => {
			tooltip.transition().duration(200).style('opacity', 1.0);
			tooltip
			.html(`${d.data.state}: ${d.data[year]}€`)
			.style('left', event.pageX + 'px')
			.style('top', event.pageY + 'px')
		}).on('mousemove', function (event) {
			moveTooltip(event);
		}).on('mouseout', () => {
			tooltip.transition().duration(500).style('opacity', 0);
		});

		function moveTooltip(event) {
			const ttw = tooltip.node().offsetWidth;
			const tth = tooltip.node().offsetHeight;
			const x = event.pageX - ttw / 2;
			const y = event.pageY - tth - 10;
			
			tooltip.style('left', x + 'px').style('top', y + 'px');
		}


	}

	onMount(() => {
		ready = true;
		if (typeof window !== 'undefined') {
			createDoughnutChart(data, currentYear, highlightedState);
		}

		window.addEventListener('resize', handleResize);
		return () => {
			window.removeEventListener('resize', handleResize);
			//unsubscribe();
		};
	});
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
</style>

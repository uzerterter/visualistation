<script>
	import { onMount } from 'svelte';
	import * as d3 from 'd3';
	import { selectedYear } from '$lib/components/timeline.svelte';

	let data = [
		{
			state: 'Baden-Württemberg',
			'2017': 31431,
			'2018': 39279,
			'2019': 40375,
			'2020': 57802,
			'2021': 63430,
			'2022': 61782
		},
		{
			state: 'Bavaria',
			'2017': 38836,
			'2018': 58435,
			'2019': 34230,
			'2020': 46719,
			'2021': 55451,
			'2022': 55182
		},
		{
			state: 'Berlin',
			'2017': 60083,
			'2018': 50184,
			'2019': 54188,
			'2020': 40540,
			'2021': 67686,
			'2022': 35499
		},
		{
			state: 'Brandenburg',
			'2017': 69662,
			'2018': 63881,
			'2019': 42008,
			'2020': 31479,
			'2021': 61243,
			'2022': 32701
		},
		{
			state: 'Bremen',
			'2017': 51697,
			'2018': 53009,
			'2019': 57508,
			'2020': 55495,
			'2021': 41006,
			'2022': 30866
		},
		{
			state: 'Hamburg',
			'2017': 42492,
			'2018': 61734,
			'2019': 65771,
			'2020': 67175,
			'2021': 43376,
			'2022': 57151
		},
		{
			state: 'Hesse',
			'2017': 54841,
			'2018': 67881,
			'2019': 30921,
			'2020': 42062,
			'2021': 69196,
			'2022': 51697
		},
		{
			state: 'Lower Saxony',
			'2017': 41299,
			'2018': 56289,
			'2019': 43474,
			'2020': 57971,
			'2021': 35186,
			'2022': 51482
		},
		{
			state: 'Mecklenburg-Vorpommern',
			'2017': 39639,
			'2018': 48599,
			'2019': 36831,
			'2020': 34919,
			'2021': 36895,
			'2022': 42146
		},
		{
			state: 'North Rhine-Westphalia',
			'2017': 54481,
			'2018': 41524,
			'2019': 53080,
			'2020': 58526,
			'2021': 61650,
			'2022': 62499
		},
		{
			state: 'Rhineland-Palatinate',
			'2017': 32485,
			'2018': 44456,
			'2019': 56074,
			'2020': 55011,
			'2021': 64323,
			'2022': 31972
		},
		{
			state: 'Saarland',
			'2017': 65913,
			'2018': 46078,
			'2019': 53122,
			'2020': 62048,
			'2021': 48756,
			'2022': 46104
		},
		{
			state: 'Saxony',
			'2017': 63459,
			'2018': 34279,
			'2019': 56271,
			'2020': 66107,
			'2021': 62390,
			'2022': 48941
		},
		{
			state: 'Saxony-Anhalt',
			'2017': 31145,
			'2018': 45053,
			'2019': 58964,
			'2020': 32618,
			'2021': 47012,
			'2022': 36742
		},
		{
			state: 'Schleswig-Holstein',
			'2017': 41637,
			'2018': 53425,
			'2019': 35742,
			'2020': 53762,
			'2021': 58654,
			'2022': 53371
		},
		{
			state: 'Thuringia',
			'2017': 47311,
			'2018': 57978,
			'2019': 60698,
			'2020': 52436,
			'2021': 47607,
			'2022': 66957
		}
	];

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
		if (typeof window !== 'undefined') {
			createDoughnutChart(data, currentYear);
		}

		window.addEventListener('resize', handleResize);
		return () => {
			window.removeEventListener('resize', handleResize);
			//unsubscribe();
		};
	});

	function handleResize() {
		if (typeof window !== 'undefined') {
			createDoughnutChart(data, currentYear);
		}
	}

	function updateChart(year) {
		currentYear = year;
		if (typeof window !== 'undefined') {
			createDoughnutChart(data, currentYear);
		}
	}

	function createDoughnutChart(data, year) {
		// Clear existing SVG if any
		d3.select('#chart').selectAll('*').remove();

		// Mapping states to their abbreviations
		const abbreviations = {
			'Baden-Württemberg': 'BW',
			Bavaria: 'BY',
			Berlin: 'BE',
			Brandenburg: 'BB',
			Bremen: 'HB',
			Hamburg: 'HH',
			Hesse: 'HE',
			'Lower Saxony': 'NI',
			'Mecklenburg-Vorpommern': 'MV',
			'North Rhine-Westphalia': 'NW',
			'Rhineland-Palatinate': 'RP',
			Saarland: 'SL',
			Saxony: 'SN',
			'Saxony-Anhalt': 'ST',
			'Schleswig-Holstein': 'SH',
			Thuringia: 'TH'
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
			.outerRadius(radius - 10)
			.innerRadius(radius - 70);

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
	<div class="button-container">
		{#each ['2017', '2018', '2019', '2020', '2021', '2022'] as year}
			<button
				on:click={() => updateChart(year)}
				class:current={year === currentYear}
				disabled={year === currentYear}
			>
				{year}
			</button>
		{/each}
	</div>
</div>

<style>
	.button-container {
		margin-top: 10px;
		text-align: center;
	}
	button {
		background-color: var(--colorscheme-blue); /* Green */
		border: 2px solid var(--colorscheme-blue);
		color: white;
		padding: 10px 10px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 12px;
		margin: 4px 2px;
		transition-duration: 0.4s;
		cursor: pointer;
		border-radius: 15px;
	}

	button:hover {
		background-color: var(--colorscheme-orange);
		opacity: 0.6;
		color: white;
		border: 2px solid var(--colorscheme-orange);
	}

	.current {
		background-color: var(--colorscheme-orange); /* Darker grey */
		color: white;
		border: 2px solid var(--colorscheme-orange);
		cursor: default;
		pointer-events: none; /* Prevents click events on the current button */
	}

	button:disabled {
		/* opacity: 0.6; */
		cursor: not-allowed;
	}

	.tooltip {
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

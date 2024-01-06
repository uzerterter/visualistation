<!-- MyDoughnutChart.svelte -->

<script>
	import { onMount, afterUpdate } from 'svelte';
	import * as d3 from 'd3';
	import { selectedYear } from '$lib/components/timeline.svelte';

	export let stateName = 'Deutschland';
	export let data = [];
	export let dropdownItems = [
		{ id: 3, label: 'Anzahl Unternehmen', orig: 'Anzahl_Unternehmen' },
		{ id: 4, label: 'Beförderte Personen in Mio', orig: 'Befoerderte_Personen_in_Mio' },
		{ id: 5, label: 'Personenkilometer in Mio', orig: 'Personenkilometer_in_Mio' }
	];
	export let selectedDropdownItem = dropdownItems[1];

	let selectedArt = 'Liniennahverkehr mit Eisenbahnen';
	let currentYear = 2017;
	let highlightedState = '';

	function handleToggle(art) {
		selectedArt = art;
		updateChart();
	}

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

	selectedYear.subscribe((value) => {
		currentYear = value;
		if (typeof window !== 'undefined') {
			updateChart();
		}
	});

	function updateChart() {
		const filteredData = data.data.filter(
			(entry) =>
				entry.Jahr === currentYear &&
				entry.Art === selectedArt &&
				entry.Bundesland !== 'Deutschland'
		);

		const chartData = filteredData.map((entry) => ({
			value: entry[selectedDropdownItem.orig],
			state: entry.Bundesland
		}));

		d3.select('#chart-container svg').remove();

		const width = 400;
		const height = 300;
		const radius = Math.min(width, height) / 2;

		const color = d3.scaleOrdinal(d3.schemeCategory10);

		const svg = d3
			.select('#chart-container')
			.append('svg')
			.attr('width', width)
			.attr('height', height)
			.append('g')
			.attr('transform', `translate(${width / 2},${height / 2})`);

		const arc = d3
			.arc()
			.outerRadius((d) => (d.data.state === highlightedState ? radius : radius - 10))
			.innerRadius((d) => (d.data.state === highlightedState ? radius - 70 - 10 : radius - 70));

		const pie = d3.pie().sort(null).value((d) => d.value);

		const arcs = svg
			.selectAll('.arc')
			.data(pie(chartData))
			.enter()
			.append('g')
			.attr('class', 'arc');

		arcs
			.append('path')
			.attr('d', arc)
			.attr('fill', (d, i) => color(i))
			.on('mouseover', function (event, d) {
				const hoveredValue = d.data.value;
				displayValueInCenter(hoveredValue);
			})
			.on('mouseout', function () {
				d3.select('#chart-container svg text.center-text').remove();
			});

		arcs
			.append('text')
			.attr('transform', (d) => `translate(${arc.centroid(d)})`)
			.attr('dy', '0.35em')
			.attr('text-anchor', 'middle')
			.text((d) => abbreviations[d.data.state]);
	}

	function displayValueInCenter(value) {
		d3.select('#chart-container svg text.center-text').remove();

		const svg = d3.select('#chart-container svg');
		const width = +svg.attr('width');
		const height = +svg.attr('height');

		svg
			.append('text')
			.attr('class', 'center-text')
			.attr('text-anchor', 'middle')
			.attr('dy', '0.35em')
			.attr('x', width / 2)
			.attr('y', height / 2)
			.text(value)
			.attr('fill', 'black');
	}

	onMount(() => {
		updateChart();
	});

	afterUpdate(() => {
		if (stateName !== 'Deutschland') {
			highlightedState = stateName;
		} else {
			highlightedState = '';
		}
		if (typeof window !== 'undefined') {
			updateChart();
		}
	});
</script>

<div id="chart-container" />

<!-- Radio buttons -->
<div>
	<input type="radio" id="train" name="transport" bind:group={selectedArt} value="Liniennahverkehr mit Eisenbahnen" on:change={() => handleToggle('Liniennahverkehr mit Eisenbahnen')} />
	<label for="train">Train</label>

	<input type="radio" id="tram" name="transport" bind:group={selectedArt} value="Liniennahverkehr mit Straßenbahnen" on:change={() => handleToggle('Liniennahverkehr mit Straßenbahnen')} />
	<label for="tram">Tram</label>

	<input type="radio" id="bus" name="transport" bind:group={selectedArt} value="Liniennahverkehr mit Omnibussen" on:change={() => handleToggle('Liniennahverkehr mit Omnibussen')} />
	<label for="bus">Bus</label>
</div>

<style>
	/* Add your styles here if needed */
	input[type='radio'] {
		cursor: pointer;
	}
</style>
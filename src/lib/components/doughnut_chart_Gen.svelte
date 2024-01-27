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
	let ready = false;

	export let isActive = false;

	function handleToggle(art) {
		if (!isActive) {
			return;
		}
		selectedArt = art;
		updateChart();
	}

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
			if (!isActive) {
				return;
			}
			updateChart();
		}
	});

	function updateChart() {
		if (!isActive) {
			return;
		}

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

		var parentDiv = document.getElementById('doughnutchart-RightViz-parent');
		var width = 0.8 * parentDiv.offsetWidth;
		var height = 0.8 * parentDiv.offsetHeight;
		var radius = Math.min(width, height) / 2;

		if (width <= 0 || height <= 0) {
			// Avoid creating the chart if width or height is zero
			return;
		}

		const color = d3.scaleOrdinal(customColors);

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

		const pie = d3
			.pie()
			.sort(null)
			.value((d) => d.value);

		const arcs = svg
			.selectAll('.arc')
			.data(pie(chartData))
			.enter()
			.append('g')
			.attr('class', 'arc');

		arcs
			.append('path')
			.attr('d', arc)
			.attr('fill', (d, i) => color(i));

		arcs
			.append('text')
			.attr('transform', (d) => `translate(${arc.centroid(d)})`)
			.attr('dy', '0.35em')
			.attr('text-anchor', 'middle')
			.text((d) => abbreviations[d.data.state]);

		const titleText = highlightedState
			? `${highlightedState}:\n${chartData.find((d) => d.state === highlightedState).value}`
			: `${selectedDropdownItem.label}`;

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
	}

	function handleResize() {
		if (typeof window !== 'undefined') {
			if (!isActive) {
				return;
			}
			updateChart();
		}
	}

	onMount(() => {
		ready = true;
		if (!isActive || !ready) {
			return;
		}
		updateChart();
		window.addEventListener('resize', handleResize);
		return () => {
			window.removeEventListener('resize', handleResize);
			//unsubscribe();
		};
	});

	afterUpdate(() => {
		if (stateName !== 'Deutschland') {
			highlightedState = stateName;
		} else {
			highlightedState = '';
		}
		if (typeof window !== 'undefined') {
			if (!isActive) {
				return;
			}
			updateChart();
		}
	});
</script>

<div id="chart-container" />

<!-- Radio buttons -->
<div>
	<input
		type="radio"
		id="train"
		name="transport"
		bind:group={selectedArt}
		value="Liniennahverkehr mit Eisenbahnen"
		on:change={() => handleToggle('Liniennahverkehr mit Eisenbahnen')}
	/>
	<label for="train">Train</label>

	<input
		type="radio"
		id="tram"
		name="transport"
		bind:group={selectedArt}
		value="Liniennahverkehr mit Straßenbahnen"
		on:change={() => handleToggle('Liniennahverkehr mit Straßenbahnen')}
	/>
	<label for="tram">Tram</label>

	<input
		type="radio"
		id="bus"
		name="transport"
		bind:group={selectedArt}
		value="Liniennahverkehr mit Omnibussen"
		on:change={() => handleToggle('Liniennahverkehr mit Omnibussen')}
	/>
	<label for="bus">Bus</label>

	<input
		type="radio"
		id="total"
		name="total"
		bind:group={selectedArt}
		value="Liniennahverkehr insgesamt"
		on:change={() => handleToggle('Liniennahverkehr insgesamt')}
	/>
	<label for="total">Total</label>
</div>

<style>
	/* Add your styles here if needed */
	input[type='radio'] {
		cursor: pointer;
	}
</style>

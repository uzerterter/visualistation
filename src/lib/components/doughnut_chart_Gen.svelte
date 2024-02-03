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

	let selectedArt = 'Liniennahverkehr mit Straßenbahnen';
	let currentYear = 2017;
	let highlightedState = '';
	let ready = false;
	let chartDataItem = '';

	export let isActive = false;

	function handleToggle(art) {
		if (!isActive) {
			return;
		}
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

	const radioLabels = {
		'Liniennahverkehr mit Straßenbahnen': 'Tram',
		'Liniennahverkehr mit Omnibussen': 'Bus',
		'Liniennahverkehr mit Eisenbahnen': 'Train',
		'Liniennahverkehr insgesamt': 'Total'
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
		const outlineColor = 'var(--colorscheme-blue)';
		const backgroundColor = 'var(--colorscheme-sand)';
		const highlightedOutlineColor = 'var(--colorscheme-sand)';
		const highlightedBackgroundColor = 'var(--colorscheme-blue)';

		if (!isActive) {
			return;
		}

		if (!ready) return;

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

		const parentDiv = document.getElementById('doughnutchart-RightViz-parent');
		const width = 0.8 * parentDiv.offsetWidth;
		const height = 0.8 * parentDiv.offsetHeight;
		const radius = Math.min(width, height) / 2;

		if (width <= 0 || height <= 0) {
			// Avoid creating the chart if width or height is zero
			return;
		}

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
			.attr('fill', (d) =>
				d.data.state === highlightedState ? highlightedBackgroundColor : backgroundColor
			)
			.attr('stroke', (d) =>
				d.data.state === highlightedState ? highlightedOutlineColor : outlineColor
			)
			.attr('stroke-width', 2); // Adjust the outline thickness if needed

		arcs
			.append('text')
			.attr('transform', (d) => `translate(${arc.centroid(d)})`)
			.attr('dy', '0.35em')
			.attr('text-anchor', 'middle')
			.style('fill', (d) =>
				d.data.state === highlightedState ? highlightedOutlineColor : outlineColor
			)
			.text((d) => abbreviations[d.data.state]);

		chartDataItem = chartData.find((d) => d.state === highlightedState);
		// console.log(chartDataItem);
		// console.log(radioLabels[selectedArt]);

		const titleText = highlightedState && chartDataItem !== undefined
			? `${highlightedState}:\n${chartDataItem.value}`
			: `${highlightedState ? highlightedState + ':\nNo ' + radioLabels[selectedArt]  +  ' Data' : selectedDropdownItem.label !== 'No Data' ? selectedDropdownItem.label : 'No Data'}`;

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

		const tooltip = d3.select('#chart-container').append('div').attr('class', 'hover-tooltip').style('opacity', 0);


		arcs
			.on('mouseover', (event, d) => {
				tooltip.transition().duration(200).style('opacity', 0.9);
				tooltip
					.html(`${d.data.state}: ${d.data.value}`)
					.style('left', event.pageX + 'px')
					.style('top', event.pageY + 'px')
					// .style('height', '30px')
					// .style('line-height', '30px');
			})
			.on('mouseout', () => {
				tooltip.transition().duration(500).style('opacity', 0);
			});
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
		id="Tram"
		name="transport"
		bind:group={selectedArt}
		value="Liniennahverkehr mit Straßenbahnen"
		on:change={() => handleToggle('Liniennahverkehr mit Straßenbahnen')}
		style="accent-color: var(--colorscheme-red)"
	/>
	<label
		for="Tram">Tram</label>

	<input
		type="radio"
		id="Bus"
		name="transport"
		bind:group={selectedArt}
		value="Liniennahverkehr mit Omnibussen"
		on:change={() => handleToggle('Liniennahverkehr mit Omnibussen')}
		style="accent-color: var(--colorscheme-orange)"
	/>
	<label 
		for="Bus">Bus</label>

	<input
		type="radio"
		id="Train"
		name="transport"
		bind:group={selectedArt}
		value="Liniennahverkehr mit Eisenbahnen"
		on:change={() => handleToggle('Liniennahverkehr mit Eisenbahnen')}
		style="accent-color: var(--colorscheme-yellow)"
	/>
	<label 
		for="Train">Train</label>

	<input
		type="radio"
		id="Total"
		name="total"
		bind:group={selectedArt}
		value="Liniennahverkehr insgesamt"
		on:change={() => handleToggle('Liniennahverkehr insgesamt')}
		style="accent-color: var(--colorscheme-blue)"
	/>
	<label 
		for="Total">Total</label>
</div>

<style>
	/* Add your styles here if needed */
	input[type='radio'] {
		cursor: pointer;
	}

</style>





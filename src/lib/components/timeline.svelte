<script>
	// Import Svelte's writable store
	import { writable } from 'svelte/store';

	// Define a store for the selected year
	const selectedYear = writable(2017);

	// Define the range of years for the timeline
	const startYear = 2017;
	const endYear = 2022;

	// Function to update the selected year
	function updateYear(event) {
		selectedYear.set(+event.target.value);
	}
</script>

<div class="timeline-container">
	<input
		type="range"
		min={startYear}
		max={endYear}
		step="1"
		bind:value={$selectedYear}
		on:input={updateYear}
	/>
	<div class="timeline-labels">
		{#each Array(endYear - startYear + 1) as _, i}
			<span>{startYear + i}</span>
		{/each}
	</div>
</div>

<style>
	.timeline-container {
		position: relative;
		margin: 20px;
		padding: 10px;
	}

	input[type='range'] {
		-webkit-appearance: none; /* Override default CSS styles */
		appearance: none;
		width: 100%;
		margin: 0;
		background: transparent; /* Required for WebKit browsers */
	}

	/* Webkit-based browsers like Chrome, Safari, and newer versions of Opera */
	input[type='range']::-webkit-slider-runnable-track {
		background: #003049;
		height: 5px;
	}

	input[type='range']::-webkit-slider-thumb {
		-webkit-appearance: none;
		border: none;
		height: 20px;
		width: 20px;
		border-radius: 50%;
		background: goldenrod;
		margin-top: -7.5px; /* Adjust the thumb position */
	}

	/* Mozilla Firefox */
	input[type='range']::-moz-range-track {
		background: #003049;
		height: 5px;
	}

	input[type='range']::-moz-range-thumb {
		height: 20px;
		width: 20px;
		border-radius: 50%;
		background: goldenrod;
		border: none;
	}

	/* Microsoft Edge */
	input[type='range']::-ms-track {
		background: transparent; /* Must be transparent for proper thumb positioning */
		border-color: transparent;
		color: transparent;
	}

	input[type='range']::-ms-fill-lower {
		background: #003049;
	}

	input[type='range']::-ms-fill-upper {
		background: #003049;
	}

	input[type='range']::-ms-thumb {
		height: 20px;
		width: 20px;
		border-radius: 50%;
		background: goldenrod;
		border: none;
	}

	.timeline-labels {
		display: flex;
		justify-content: space-between;
		padding: 0 10px;
		color: var(--colorscheme-blue);
	}
</style>

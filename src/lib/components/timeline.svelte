<script>
	import { writable, derived } from 'svelte/store';

	// Initialize the selected year
	const selectedYear = writable(2017);

	// Define the start and end years for the timeline
	const startYear = 2017;
	const endYear = 2022;

	// IsThumbPressed
	const isThumbPressed = writable(false); // Track if thumb is being pressed

	// Autoplay state
	let autoplayInterval;
	const isAutoplayActive = writable(false);

	// Calculate the percentage of the slider to fill based on the selected year
	const fillPercentage = derived(
		selectedYear,
		($selectedYear) => (($selectedYear - startYear) / (endYear - startYear)) * 100
	);

	// Function to update the selected year
	function updateYear(event) {
		selectedYear.set(+event.target.value);
	}

	// Functions to update thumb press state
	function onThumbPress() {
		isThumbPressed.set(true);
	}

	function onThumbRelease() {
		isThumbPressed.set(false);
	}

	// Toggle autoplay
	function toggleAutoplay() {
		const autoplayActive = $isAutoplayActive;

		if (autoplayActive) {
			clearInterval(autoplayInterval);
		} else {
			autoplayInterval = setInterval(() => {
				// Increment the selected year by 1
				const newYear = $selectedYear + 1;
				// If the new year is within the allowed range, update the selected year
				if (newYear <= endYear) {
					selectedYear.set(newYear);
				} else {
					// Stop autoplay if the end of the range is reached
					clearInterval(autoplayInterval);
					isAutoplayActive.set(false);
				}
			}, 1000); // Adjust the interval as needed
		}

		isAutoplayActive.set(!autoplayActive);
	}
</script>

<div class="timeline-container">
	<button on:click={toggleAutoplay} id="autoplay-button">
		{#if $isAutoplayActive}
			Pause
			<!-- Todo: Add Icons -->
		{:else}
			Play
		{/if}
	</button>
	<input
		type="range"
		min={startYear}
		max={endYear}
		step="1"
		bind:value={$selectedYear}
		on:input={updateYear}
		on:mousedown={onThumbPress}
		on:mouseup={onThumbRelease}
		on:touchstart={onThumbPress}
		on:touchend={onThumbRelease}
		class:pressed={$isThumbPressed}
		style={`background: linear-gradient(to right, #003049 0%, #003049 ${$fillPercentage}%, #ddd ${$fillPercentage}%, #ddd 100%); border-radius: 10px;`}
	/>
	<div class="timeline-labels">
		{#each Array(endYear - startYear + 1) as _, i}
			<span class="year-label">{startYear + i}</span>
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
		height: 6px;
		-webkit-appearance: none;
		appearance: none;
		width: 100%;
		margin: 0;
		background: transparent;
		border-radius: 10px; /* Rounded edges */
	}

	input[type='range']::-webkit-slider-thumb {
		-webkit-appearance: none;
		border: none;
		height: 20px;
		width: 20px;
		border-radius: 50%;
		background: var(--colorscheme-orange);
		margin-top: -7.5px;
	}

	input[type='range']::-webkit-slider-thumb {
		box-shadow: rgba(247, 127, 0, 0.16) 0px 0px 0px 7px;
	}

	input[type='range']::-moz-range-thumb {
		height: 20px;
		width: 20px;
		border-radius: 50%;
		background: var(--colorscheme-orange);
		border: none;
	}

	input[type='range']::-moz-range-thumb:hover {
		box-shadow: rgba(247, 127, 0, 0.16) 0px 0px 0px 7px;
	}

	input[type='range']::-ms-thumb {
		height: 20px;
		width: 20px;
		border-radius: 50%;
		background: var(--colorscheme-orange);
		border: none;
	}

	input[type='range']::-ms-thumb:hover {
		box-shadow: rgba(247, 127, 0, 0.16) 0px 0px 0px 7px;
	}

	.timeline-labels {
		display: flex;
		justify-content: space-between;
		padding: 10px;
		color: var(--colorscheme-blue);
	}

	.year-label {
		flex: 0 0 auto;
		text-align: center;
		width: 20%; /* Set width to distribute the labels evenly */
		position: relative;
		left: -10%; /* Adjust position to center the text under the thumb */
	}

	input[type='range'].pressed::-webkit-slider-thumb {
		/* Define your styles for the pressed thumb here */
		box-shadow: rgba(247, 127, 0, 0.16) 0px 0px 0px 12px;
	}

	input[type='range'].pressed::-moz-range-thumb {
		/* Define your styles for the pressed thumb here */
		box-shadow: rgba(247, 127, 0, 0.16) 0px 0px 0px 12px;
	}

	input[type='range'].pressed::-ms-thumb {
		/* Define your styles for the pressed thumb here */
		box-shadow: rgba(247, 127, 0, 0.16) 0px 0px 0px 12px;
	}

	button {
		transform: translateY(-50%);
		background-color: var(--colorscheme-orange);
		color: var(--colorscheme-blue);
		padding: 8px 12px;
		border: none;
		border-radius: 20px;
		cursor: pointer;
		font-size: 14px;
		margin-right: 10px; /* Adjust the margin as needed */
	}

</style>

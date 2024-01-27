<script context="module">
	import { writable, derived } from 'svelte/store';

	// Initialize the selected year
	export const selectedYear = writable(2017);

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
</script>
<script>


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
			<svg
				xmlns="http://www.w3.org/2000/svg"
				viewBox="0 0 24 24"
				class="icon"
			>
				<path
					fill-rule="evenodd"
					d="M6.75 5.25a.75.75 0 01.75-.75H9a.75.75 0 01.75.75v13.5a.75.75 0 01-.75.75H7.5a.75.75 0 01-.75-.75V5.25zm7.5 0A.75.75 0 0115 4.5h1.5a.75.75 0 01.75.75v13.5a.75.75 0 01-.75.75H15a.75.75 0 01-.75-.75V5.25z"
					clip-rule="evenodd"
				/>
			</svg>
		{:else}
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="icon">
				<path
					fill-rule="evenodd"
					d="M4.5 5.653c0-1.426 1.529-2.33 2.779-1.643l11.54 6.348c1.295.712 1.295 2.573 0 3.285L7.28 19.991c-1.25.687-2.779-.217-2.779-1.643V5.653z"
					clip-rule="evenodd"
				/>
			</svg>
		{/if}
	</button>
	<div class="timeline-wrapper">
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
</div>

<style>
	.timeline-container {
		display: flex;
		align-items: center; /* Center items vertically */
		margin: 20px;
		padding: 170px;
	}

	.timeline-wrapper {
		flex-grow: 1; /* Grow to take remaining space */
		margin-left: 20px; /* Adjust spacing between button and timeline */
		position: relative;
	}

	.icon {
		height: 1.5vh;
		width: 1.5vw;
		fill: var(--colorscheme-orange);
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
		color: black;
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
		transform: translateY(-20%);
		padding: 8px 12px;
		border: none;
		border-radius: 20px;
		cursor: pointer;
		margin-right: 15px;
	}

	input {
		cursor: pointer;
	}
</style>

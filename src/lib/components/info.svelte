<script>
	import Tooltip from './tooltip.svelte';

	export let title = '';
</script>

<div class="tooltip-wrapper">
	<Tooltip
		title={title}>
		<button class="info">
			i
		</button>
	</Tooltip>
</div>

<style>

    button {
        text-align: center;
        background-color: white;
        border: 2px;
        border-color: var(--colorscheme-blue);
        border-radius: 50%;
        color: var(--colorscheme-blue);
        font-weight: 800;
        font-size: 3vh;
        width: 4vh;
        height: 4vh;
    }

    button:hover {
        border: white;
        color: white;
        background-color: var(--colorscheme-blue);
    }

    .tooltip-wrapper {
        padding: 1%;
        margin: 1%;
    }

</style>
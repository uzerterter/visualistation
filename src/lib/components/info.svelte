<script>
	import Tooltip from './tooltip.svelte';
	export let title = '';
</script>

<Tooltip
	title={title}>
	<div class="info">
		i
	</div>
</Tooltip>

<style>

    .info {
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

    .info:hover {
        border: white;
        color: white;
        background-color: var(--colorscheme-blue);
    }

</style>
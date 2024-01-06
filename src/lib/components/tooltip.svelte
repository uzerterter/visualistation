<script>
	export let title = '';
	let isHovered = false;
	let x;
	let y;

	function mouseOver(event) {
		isHovered = true;
		x = event.pageX + 15;
		y = event.pageY + 15;
	}

	function mouseMove(event) {
		x = event.pageX + 15;
		y = event.pageY + 15;
	}

	function mouseLeave() {
		isHovered = false;
	}

</script>


<div
	role="tooltip"
	on:mouseover={mouseOver}
	on:mouseleave={mouseLeave}
	on:mousemove={mouseMove}>
	<slot />
</div>

{#if isHovered}
	<div style="top: {y}px; left:{x}px;" class="tooltip">
		{title}
	</div>
{/if}


<style>

    .tooltip {
        border: 1px solid var(--colorscheme-blue);
        box-shadow: 1px 1px 1px #444444;
				background: white;
        border-radius: 4px;
        padding: 4px;
				position: fixed;
        inline-size: fit-content;
        font-size: small;
        text-align: left;
        white-space: pre-line;
    }

</style>
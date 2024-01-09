<script>
	export let title = '';
	let isHovered = false;
	let x;
	let y;
	let showOnLeft = false;

	function mouseOver(event) {
		isHovered = true;
		x = event.pageX + 15;
		y = event.pageY + 15;

		const viewportWidth = window.innerWidth || document.documentElement.clientWidth;
		showOnLeft = viewportWidth - event.clientX <= 300;
	}

	function mouseMove(event) {
		x = event.pageX + 15;
		y = event.pageY + 15;
	}

	function mouseLeave() {
		isHovered = false;
	}

</script>

<div class="tooltip-container">
<div
	role="tooltip"
	on:mouseover={mouseOver}
	on:mouseleave={mouseLeave}
	on:mousemove={mouseMove}>
	<slot />
</div>
</div>

{#if isHovered}
	{#if showOnLeft}
		<div style="top: {y}px; right: {window.innerWidth - x}px;" class="tooltip">
			<div class="tooltip-content">
				{title}
			</div>
		</div>
	{:else}
		<div style="top: {y}px; left: {x}px;" class="tooltip">
			<div class="tooltip-content">
				{title}
			</div>
		</div>
	{/if}
{/if}


<style>

    .tooltip-container {
        position: relative;
        z-index: 9999;
    }

    .tooltip {
        border: 1px solid var(--colorscheme-blue);
        box-shadow: 5px 5px 5px #444444;
        background: white;
        border-radius: 4px;
        padding: 8px;
        position: fixed;
        max-width: 200px;
        z-index: 9999;
        word-wrap: break-word;
        width: fit-content;
        block-size: fit-content;
    }

    .tooltip-content {
        font-family: Poppins-Black, sans-serif;
        font-size: 14px;
        color: #333;
        line-height: 1.4;
        max-width: 100%;
				text-align: left;
    }

</style>

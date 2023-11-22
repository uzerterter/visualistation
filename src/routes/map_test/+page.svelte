<script>
    import '../../styles/global.css';
    let group = "group08"
    import TestComponent from '$lib/test_component.svelte';
    import BarChart from '$lib/components/bar_chart.svelte';
    import Data from '$lib/data/final_genesis_traffic.json';	
    import Map from '$lib/components/map.svelte';
</script>



<div id="map-parent">
    <Map/>
</div>





<style>

    #map-parent {
        width: 100vw;
        height: 100vh;
    }

</style>
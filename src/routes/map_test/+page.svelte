<script>
    import '../../styles/global.css';
    let group = "group08"	
    import Map from '$lib/components/map_test.svelte';
    import BarChart from '$lib/components/bar_chart.svelte';
    import Data from '$lib/data/final_genesis_traffic.json';
    let mapContainer;
</script>

<div class="map-background" bind:this={mapContainer} id="map-parent">
    <Map bind:container={mapContainer}/>
</div>

<div id="main">
    <!-- Three equally sized empty divs that take a third of the width of #main each -->

    <div class="visualizations">
        <div class="left-viz viz-border"> 
        
        </div>

        <div class="center-viz"> 
        
        </div>

        <div class="right-viz viz-border"> 
            <div class="bar-chart-container"  id="barchart-parent">
                <BarChart data={Data}/>
            </div>
        </div>
    </div>
    <div class="timeline">
        <div class="timeline-viz viz-border"> 

        </div>
    </div>
</div>





<style>

#main {
        text-align: center;
    }

    .visualizations {
        /* position: relative; */
        width: 100%;
        height: 70vh;
        display: flex;
        /* justify-content: center;
        align-items: center; */
    }

    .left-viz, .center-viz, .right-viz {
        width: 33.33%; 
        height: 50vh;
        z-index: 2;
        
    }

    .left-viz, .right-viz {
        
        float: left;
        background-color: white;
        display: flex;
        flex-direction: column;
        margin-top: 15vh;
        flex-direction: column;
        align-items: center;
        justify-content: center;  
    }

    .left-viz {
        margin-right: 4%;
        
    }

    .right-viz {
        margin-left: 4%;
        
    }

    .center-viz {
        z-index: 0;
        pointer-events: none;
        
    }

    .timeline {
        width: 100%;
        height: 22vh;
        display: flex;
        justify-content: center; /* Center the child horizontally */
        /* align-items: center; Center the child vertically */
    }

    .timeline-viz {
        width: 50%;
        height: 50%;
        background-color: white;
        margin-top: 2vh;
    }

    .viz-border {
        border: solid 3px;
        border-radius: 15px; /* Add rounded borders */
        border-color: var(--colorscheme-blue);
    }

    .bar-chart-container {
        width: 100%;
        height: 90%;
        display: flex;
        flex-direction: column;
        align-items: center; /* Center the chart horizontally within the container */
        justify-content: center; /* Center the chart vertically within the container */
    }

    .map-background {
        position: fixed;
        z-index: 1;
        top: 0;
        left: 0;
        width: 100%;
        margin-top: 8vh;
        height: 70vh; /* Match the height of the visualizations */
        z-index: 0; /* Layered behind the side containers */
    }

</style>
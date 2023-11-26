<script>
    import '../styles/global.css';
    let group = "group08"
    import TestComponent from '$lib/test_component.svelte';
    import BarChart from '$lib/components/bar_chart.svelte';
    import _data from '$lib/data/final_genesis_traffic.json';
    let data = {..._data, data: _data.data.filter(v=>v.Bundesland==='Deutschland')}	
    import Timeline from '../lib/components/timeline.svelte';
    import Map from '$lib/components/map.svelte';
    let mapContainer;
</script>



<div id="main">
    <!-- Three equally sized empty divs that take a third of the width of #main each -->
    <div class="visualizations">
        <div class="left-viz viz-border"> 
        
        </div>
    
        <div class="center-viz viz-border"> 
            <div class="map-container" bind:this={mapContainer} id="map-parent">
                <Map bind:container={mapContainer}/>
            </div>
        </div>
    
        <div class="right-viz viz-border"> 
            <div class="bar-chart-container"  id="barchart-parent">
                <BarChart data={data}/>
            </div>
        </div>
    </div>
    <div class="timeline">
        <div class="timeline-viz"> 
            <Timeline/>
        </div>
    </div>
</div>





<style>
    #main {
        text-align: center;
    }

    .visualizations {
        width: 100%;
        height: 70vh;
        display: flex;
        /* justify-content: center;
        align-items: center; */
    }

    .left-viz, .center-viz, .right-viz {
        width: 33.33%; 
        height: 50vh;
        float: left;
        background-color: white;
        display: flex;
        flex-direction: column;
        margin-top: 15vh;
        flex-direction: column;
        align-items: center; /* Center the chart horizontally within the container */
        justify-content: center; /* Center the chart vertically within the container */
    }

    .left-viz {
        margin-right: 4%;
    }
    .center-viz {
        margin-left: 4%;
        margin-right: 4%;
    }

    .right-viz {
        margin-left: 4%;
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

    .map-container {
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center; /* Center the chart horizontally within the container */
        justify-content: center; /* Center the chart vertically within the container */
    }

    

</style>
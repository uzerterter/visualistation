<script>
    import '../styles/global.css';
    let group = "group08"
    import TestComponent from '$lib/test_component.svelte';
    import BarChart from '$lib/components/bar_chart.svelte';
    import originalData from '$lib/data/final_genesis_traffic.json';
    import incomeData from '$lib/data/income.json';	
    import unimploymentData from '$lib/data/unemployment_rate.json';
    import Timeline from '../lib/components/timeline.svelte';
    import Map from '$lib/components/map.svelte';
    import DoughnutChart from '$lib/components/doughnut_chart.svelte';
    import ColorLegend from '$lib/components/color_legend.svelte'; // Import the ColorLegend component

	import { base } from '$app/paths';

    let mapContainer;

    import { selectedYear } from '$lib/components/timeline.svelte';
    let selectedYearValue;
    
    selectedYear.subscribe(value => {
        selectedYearValue = value;
    });

    let showToprowContent = false;
    let stateName = "Deutschland"; // Default to Germany
    let stateFlag = "Deutschland";
    function handleStateClick(event) {
        stateName = event.detail.stateName || "Deutschland";
        if (stateName == "Deutschland") {
            setTimeout(() => {
                showToprowContent = false;
                stateFlag = stateName;
            }, 1000); // Delay for 1000 milliseconds (1 second)
        } else {
            showToprowContent = true;
            stateFlag = stateName;
        }
        console.log(showToprowContent);
    }

    let selectedData = incomeData; // Default data

    const dataOptions = [
        { label: 'Income Data', value: incomeData },
        { label: 'Unemployment Rate', value: unimploymentData },
    ];

    function handleDataChange() {
        // Handle the change of selected data
        // You can perform additional actions here if needed
    }
</script>



<div class="map-background" bind:this={mapContainer} id="map-parent">
    <Map bind:container={mapContainer} on:stateClicked={handleStateClick} />
    <ColorLegend />
</div>


<div id="main">
    <!-- Three equally sized empty divs that take a third of the width of #main each -->

    <div class="visualizations">
        <div class="left-viz viz-border" id="doughnutchart-parent">
            <select bind:value={selectedData} on:change={handleDataChange}>
                {#each dataOptions as option (option.value)}
                    <option value={option.value}>{option.label}</option>
                {/each}
            </select>
            <DoughnutChart realData={selectedData} stateName={stateName}/>
        </div>        

        <div class="center-viz">
            <div id="center-viz-toprow" class:fade-in={stateName !== "Deutschland"}>
                {#if showToprowContent}
                    <div id="flag">
                        <img src={base}/{`${stateFlag}-flag.png`} alt={`flag of ${stateFlag}`} id="flag" />
                    </div>
                    <div id="statename">
                        <h2>{stateFlag}</h2>
                    </div>
                {/if}
            </div>
        
        </div>

        <div class="right-viz viz-border"> 
            <div class="bar-chart-container"  id="barchart-parent">
                <BarChart data={originalData} stateName={stateName} selectedYearValue={selectedYearValue} year={selectedYearValue}/>
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
        /* position: relative; */
        width: 100%;
        height: 70vh;
        display: flex;
        /* justify-content: center;
        align-items: center; */
    }

    .left-viz, .center-viz, .right-viz {
        width: 33.33%; 
        height: 60vh;
        z-index: 2; 
    }

    .left-viz, .right-viz {
        float: left;
        background-color: white;
        display: flex;
        flex-direction: column;
        margin-top: 10vh;
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
        float: left;
        display: flex;
        flex-direction: column;
        margin-top: 3vh;
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
        background-color: transparent;
        width: 95%;
        height: 95%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .map-background {
        position: fixed;
        z-index: 1;
        top: 0;
        left: 0;
        width: 100%;
        margin-top: 8vh;
        height: 65vh;
        z-index: 0;
    }

    #center-viz-toprow {
        display: flex;
        align-items: center;
        flex-direction: column;
        height: 15%;
        width: 100%;
        opacity: 0;
        transition: opacity 1s ease-in-out;
    }

    #center-viz-toprow.fade-in {
        opacity: 1;
        transition: opacity 1s ease-in-out;
    }

    #statename {
        width: 100%;
        height: 30%;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    #flag {
        height: 66%;
        width: 22%;
        /* margin-left: auto;
        margin-right: auto; */
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        bottom: 0;
    }

    #flag img {
        width: 90%;
        height: 90%;
        max-width: 100%;
        max-height: 100%;
        border: solid 3px black;
        border-radius: 15px;
    }
</style>

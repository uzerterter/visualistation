<script>
	import '../../styles/global.css';

	let group = 'group08';
	import BarChart from '$lib/components/bar_chart.svelte';
	import originalData from '$lib/data/final_genesis_traffic.json';
	import incomeData from '$lib/data/income.json';
	import unimploymentData from '$lib/data/unemployment_rate.json';
	import Timeline from '$lib/components/timeline.svelte';
	import Map from '$lib/components/map.svelte';
	import DoughnutChartIN from '$lib/components/doughnut_chart_In.svelte';
	import DoughnutChartUR from '$lib/components/doughnut_chart_UR.svelte';
	import DoughnutChartGE from '$lib/components/doughnut_chart_Gen.svelte';
	import ColorLegend from '$lib/components/color_legend.svelte';
	import BarChartEconomicIN from '$lib/components/bar_chart_economic_IN.svelte';
	import BarChartEconomicUR from '$lib/components/bar_chart_economic_UR.svelte';
	import BarChart_2 from '$lib/components/bar_chart_2.svelte';
	import Info from '$lib/components/info.svelte';

	import { base } from '$app/paths';

	let mapContainer;

	import { selectedYear } from '$lib/components/timeline.svelte';

	let selectedYearValue;

	selectedYear.subscribe(value => {
		selectedYearValue = value;
	});

	let showToprowContent = false;
	let stateName = 'Deutschland'; // Default to Germany
	let stateFlag = 'Deutschland';

	function handleStateClick(event) {
		stateName = event.detail.stateName || 'Deutschland';
		if (stateName === 'Deutschland') {
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

	let radioButtonsLeft = [
		{ color: 'var(--colorscheme-blue)' }
	];

	let radioButtonsRight = [
		{ id: 6, label: 'Tram', orig: 'Liniennahverkehr mit Straßenbahnen', color: 'var(--colorscheme-red)' },
		{ id: 7, label: 'Bus', orig: 'Liniennahverkehr mit Omnibussen', color: 'var(--colorscheme-orange)' },
		{ id: 8, label: 'Train', orig: 'Liniennahverkehr mit Eisenbahnen', color: 'var(--colorscheme-yellow)' },
		{ id: 9, label: 'Total', orig: 'Liniennahverkehr insgesamt', color: 'var(--colorscheme-total)' },
	];

	let radioButtonsLeftIN = [
		{color: 'var(--colorscheme-left1)' },
	];

	let radioButtonsLeftUR = [
		{color: 'var(--colorscheme-left2)' },
	];

	//pass the dropdown data centrally to the right vizualisation, exrtacted from barchart
	let dropdownItemsRightViz = [
		{ id: 3, label: 'Number of public\n transport operators', orig: 'Anzahl_Unternehmen' },
		{ id: 4, label: 'Passengers transported\n in mil.', orig: 'Befoerderte_Personen_in_Mio' },
		{ id: 5, label: 'Kilometers travelled\n per Person in mil.', orig: 'Personenkilometer_in_Mio' }
	];
	let selectedDropdownItemRightViz = dropdownItemsRightViz[1];

	let selectedData = incomeData; // Default data
	let selectedTabLeftViz = 'doughnut'; // Default tab for left vizualisation
	let selectedTabRightViz = 'bar'; // Default tab for right vizualisation

	const dataOptions = [
		{ label: 'Average annual gross income', value: incomeData, orig: 'Income' },
		{ label: 'Unemployment rate', value: unimploymentData, orig: 'Prozent' }
	];

	function handleDataChange() {
		console.log(selectedData);
	}

	// Function to handle tab change
	let isActiveLeftViz = true;

	function handleTabChangeLeftViz(tab) {
		selectedTabLeftViz = tab;
		isActiveLeftViz = tab === 'doughnut';
	}

	let isActiveRightViz = true;

	function handleTabChangeRightViz(tab) {
		selectedTabRightViz = tab;
		isActiveRightViz = tab === 'doughnut';
	}

	function pickTooltip(stateName, direction) {
		let selectedState = stateName.toString();
		const stateSensitiveTooltipRight = (
			'This Chart displays public transportation data, e.g. number of transported passengers or passenger kilometers.\n' +
			'You can choose between Train, Tram, Bus or Total - which is the sum of all transportation possibilities.\n' +
			'\n' +
			'Distribution: Distribution of transportation data in ' + selectedState + '.\n' +
			'\n' +
			'Development: Shows development of transportation data for ' + selectedState + ' from 2017 - 2022.\n' +
			'\n' +
			'Comparison: Direct comparison of transportation data between federal states and ' + selectedState + '.'
		);
		const stateSensitiveTooltipLeft = (
			'This Chart displays economic data for ' + stateName + '.\n' +
			'\n' +
			'Distribution: Overview over economical factors of ' + selectedState + ', the highlighted state below.\n' +
			'\n' +
			'Development: Shows development of e.g. the unemployment rate in ' + selectedState + ' over the years 2017-2022.\n' +
			'\n' +
			'Comparison: Direct comparison of economical factors between federal states and ' + selectedState + '.'
		);
		if (direction === 'left') {
			return stateSensitiveTooltipLeft;
		} else return stateSensitiveTooltipRight;
	}
</script>


<div class="map-background" bind:this={mapContainer} id="map-parent">
	<Map bind:container={mapContainer} on:stateClicked={handleStateClick} />
	<ColorLegend />
</div>


<div id="main">
	<!-- Three equally sized empty divs that take a third of the width of #main each -->

	<div class="visualizations">
		<div class="left-viz viz-border">
			<div id="left-viz-toprow">
				<div id="left-viz-dropdown">
					<select bind:value={selectedData} on:change={handleDataChange}>
						{#each dataOptions as option (option.value)}
							<option value={option.value}>{option.label}</option>
						{/each}
					</select>
				</div>
				<div class="toprowCurrentStateNameContainer">
					<h4>{stateName}</h4>
				</div>
				<div class="toprowTooltipContainer">
					<Info
						title={pickTooltip(stateName, "left")} />
				</div>
			</div>
			<div class="tab-buttons">
				<ul>
					<li>
						<button on:click={() => handleTabChangeLeftViz('doughnut')}
										class:selected={selectedTabLeftViz === 'doughnut'}>Distribution
						</button>
					</li>
					<li>
						<button on:click={() => handleTabChangeLeftViz('bar')} class:selected={selectedTabLeftViz === 'bar'}>
							Development
						</button>
					</li>
					<li>
						<button on:click={() => handleTabChangeLeftViz('bar2')} class:selected={selectedTabLeftViz === 'bar2'}>
							Comparison
						</button>
					</li>
				</ul>
			</div>
			<!-- Content based on selected tab -->
			{#if selectedTabLeftViz === 'doughnut'}
				{#if selectedData === incomeData}
					<div id="doughnutchart-parent">
						<DoughnutChartIN realData={incomeData} stateName={stateName} isActive={isActiveLeftViz} />
					</div>
					<div class="bar-chart-container" id="barchart-leftViz-parent" style="display: none;">
						<BarChartEconomicIN data={incomeData} stateName={stateName} selectedYearValue={selectedYearValue}
																year={selectedYearValue} />
					</div>
					<div class="bar-chart-container" id="barchart2-leftViz-parent" style="display: none;">
						<BarChart_2 data={incomeData} stateName={stateName} year={selectedYearValue}
											dropdownItems={null} radioButtons={radioButtonsLeftIN} parentId="barchart2-leftViz-parent"
											selectedDropdownItem={dataOptions.filter(o=>o.value===selectedData)[0]}></BarChart_2>
					</div>
				{:else if selectedData === unimploymentData}
					<div id="doughnutchart-parent">
						<DoughnutChartUR realData={unimploymentData} stateName={stateName} isActive={isActiveLeftViz} />
					</div>
					<div class="bar-chart-container" id="barchart-leftViz-parent" style="display: none;">
						<BarChartEconomicUR data={unimploymentData} stateName={stateName} selectedYearValue={selectedYearValue}
																year={selectedYearValue} />
					</div>
					<div class="bar-chart-container" id="barchart2-leftViz-parent" style="display: none;">
						<BarChart_2 data={unimploymentData} stateName={stateName} year={selectedYearValue}
											dropdownItems={null} radioButtons={radioButtonsLeftUR} parentId="barchart2-leftViz-parent"
											selectedDropdownItem={dataOptions.filter(o=>o.value===selectedData)[0]}></BarChart_2>
					</div>
				{/if}
			{/if}
			{#if selectedTabLeftViz === 'bar'}
				<!-- Bitte verzeiht mir für diesen Workaround :_) -->
				{#if selectedData === incomeData}
					<div id="doughnutchart-parent" style="display: none;">
						<DoughnutChartIN realData={incomeData} stateName={stateName} isActive={isActiveLeftViz} />
					</div>
					<div class="bar-chart-container" id="barchart-leftViz-parent">
						<BarChartEconomicIN data={incomeData} stateName={stateName} selectedYearValue={selectedYearValue}
																year={selectedYearValue} />
					</div>
					<div class="bar-chart-container" id="barchart2-leftViz-parent" style="display: none;">
						<BarChart_2 data={incomeData} stateName={stateName} year={selectedYearValue}
											dropdownItems={null} radioButtons={radioButtonsLeftIN} parentId="barchart2-leftViz-parent"
											selectedDropdownItem={dataOptions.filter(o=>o.value===selectedData)[0]}></BarChart_2>
					</div>
				{:else if selectedData === unimploymentData}
					<div id="doughnutchart-parent" style="display: none;">
						<DoughnutChartUR realData={unimploymentData} stateName={stateName} isActive={isActiveLeftViz} />
					</div>
					<div class="bar-chart-container" id="barchart-leftViz-parent">
						<BarChartEconomicUR data={unimploymentData} stateName={stateName} selectedYearValue={selectedYearValue}
																year={selectedYearValue} />
					</div>
					<div class="bar-chart-container" id="barchart2-leftViz-parent" style="display: none;">
						<BarChart_2 data={unimploymentData} stateName={stateName} year={selectedYearValue}
											dropdownItems={null} radioButtons={radioButtonsLeftUR} parentId="barchart2-leftViz-parent"
											selectedDropdownItem={dataOptions.filter(o=>o.value===selectedData)[0]}></BarChart_2>
					</div>
				{/if}
			{/if}
			{#if selectedTabLeftViz === 'bar2'}
				<!-- Bitte verzeiht mir für diesen Workaround :_) -->
				{#if selectedData === incomeData}
					<div id="doughnutchart-parent" style="display: none;">
						<DoughnutChartIN realData={incomeData} stateName={stateName} isActive={isActiveLeftViz} />
					</div>
					<div class="bar-chart-container" id="barchart-leftViz-parent" style="display: none;">
						<BarChartEconomicIN data={incomeData} stateName={stateName} selectedYearValue={selectedYearValue}
																year={selectedYearValue} />
					</div>
					<div class="bar-chart-container" id="barchart2-leftViz-parent">
						<BarChart_2 data={incomeData} stateName={stateName} year={selectedYearValue}
											dropdownItems={null} radioButtons={radioButtonsLeftIN} parentId="barchart2-leftViz-parent"
											selectedDropdownItem={dataOptions.filter(o=>o.value===selectedData)[0]}></BarChart_2>
					</div>
				{:else if selectedData === unimploymentData}
					<div id="doughnutchart-parent" style="display: none;">
						<DoughnutChartUR realData={unimploymentData} stateName={stateName} isActive={isActiveLeftViz} />
					</div>
					<div class="bar-chart-container" id="barchart-leftViz-parent" style="display: none;">
						<BarChartEconomicUR data={unimploymentData} stateName={stateName} selectedYearValue={selectedYearValue}
																year={selectedYearValue} />
					</div>
					<div class="bar-chart-container" id="barchart2-leftViz-parent">
						<BarChart_2 data={unimploymentData} stateName={stateName} year={selectedYearValue}
											dropdownItems={null} radioButtons={radioButtonsLeftUR} parentId="barchart2-leftViz-parent"
											selectedDropdownItem={dataOptions.filter(o=>o.value===selectedData)[0]}></BarChart_2>
					</div>
				{/if}
			{/if}
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
			<div id="right-viz-toprow">
				<div id="right-viz-dropdown">
					<select bind:value={selectedDropdownItemRightViz}>
						{#each dropdownItemsRightViz as d}
							<option value={d}>
								{d.label}
							</option>
						{/each}
					</select>
				</div>
				<div class="toprowCurrentStateNameContainer">
					<h4>{stateName}</h4>
				</div>
				<div class="toprowTooltipContainer">
					<Info
						title={pickTooltip(stateName, "right")}/>
				</div>
			</div>
			<div class="tab-buttons">
				<ul>
					<li>
						<button on:click={() => handleTabChangeRightViz('doughnut')}
										class:selected={selectedTabRightViz === 'doughnut'}>Distribution
						</button>
					</li>
					<li>
						<button on:click={() => handleTabChangeRightViz('bar')} class:selected={selectedTabRightViz === 'bar'}>
							Development
						</button>
					</li>
					<li>
						<button on:click={() => handleTabChangeRightViz('bar2')} class:selected={selectedTabRightViz === 'bar2'}>
							Comparison
						</button>
					</li>
				</ul>
			</div>
			{#if selectedTabRightViz === 'doughnut'}
				<div id="doughnutchart-RightViz-parent">
					<DoughnutChartGE data={originalData} stateName={stateName} selectedDropdownItem={selectedDropdownItemRightViz}
													 isActive={isActiveRightViz} />
				</div>
				<div class="bar-chart-container" id="barchart-parent" style="display: none;">
					<BarChart data={originalData} stateName={stateName} selectedYearValue={selectedYearValue}
										year={selectedYearValue}
										dropdownItems={dropdownItemsRightViz} selectedDropdownItem={selectedDropdownItemRightViz} />
				</div>
				<!-- BAR CHART 2 -->
				<div id="barchart2-parent" style="display: none;">
					<BarChart_2 data={originalData} stateName={stateName} year={selectedYearValue}
											dropdownItems={dropdownItemsRightViz} radioButtons={radioButtonsRight} parentId="barchart2-parent"
											selectedDropdownItem={selectedDropdownItemRightViz}></BarChart_2>
				</div>
			{/if}
			{#if selectedTabRightViz === 'bar'}
				<!-- Bitte verzeiht mir für diesen Workaround :_) -->
				<div id="doughnutchart-RightViz-parent" style="display: none;">
					<DoughnutChartGE data={originalData} stateName={stateName} isActive={isActiveRightViz} />
				</div>
				<div class="bar-chart-container" id="barchart-parent">
					<BarChart data={originalData} stateName={stateName} selectedYearValue={selectedYearValue}
										year={selectedYearValue}
										dropdownItems={dropdownItemsRightViz} selectedDropdownItem={selectedDropdownItemRightViz} />
				</div>
				<!-- BAR CHART 2 -->
				<div id="barchart2-parent" style="display: none;">
					<BarChart_2 data={originalData} stateName={stateName} year={selectedYearValue}
											dropdownItems={dropdownItemsRightViz} radioButtons={radioButtonsRight} parentId="barchart2-parent"
											selectedDropdownItem={selectedDropdownItemRightViz}></BarChart_2>
				</div>
			{/if}
			{#if selectedTabRightViz === 'bar2'}
				<!-- Bitte verzeiht mir für diesen Workaround :_) -->
				<div id="doughnutchart-RightViz-parent" style="display: none;">
					<DoughnutChartGE data={originalData} stateName={stateName} isActive={isActiveRightViz} />
				</div>
				<div class="bar-chart-container" id="barchart-parent" style="display: none;">
					<BarChart data={originalData} stateName={stateName} selectedYearValue={selectedYearValue}
										year={selectedYearValue}
										dropdownItems={dropdownItemsRightViz} selectedDropdownItem={selectedDropdownItemRightViz} />
				</div>
				<!-- BAR CHART 2 -->
				<div class="bar-chart-container" id="barchart2-parent">
					<BarChart_2 data={originalData} stateName={stateName} year={selectedYearValue}
											dropdownItems={dropdownItemsRightViz} radioButtons={radioButtonsRight} parentId="barchart2-parent"
											selectedDropdownItem={selectedDropdownItemRightViz}></BarChart_2>
				</div>
			{/if}
		</div>
	</div>
	<div class="timeline">
		<div class="timeline-viz">
			<Timeline />
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

    .left-viz, .right-viz {
        width: 35%;
        height: 60vh;
        z-index: 2;
    }

    .center-viz {
        width: 30%;
        height: 60vh;
        z-index: 2;
    }

    .left-viz, .right-viz {
        float: left;
        display: flex;
        flex-direction: column;
        margin-top: 10vh;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    .left-viz {
        margin-right: 10%;

    }

    .right-viz {
        margin-left: 10%;
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
        border: solid 1px;
        border-radius: 15px; /* Add rounded borders */
        border-color: var(--colorscheme-blue);
    }

    .bar-chart-container, #barchart-leftViz-parent, #barchart2-leftViz-parent, #barchart-parent, #barchart2-parent {
        background-color: transparent;
        width: 95%;
        height: 95%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    #doughnutchart-parent, #doughnutchart-RightViz-parent {
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

    #right-viz-toprow, #left-viz-toprow {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        height: 10%;
        width: 100%;
        padding: 1%;
        margin: 1%;
    }

    #right-viz-dropdown, #left-viz-dropdown {
        width: 90%;
        margin: 2%;
        padding: 1%;
        display: flex;
    }

    #right-viz-dropdown select, #left-viz-dropdown select {
        width: 100%;
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 5px;
        box-sizing: border-box;
        background-color: rgb(236, 236, 236);
        font-size: 0.8vw;
        float: left;
        cursor: pointer;
    }

    .toprowCurrentStateNameContainer {
        width: 34%;
    }

    .toprowCurrentStateNameContainer h4 {
        text-align: center;
        width: auto;
    }

    .toprowTooltipContainer {
        width: 20%;
    }

    .tab-buttons {
        display: flex;
        flex-direction: row;
        width: 100%;
        margin-bottom: 5px;
    }

    .tab-buttons ul {
        list-style: none;
        padding-left: 0;
        margin: 1em 0 0;
        display: flex;
        border-bottom: 1px solid var(--colorscheme-blue);
        width: 100%;
    }

    .tab-buttons ul li {
        flex: 1;
        width: 100%;
        display: flex
    }


    .tab-buttons button {
        appearance: none;
        background: none;
        border: none;
        border-radius: 0;
        font: inherit;
        color: inherit;
        display: flex;
        align-items: center;
        vertical-align: middle;
        padding: .75em .5em;
        width: 80%;
        margin: auto;
        margin-bottom: 0px;
        justify-content: center;
        cursor: pointer;
    }

    /* Style for the selected tab */
    .tab-buttons button.selected {
        border-bottom: 3px solid var(--colorscheme-blue);
        cursor: default;
    }

    .tab-buttons button.selected:hover {
        border-bottom: 3px solid var(--colorscheme-blue);
        cursor: default;
    }

    .tab-buttons button:hover {
        border-bottom: 2px solid var(--colorscheme-blue);
    }


</style>

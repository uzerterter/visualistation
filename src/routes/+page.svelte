<script>
    import '../styles/global.css';
    let group = "group08"
    import TestComponent from '$lib/test_component.svelte';
</script>




<div id="main">
    <!-- Three equally sized empty divs that take a third of the width of #main each -->
    <div class="visualizations">
        <div class="left-viz"> 
        
        </div>
    
        <div class="center-viz"> 
            
        </div>
    
        <div class="right-viz"> 
            
        </div>
    </div>
    <div class="timeline">
        <div class="timeline-viz"> 

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
        background-color: var(--colorscheme-sand);
        display: flex;
        flex-direction: column;
        margin-top: 15vh;
        border-radius: 15px; /* Add rounded borders */
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
        background-color: var(--colorscheme-sand);
        border-radius: 15px; /* Add rounded borders */
        margin-top: 2vh;
    }

</style>
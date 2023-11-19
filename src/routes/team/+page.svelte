<script>
    import '../../styles/global.css';
    let group = "group08"
    let pagename = "about page"
    import TestComponent from '$lib/test_component.svelte';
</script>

<h1>This is {group}'s {pagename}</h1>
<h3>Take me <a href="/">home</a></h3>
<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
<TestComponent testCompName="test component on the about page" />

<style>

    
</style>
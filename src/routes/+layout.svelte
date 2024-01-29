<script>
    import '../styles/global.css';
    import { page } from '$app/stores';    
    import { base } from '$app/paths';
</script>

<header>
    <nav class="navbar">
        <div class="navbar-content">
            <div class="logo">
                <img src="Logo.png" alt="logo">
                <p>visuali-station</p>
            </div>
            <ul class="navbar-links">
                {#each [
                    { href: '/', label: 'about' },
                    { href: '/visualization', label: 'visualization' },
                    // Add more links as needed
                  ] as { href, label }}
                    <a href={base}{href} class:active={$page.route.id === href}>{label}</a>
                  {/each}
            </ul>
        </div>
    </nav>
</header>


<main>
    <slot></slot>
</main>


<footer>

</footer>



<style>
    /* header {
        font-size: x-large;
    } */

    .navbar {
        background-color: var(--colorscheme-sand-light);
        width: 100%;
        height: 7vh;
        color: var(--colorscheme-blue);
        border-bottom: 1px solid var(--colorscheme-blue);
    }

    .navbar-content {
        padding-left: 10%;      
        padding-right: 10%; 
        display: flex;
        height: 100%;
    }

    .navbar-content div {
        display: flex;
        /* align-items: center;
        float: left; */
    }

    .navbar-content p {
        margin-left: 10px;
        align-self: center;
        font-weight: 600;
        letter-spacing: 0.2rem;
    }

    .navbar-content img {
        height: 50px;
        align-self: center;
        padding: auto;
    }

    .logo {
        height: 100%;
    }

    .navbar-links {
        margin-left: auto; /* Push the links to the right */
        display: flex;
        align-items: center;
        letter-spacing: 0.2rem;
        font-weight: 600;
    }

    .navbar-links a {
        color: var(--colorscheme-blue);
        margin-left: 25px; /* Add spacing between links */
        text-decoration: none;
    }

    /* Style for links on hover */
    .navbar-links a:hover,
    .navbar-links a.active {
        text-decoration-line: underline;
        text-decoration-thickness: 3px; 
        text-decoration-color: var(--colorscheme-orange);
    }
</style>
<script>
    import '../styles/global.css';
    import { page } from '$app/stores';

</script>

<header>
    <nav class="navbar">
        <div class="navbar-content">
            <div class="logo">
                <img src="Logo.png" alt="logo">
                <p>VISUALIZE IT</p>
            </div>
            <ul class="navbar-links">
                {#each [
                    { href: '{base}/', label: 'Home' },
                    { href: '{base}/team', label: 'Team' },
                    // Add more links as needed
                  ] as { href, label }}
                    <a href={href} class:active={$page.route.id === href}>{label}</a>
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
    header {
        font-size: x-large;
    }

    .navbar {
        background-color: var(--colorscheme-blue);
        width: 100%;
        height: 8vh;
        color: white;
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
        height: 60px;
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
    }

    .navbar-links a {
        color: white;
        margin-left: 25px; /* Add spacing between links */
        text-decoration: none;
    }

    /* Style for links on hover */
    .navbar-links a:hover,
    .navbar-links a.active {
        text-decoration: underline;
    }
</style>
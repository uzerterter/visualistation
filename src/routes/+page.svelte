<script>
	import '../styles/global.css';
	import { base } from '$app/paths';
</script>

<div class="background-image" />
<div class="about-container">
	<div class="text-container">
		<h1>VISUALI<br />STATION</h1>
		<p>
			As part of the information visualization course, we analyzed Germany's public transport data
			from 2017 to 2022 alongside economic indicators. Our interactive exploratory approach empowers
			users to dynamically investigate potential correlations. On the left, detailed economic data
			is presented, while the right side displays public transport data. Each side features three
			distinct visualizations for data distribution, development, and relative comparison. The
			central interactive map provides supplementary demographic information and enables users to select a
			federal state for data presentation. Furthermore, users can seamlessly navigate through
			different years using the bottom timeline.
		</p>
		<a href={`${base}/visualization`} target="_blank">
			<button class="custom-button">GO TO VISUALIZATION</button>
		</a>
	</div>
	<div>
		<img src={`${base}/{Logo.png`}} alt="logo" />
	</div>
</div>

<style>
	.background-image {
		position: fixed;
		top: 0;
		left: 0;
		width: 60vw;
		height: 100vh;
		background-image: url($lib/img/tubemap.png);
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		background-color: var(--colorscheme-sand-light);
		opacity: 0.1;
		z-index: -1; /* Set z-index to ensure it's behind other content */
	}

	.about-container {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding-left: 20vh; /* Adjust padding as needed */
		padding-right: 5vh; /* Adjust padding as needed */
		padding-top: 5vh;
		position: relative;
	}

	.text-container {
		max-width: 750px;
	}

	h1 {
		font-size: 6em;
		margin-bottom: 10px;
		letter-spacing: 20px;
		font-weight: 900;
		color: rgb(22, 41, 55);
	}

	p {
		font-size: 1.1em;
		color: #242424;
		letter-spacing: 3px;
		line-height: 25px;
	}

	.custom-button {
		padding: 15px 30px;
		font-size: 1.2em;
		background-color: rgb(232, 111, 70);
		color: #fff;
		border: none;
		border-radius: 10px;
		cursor: pointer;
		margin-top: 15px;
	}

	img {
		max-width: 100%;
		height: auto;
		border-radius: 8px;
	}
</style>

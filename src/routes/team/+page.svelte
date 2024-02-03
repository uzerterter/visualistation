<script>
	import '../../styles/global.css';
	import { base } from '$app/paths';

	let teamMembers = [
		{
			name: "Lara",
			description: "Media Informatics | Product Owner",
			image: "Lara.png"
		},
		{
			name: "Linus",
			description: "Computer Science | Design & Concept",
			image: "Linus.png"
		},
        {
			name: "Andrian",
			description: "Computer Science | Lead Developer",
			image: "andrian.png"
		},
        {
			name: "Ludwig",
			description: "Human Computer Interaction | Scrum Master",
			image: "Ludwig.png"
		},
        {
			name: "Rebecca",
			description: "Human Computer Interaction | Data Scientist",
			image: "rebecca.png"
		},
		// Add more team members as needed
	];
</script>

<div class="background-image" />
<div class="team-container">
	<div class="team-members">
		{#each teamMembers as member (member.name)}
			<div class="team-member">
				<img src={base}/{`${member.image}`} alt={member.name} />
				<div class="member-info">
					<h2>{member.name}</h2>
					<p>{member.description}</p>
				</div>
			</div>
		{/each}
	</div>
	<div class="headline-container">
		<h1>MEET THE TEAM</h1>
	</div>
</div>

<style>
	.background-image {
		position: fixed;
		top: 0;
		right: 0;
		width: 60vw;
		height: 100vh;
		background-image: url($lib/img/tubemapflipped.png);
		background-size: cover;
		background-position: center;
		background-repeat: no-repeat;
		background-color: var(--colorscheme-sand-light);
		opacity: 0.1;
		z-index: -1;
	}

	.team-container {
		display: flex;
		align-items: center;
		justify-content: space-between;
		padding-left: 20vh; /* Adjust padding as needed */
		padding-right: 20vh; /* Adjust padding as needed */
		padding-top: 5vh;
		position: relative;
	}

	.team-members {
		width: 50%; /* 50% of the container width */
		padding-top: 3%;
	}

	.headline-container {
		width: 50%; /* 50% of the container width */
		text-align: right; /* Align text to the right */
	}

	h1 {
		font-size: 6em;
		margin-bottom: 10px;
		letter-spacing: 20px;
		font-weight: 900;
		color: rgb(22, 41, 55);
	}

	.team-member {
		display: flex;
		align-items: center;
		margin-bottom: 20px;
	}

	.team-member img {
		max-width: 125px;
		height: auto;
		border-radius: 50%;
		margin-right: 20px;
	}

	.member-info {
		max-width: 400px;
	}

	h2 {
		font-size: 2em;
		margin-bottom: 5px;
		color: rgb(22, 41, 55);
	}

	p {
		font-size: 1.1em;
		color: #242424;
		letter-spacing: 1px;
		line-height: 20px;
	}
</style>

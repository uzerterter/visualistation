<script>

	let Arbeitnehmereinkommen = [
		{
			name: 'Bayern',
			link: 'https://de.statista.com/statistik/daten/studie/253200/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-bayern/'
		},
		{
			name: 'Bremen',
			link: 'https://de.statista.com/statistik/daten/studie/253203/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-bremen/'
		},
		{
			name: 'Berlin',
			link: 'https://de.statista.com/statistik/daten/studie/253201/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-berlin/'
		},
		{
			name: 'Baden-Württemberg',
			link: 'https://de.statista.com/statistik/daten/studie/252496/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-baden-wuerttemberg/'
		},
		{
			name: 'Brandenburg',
			link: 'https://de.statista.com/statistik/daten/studie/253202/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-brandenburg/'
		},
		{
			name: 'Sachsen',
			link: 'https://de.statista.com/statistik/daten/studie/253210/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-sachsen/'
		},
		{
			name: 'Sachsen-Anhalt',
			link: 'https://de.statista.com/statistik/daten/studie/253211/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-sachsen-anhalt/'
		},
		{
			name: 'Saarland',
			link: 'https://de.statista.com/statistik/daten/studie/253209/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-im-saarland/'
		},
		{
			name: 'Schleswig-Holstein',
			link: 'https://de.statista.com/statistik/daten/studie/253212/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-schleswig-holstein/'
		},
		{
			name: 'Hamburg',
			link: 'https://de.statista.com/statistik/daten/studie/252383/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-hamburg/'
		},
		{
			name: 'Thüringen',
			link: 'https://de.statista.com/statistik/daten/studie/253213/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-thueringen/'
		},
		{
			name: 'Mecklenburg-Vorpommern',
			link: 'https://de.statista.com/statistik/daten/studie/253205/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-mecklenburg-vorpommern/'
		},
		{
			name: 'Hessen',
			link: 'https://de.statista.com/statistik/daten/studie/253204/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-hessen/'
		},
		{
			name: 'Nordrhein-Westfahlen',
			link: 'https://de.statista.com/statistik/daten/studie/253207/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-nordrhein-westfalen/'
		},
		{
			name: 'Niedersachsen',
			link: 'https://de.statista.com/statistik/daten/studie/253206/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-niedersachsen/'
		},
		{
			name: 'Rheinland-Pfalz',
			link: 'https://de.statista.com/statistik/daten/studie/253208/umfrage/arbeitnehmerentgelt-je-arbeitnehmer-in-rheinland-pfalz/'
		},
		{
			name: 'Deutschland',
			link: 'https://de.statista.com/statistik/daten/studie/440525/umfrage/arbeitnehmerentgelte-je-arbeitnehmer-in-deutschland/'
		}
	];

	let Bevoelkerungsdichte = [
		{
			name: 'Bayern',
			link: 'https://de.statista.com/statistik/daten/studie/254957/umfrage/bevoelkerungsdichte-in-bayern/'
		},
		{
			name: 'Bremen',
			link: 'https://de.statista.com/statistik/daten/studie/256231/umfrage/bevoelkerungsdichte-in-bremen/'
		},
		{
			name: 'Berlin',
			link: 'https://de.statista.com/statistik/daten/studie/255791/umfrage/bevoelkerungsdichte-in-berlin/'
		},
		{
			name: 'Baden-Württemberg',
			link: 'https://de.statista.com/statistik/daten/studie/254840/umfrage/bevoelkerungsdichte-in-baden-wuerttemberg/'
		},
		{
			name: 'Brandenburg',
			link: 'https://de.statista.com/statistik/daten/studie/256068/umfrage/bevoelkerungsdichte-in-brandenburg/'
		},
		{
			name: 'Sachsen',
			link: 'https://de.statista.com/statistik/daten/studie/274543/umfrage/bevoelkerungsdichte-in-sachsen/'
		},
		{
			name: 'Sachsen-Anhalt',
			link: 'https://de.statista.com/statistik/daten/studie/274544/umfrage/bevoelkerungsdichte-in-sachsen-anhalt/'
		},
		{
			name: 'Saarland',
			link: 'https://de.statista.com/statistik/daten/studie/274547/umfrage/bevoelkerungsdichte-im-saarland/'
		},
		{
			name: 'Schleswig-Holstein',
			link: 'https://de.statista.com/statistik/daten/studie/274545/umfrage/bevoelkerungsdichte-in-schleswig-holstein/'
		},
		{
			name: 'Hamburg',
			link: 'https://de.statista.com/statistik/daten/studie/254514/umfrage/bevoelkerungsdichte-in-hamburg/'
		},
		{
			name: 'Thüringen',
			link: 'https://de.statista.com/statistik/daten/studie/274546/umfrage/bevoelkerungsdichte-in-thueringen/'
		},
		{
			name: 'Mecklenburg-Vorpommern',
			link: 'https://de.statista.com/statistik/daten/studie/258841/umfrage/bevoelkerungsdichte-in-mecklenburg-vorpommern/'
		},
		{
			name: 'Hessen',
			link: 'https://de.statista.com/statistik/daten/studie/258107/umfrage/bevoelkerungsdichte-in-hessen/'
		},
		{
			name: 'Nordrhein-Westfahlen',
			link: 'https://de.statista.com/statistik/daten/studie/258069/umfrage/bevoelkerungsdichte-in-nordrhein-westfalen/'
		},
		{
			name: 'Niedersachsen',
			link: 'https://de.statista.com/statistik/daten/studie/258893/umfrage/bevoelkerungsdichte-in-niedersachsen/'
		},
		{
			name: 'Rheinland-Pfalz',
			link: 'https://de.statista.com/statistik/daten/studie/274542/umfrage/bevoelkerungsdichte-in-rheinland-pfalz/'
		},
		{
			name: 'Deutschland',
			link: 'https://de.statista.com/statistik/daten/studie/440766/umfrage/bevoelkerungsdichte-in-deutschland/'
		}
	];

	let Einwohnerzahlen = [
		{
			name: 'Bayern',
			link: 'https://de.statista.com/statistik/daten/studie/154879/umfrage/entwicklung-der-bevoelkerung-von-bayern-seit-1961/'
		},
		{
			name: 'Bremen',
			link: 'https://de.statista.com/statistik/daten/studie/155144/umfrage/entwicklung-der-bevoelkerung-von-bremen-seit-1961/'
		},
		{
			name: 'Berlin',
			link: 'https://de.statista.com/statistik/daten/studie/154880/umfrage/entwicklung-der-bevoelkerung-von-berlin-seit-1961/'
		},
		{
			name: 'Baden-Württemberg',
			link: 'https://de.statista.com/statistik/daten/studie/154878/umfrage/entwicklung-der-bevoelkerung-von-baden-wuerttemberg-seit-1961/'
		},
		{
			name: 'Brandenburg',
			link: 'https://de.statista.com/statistik/daten/studie/155142/umfrage/entwicklung-der-bevoelkerung-von-brandenburg-seit-1961/'
		},
		{
			name: 'Sachsen',
			link: 'https://de.statista.com/statistik/daten/studie/155167/umfrage/entwicklung-der-bevoelkerung-von-sachsen-seit-1961/'
		},
		{
			name: 'Sachsen-Anhalt',
			link: 'https://de.statista.com/statistik/daten/studie/155169/umfrage/entwicklung-der-bevoelkerung-von-sachsen-anhalt-seit-1961/'
		},
		{
			name: 'Saarland',
			link: 'https://de.statista.com/statistik/daten/studie/155163/umfrage/entwicklung-der-bevoelkerung-des-saarlands-seit-1961/'
		},
		{
			name: 'Schleswig-Holstein',
			link: 'https://de.statista.com/statistik/daten/studie/155171/umfrage/entwicklung-der-bevoelkerung-von-schleswig-holstein-seit-1961/'
		},
		{
			name: 'Hamburg',
			link: 'https://de.statista.com/statistik/daten/studie/155147/umfrage/entwicklung-der-bevoelkerung-von-hamburg-seit-1961/'
		},
		{
			name: 'Thüringen',
			link: 'https://de.statista.com/statistik/daten/studie/155172/umfrage/entwicklung-der-bevoelkerung-von-thueringen-seit-1961/'
		},
		{
			name: 'Mecklenburg-Vorpommern',
			link: 'https://de.statista.com/statistik/daten/studie/155151/umfrage/entwicklung-der-bevoelkerung-von-mecklenburg-vorpommern-seit-1961/'
		},
		{
			name: 'Hessen',
			link: 'https://de.statista.com/statistik/daten/studie/155150/umfrage/entwicklung-der-bevoelkerung-von-hessen-seit-1961/'
		},
		{
			name: 'Nordrhein-Westfahlen',
			link: 'https://de.statista.com/statistik/daten/studie/258069/umfrage/bevoelkerungsdichte-in-nordrhein-westfalen/'
		},
		{
			name: 'Niedersachsen',
			link: 'https://de.statista.com/statistik/daten/studie/155154/umfrage/entwicklung-der-bevoelkerung-von-niedersachsen-seit-1961/'
		},
		{
			name: 'Rheinland-Pfalz',
			link: 'https://de.statista.com/statistik/daten/studie/155158/umfrage/entwicklung-der-bevoelkerung-von-rheinland-pfalz-seit-1961/'
		},
		{
			name: 'Deutschland',
			link: 'https://de.statista.com/statistik/daten/studie/1358/umfrage/entwicklung-der-gesamtbevoelkerung-deutschlands/'
		}
	];

	let Arbeitslosenquote = [
		{
			name: 'Bayern',
			link: 'https://de.statista.com/statistik/daten/studie/2517/umfrage/entwicklung-der-arbeitslosenquote-in-bayern-seit-1999/'
		},
		{
			name: 'Bremen',
			link: 'https://de.statista.com/statistik/daten/studie/2512/umfrage/entwicklung-der-arbeitslosenquote-in-bremen-seit-1999/'
		},
		{
			name: 'Berlin',
			link: 'https://de.statista.com/statistik/daten/studie/2519/umfrage/entwicklung-der-arbeitslosenquote-in-berlin-seit-1999/'
		},
		{
			name: 'Baden-Württemberg',
			link: 'https://de.statista.com/statistik/daten/studie/2516/umfrage/entwicklung-der-arbeitslosenquote-in-baden-wuerttemberg-seit-1999/'
		},
		{
			name: 'Brandenburg',
			link: 'https://de.statista.com/statistik/daten/studie/2520/umfrage/entwicklung-der-arbeitslosenquote-in-brandenburg-seit-1999/'
		},
		{
			name: 'Sachsen',
			link: 'https://de.statista.com/statistik/daten/studie/2522/umfrage/entwicklung-der-arbeitslosenquote-in-sachsen-seit-1999/'
		},
		{
			name: 'Sachsen-Anhalt',
			link: 'https://de.statista.com/statistik/daten/studie/2523/umfrage/entwicklung-der-arbeitslosenquote-in-sachsen-anhalt-seit-1999/'
		},
		{
			name: 'Saarland',
			link: 'https://de.statista.com/statistik/daten/studie/2518/umfrage/entwicklung-der-arbeitslosenquote-im-saarland-seit-1999/'
		},
		{
			name: 'Schleswig-Holstein',
			link: 'https://de.statista.com/statistik/daten/studie/2509/umfrage/entwicklung-der-arbeitslosenquote-in-schleswig-holstein-seit-1999/'
		},
		{
			name: 'Hamburg',
			link: 'https://de.statista.com/statistik/daten/studie/2510/umfrage/entwicklung-der-arbeitslosenquote-in-hamburg-seit-1999/'
		},
		{
			name: 'Thüringen',
			link: 'https://de.statista.com/statistik/daten/studie/2524/umfrage/entwicklung-der-arbeitslosenquote-in-thueringen-seit-1999/'
		},
		{
			name: 'Mecklenburg-Vorpommern',
			link: 'https://de.statista.com/statistik/daten/studie/2521/umfrage/entwicklung-der-arbeitslosenquote-in-mecklenburg-vorpommern-seit-1999/'
		},
		{
			name: 'Hessen',
			link: 'https://de.statista.com/statistik/daten/studie/2514/umfrage/entwicklung-der-arbeitslosenquote-in-hessen-seit-1999/'
		},
		{
			name: 'Nordrhein-Westfahlen',
			link: 'https://de.statista.com/statistik/daten/studie/2513/umfrage/entwicklung-der-arbeitslosenquote-in-nordrhein-westfalen-seit-1999/'
		},
		{
			name: 'Niedersachsen',
			link: 'https://de.statista.com/statistik/daten/studie/2511/umfrage/entwicklung-der-arbeitslosenquote-in-niedersachsen-seit-1999/'
		},
		{
			name: 'Rheinland-Pfalz',
			link: 'https://de.statista.com/statistik/daten/studie/2515/umfrage/entwicklung-der-arbeitslosenquote-in-rheinland-pfalz-seit-1999/'
		},
		{
			name: 'Deutschland',
			link: 'https://de.statista.com/statistik/daten/studie/1224/umfrage/arbeitslosenquote-in-deutschland-seit-1995/'
		}
	];

	let columnData = [
		{
			id: 1,
			title: 'Unemployment Rate',
			links: Arbeitslosenquote
		},
		{
			id: 2,
			title: 'Average Annual Gross Employee Income',
			links: Arbeitnehmereinkommen
		},
		{
			id: 3,
			title: 'Population Density',
			links: Bevoelkerungsdichte
		},
		{
			id: 4,
			title: 'Inhabitants',
			links: Einwohnerzahlen
		}
	];

	let genesisTrafficLink = {
		title: 'Public Transportation',
		name: 'Company, passengers transported and passenger kilometers per federal state, quarters and type of transport',
		link: 'https://www-genesis.destatis.de/genesis//online?operation=table&code=46181-0015&bypass=true&levelindex=0&levelid=1697718366080#abreadcrumb'
	};

</script>

<div class="sources-container">
	<div id="main">
		{#each columnData as column (column.id)}
			<div class="column">
				<div class="title-container">
					<h2 class="h2">{column.title}</h2>
				</div>
				{#each column.links as { name, link }}
					<a href={link} class="link">{name}</a>
				{/each}
			</div>
		{/each}
		<div class="genesis-row">
			<div class="title-container-2">
				<h2 class="h2" style="margin-bottom: 1.5vh">{genesisTrafficLink.title}</h2>
			</div>
			<a href={genesisTrafficLink.link} class="link">{genesisTrafficLink.name}</a>
		</div>
	</div>
</div>

<style>

    .sources-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-left: 10vh;
        padding-right: 10vh;
        padding-top: 5vh;
        position: relative;
    }

    #main {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2vh;
    }

    .column {
        padding: 5vh;
        border-radius: 2vh;
    }

    .title-container {
        height: 5vh;
        margin-bottom: 3vh;
    }

    .title-container-2 {
        height: 5vh;
        margin-bottom: 1.5vh;
    }

    .h2 {
        color: var(--colorscheme-blue);
        font-size: 1.2em;
    }

    .link {
        display: block;
        margin-bottom: 1vh;
        text-decoration: none;
        color: var(--colorscheme-blue);
    }

    .link:hover {
        text-decoration-line: underline;
        text-decoration-thickness: 0.2vh;
        text-decoration-color: var(--colorscheme-orange);
    }

    .genesis-row {
        border-radius: 2vh;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        grid-column: span 4;
        margin-left: 5vh;
    }

</style>
<script>
	import { page } from '$app/stores';
	import '../styles/global.css';
</script>

<h1>{$page.status}: {$page.error.message}</h1>
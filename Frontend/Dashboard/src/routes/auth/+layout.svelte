<script lang="ts">
	import authBG from '#lib/assets/authBG.jpg';

	let { children } = $props();
</script>

<main
	class="grid min-h-dvh w-full items-center bg-cover bg-center bg-no-repeat"
	style:background-image="url({authBG})"
>
	{@render children()}
</main>

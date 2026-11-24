<script lang="ts">
	import { resolve } from '$app/paths';
	import { ChevronLeft } from '@lucide/svelte';
</script>

<main>
	<header class="flex items-center justify-start bg-linear-to-b from-[#508dff] to-[#2563eb] p-5 text-white gap-5">
		<a href={resolve('/')}> <ChevronLeft size={20}></ChevronLeft></a>
		<h1 class="text-xl">Chat</h1>
	</header>
</main>

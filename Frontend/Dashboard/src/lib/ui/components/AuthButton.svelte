<script lang="ts">
	import SpinningLoader from "../icons/SpinningLoader.svelte";

	let { 
		text, 
		authHandler, 
		bgColor, 
		isAuthenticating
	}: { text: string; 
		authHandler: () => void;
		bgColor: string, isAuthenticating: boolean } = $props();
</script>

<button
	onclick={authHandler}
	style:background-color={bgColor}
	class="w-full cursor-pointer rounded-md p-3 text-white active:opacity-75 relative"
	disabled={isAuthenticating}
>
	{text}
	{#if isAuthenticating}
	<div class="w-full h-full bg-[#929292e4] absolute inset-0 flex justify-center items-center rounded-md">
		<SpinningLoader size={23}></SpinningLoader>
	</div>
{/if}
</button>


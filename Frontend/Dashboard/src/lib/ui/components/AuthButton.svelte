<script lang="ts">
	import SpinningLoader from '../icons/SpinningLoader.svelte';

	let {
		text,
		authHandler,
		bgColor,
		isAuthenticating,
		type = 'button'
	}: {
		text: string;
		authHandler?: () => void;
		bgColor: string;
		isAuthenticating: boolean;
		type?: 'button' | 'submit' | 'reset';
	} = $props();
</script>

<button
	{type}
	onclick={authHandler}
	style:background-color={bgColor}
	class="relative w-full cursor-pointer rounded-md p-3 text-white active:opacity-75"
	disabled={isAuthenticating}
	aria-busy={isAuthenticating}
>
	{text}
	{#if isAuthenticating}
		<div
			class="absolute inset-0 flex h-full w-full items-center justify-center rounded-md bg-[#929292e4]"
		>
			<SpinningLoader size={23}></SpinningLoader>
		</div>
	{/if}
</button>

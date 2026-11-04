<script lang="ts">
	let { text }: { text: string } = $props();
</script>

<button
	onclick={() => {
		console.log(`${text} clicked`);
	}}
	class="w-full max-w-[25rem] cursor-pointer rounded-2xl bg-black p-3 text-white active:opacity-75"
>
	{text}
</button>

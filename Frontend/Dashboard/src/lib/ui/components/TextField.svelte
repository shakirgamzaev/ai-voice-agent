<script lang="ts">
	let {
		text,
		inputFieldType,
		value = $bindable('')
	}: { text: string; inputFieldType: string; value?: string } = $props();

	
</script>

<div class="flex w-full flex-col items-start gap-1.5">
	<p class="text-[0.9rem]">{text}</p>
	<input type={inputFieldType} bind:value class="w-full rounded-md border border-[#9a9a9a] p-1 py-1" />
</div>

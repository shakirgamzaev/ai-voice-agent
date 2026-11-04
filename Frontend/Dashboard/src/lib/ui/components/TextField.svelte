<script lang="ts">
	let { text, inputFieldType }: { text: string; inputFieldType: string } = $props();
</script>

<div class="flex w-full flex-col items-start gap-1.5">
	<p>{text}</p>
	<input type={inputFieldType} class="w-full rounded-md border p-1 py-2" />
</div>

<script lang="ts">
	import type { HTMLInputAttributes } from 'svelte/elements';

	let {
		text,
		inputFieldType,
		value = $bindable(''),
		autocomplete,
		required = false,
		minlength,
		maxlength
	}: {
		text: string;
		inputFieldType: string;
		value?: string;
		autocomplete?: HTMLInputAttributes['autocomplete'];
		required?: boolean;
		minlength?: number;
		maxlength?: number;
	} = $props();
	const inputId = $props.id();
</script>

<div class="flex w-full flex-col items-start gap-1.5">
	<label for={inputId} class="text-[0.9rem]">{text}</label>
	<input
		id={inputId}
		type={inputFieldType}
		bind:value
		{autocomplete}
		{required}
		{minlength}
		{maxlength}
		class="w-full rounded-md border border-[#9a9a9a] p-1 py-1"
	/>
</div>

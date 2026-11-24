<script lang="ts">
	let props: { isAiGenerated: boolean; text: string } = $props();
</script>

<div
	class={[
		'bg-linear-to-b p-3 shadow-[0_0_3px_2px_rgba(0,0,0,0.1)] rounded-lg self-start max-w-[20rem]',
		props.isAiGenerated
			? 'justify-self-start from-white to-[#f7f7f7] text-gray-900'
			: 'justify-self-end from-[#508dff] to-[#2563eb] text-white'
	]}
>
	{props.text}
</div>

<script lang="ts">
	import { resolve } from '$app/paths';
	import { ChevronLeft } from '@lucide/svelte';
	import ChatBubble from './ChatBubble.svelte';
	import TypeMessage from './TypeMessage.svelte';

	const sampleMessages = Array.from({ length: 8 }, (_, index) => {
		const isAiGenerated = index % 2 === 0;

		return {
			id: index + 1,
			isAiGenerated,
			text: isAiGenerated ? 'Hi! How can I help you today?' : 'I have a question about my order.'
		};
	});
</script>

<main class="grid h-dvh grid-cols-[1fr] grid-rows-[auto_minmax(0,1fr)_auto]">
	<header
		class="flex items-center justify-start gap-5 bg-linear-to-b from-[#508dff] to-[#2563eb] p-5 text-white"
	>
		<a href={resolve('/')}> <ChevronLeft size={20}></ChevronLeft></a>
		<h1 class="text-xl">Chat</h1>
	</header>
	<div class="grid grid-cols-[1fr] content-start gap-y-8 overflow-y-auto p-6 bg-[#f6f6f6]">
		{#each sampleMessages as message (message.id)}
			<ChatBubble isAiGenerated={message.isAiGenerated} text={message.text} />
		{/each}
	</div>
	<TypeMessage></TypeMessage>
</main>

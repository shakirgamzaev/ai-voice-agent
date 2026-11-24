<script lang="ts">
	import { resolve } from '$app/paths';
	import type { PageRouteId } from '$app/types';
	import { ChevronRight, MessageSquareText } from '@lucide/svelte';
	let { url }: { url: PageRouteId } = $props();
</script>

<a
	href={resolve(url)}
	class="shadow- flex justify-between bg-linear-to-b from-[#fafafa] to-[#f8f8f8] p-4 shadow-[0_0_6px_3px_rgba(0,0,0,0.1)]"
>
	<div class="flex gap-2 items-center">
		<MessageSquareText size={17}></MessageSquareText>
		<p>Start Chat</p>
	</div>
	<ChevronRight></ChevronRight>
</a>

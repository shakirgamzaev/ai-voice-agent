<script lang="ts" module>
	import type { LucideIcon } from '@lucide/svelte';

	export type SectionLinkProps = {
		icon: LucideIcon;
		text: string;
		href: string;
	};
</script>

<script lang="ts">
	import SectionLink from '#lib/ui/components/SectionLink.svelte';
	import { page } from '$app/state';

	type Props = {
		title: string;
		links: SectionLinkProps[];
	};

	let { title, links }: Props = $props();
</script>

<div class="grid grid-cols-[1fr] gap-y-2">
	<h2 class="pl-3 text-[0.9rem] text-[#939393]">{title}</h2>

	{#each links as link (link.href)}
		<SectionLink
			iconSize={18}
			icon={link.icon}
			gap={0.8}
			text={link.text}
			href={link.href}
			isSelected={page.url.pathname.startsWith(link.href)}
		></SectionLink>
	{/each}
</div>

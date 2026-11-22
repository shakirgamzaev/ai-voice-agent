<script lang="ts">
	import OrgHomeIcon from '#lib/ui/components/OrgHomeIcon.svelte';
	import { Settings } from '@lucide/svelte';
	import { getContext } from 'svelte';

	let {
		organizationName,
		role,
		isOpen = $bindable()
	}: { organizationName: string; role: string; isOpen: boolean } = $props();

	let orgOverlay = getContext<{isShown: boolean}>("orgOverlay")

</script>

<section
	class="absolute top-full left-0 z-10 mt-[7px] grid w-[20rem] grid-cols-[1fr] rounded-md border border-gray-300 bg-white p-3 shadow-[0_0_10px_rgba(0,0,0,0.15)]"
>
	<div class="flex items-center justify-between p-2">
		<div class="flex items-center gap-2">
			<OrgHomeIcon iconWidth={22} iconHeight={22}></OrgHomeIcon>
			<div class="flex flex-col">
				<p class="text-[0.88rem]">{organizationName}</p>
				<p class="text-[0.8rem] text-gray-500">{role}</p>
			</div>
		</div>
		<button
			class="flex items-center gap-1.5 rounded-md border border-gray-300 p-1 text-gray-700 shadow-[2px_2px_4px_rgba(0,0,0,0.1)]"
			onclick={() => {
				orgOverlay.isShown = true;
				isOpen = false;
			}}
		>
			<Settings size={15}></Settings>
			<span class="text-sm">Manage</span>
		</button>
	</div>
</section>

<script lang="ts">
	import { House, Users, X } from '@lucide/svelte';
	import BtnSectionChange from './components/BtnSectionChange.svelte';
	import OrgGeneral from './OrgGeneral.svelte';
	import OrgMembers from './OrgMembers.svelte';
	import { getContext } from 'svelte';
	import type { authClient } from '#lib/auth-client.ts';

	type Section = 'general' | 'members';

	let {
		organization,
		role
	}: { organization: typeof authClient.$Infer.Organization; role: string } = $props();
	let orgOverlay = getContext<{ isShown: boolean }>('orgOverlay');
	let activeSection = $state<Section>('general');
</script>

<div class="fixed inset-0 z-50 flex h-full w-full items-center justify-center bg-[#0101015e]">
	<div
		class="grid aspect-square h-[75dvh] min-h-[30rem] max-w-[55rem] grow grid-cols-[1fr_3fr] bg-white  rounded-2xl overflow-hidden"
	>
		<div class="flex flex-col bg-[#f7f7f7] p-4">
			<h1 class="self-start text-2xl">Organization</h1>
			<h3 class="mb-[2rem] self-start text-[0.74rem] text-[#828282]">Manage your organization</h3>
			<BtnSectionChange
				icon={House}
				text="General"
				iconSize={17}
				isSelected={activeSection === 'general'}
				onclick={() => (activeSection = 'general')}
			></BtnSectionChange>
			<BtnSectionChange
				icon={Users}
				text="Members"
				iconSize={17}
				isSelected={activeSection === 'members'}
				onclick={() => (activeSection = 'members')}
			></BtnSectionChange>
		</div>
		<div class="grid grid-cols-[1fr] content-start p-6 gap-y-11">
			<div class="flex items-center justify-between self-start">
				<h1 class="text-xl font-bold">{activeSection === 'general' ? 'General' : 'Members'}</h1>
				<button
					onclick={() => {
						orgOverlay.isShown = false;
					}}
				>
					<X></X>
				</button>
			</div>
			{#if activeSection === 'general'}
				<OrgGeneral {organization} {role}></OrgGeneral>
			{:else if activeSection === 'members'}
				<OrgMembers></OrgMembers>
			{/if}
		</div>
	</div>
</div>

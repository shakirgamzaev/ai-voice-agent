<script lang="ts">
	import { authClient } from '#lib/auth-client.ts';
	import OrgHomeIcon from '#lib/ui/components/OrgHomeIcon.svelte';
	import SpinningLoader from '#lib/ui/icons/SpinningLoader.svelte';

	let {
		organization,
		role
	}: { organization: typeof authClient.$Infer.Organization; role: string } = $props();

	// Better Auth stores multiple roles as one comma-separated string, e.g. "owner,admin".
	const isOwner = $derived(
		role
			.split(',')
			.map((r) => r.trim())
			.includes('owner')
	);
	let errorThrown = $state(false);
	let isDeleting = $state(false);

	async function deleteOrganization() {
		if (isDeleting) {
			return;
		}
		isDeleting = true;

		try {
			await new Promise((resolve) => setTimeout(resolve, 2000));
		} catch (error) {
			console.log('some error');
		} finally {
			isDeleting = false;
		}
	}
</script>

<div class="grid grid-cols-[1fr_1fr_1fr] gap-y-9 text-[0.9rem]">
	<p class="self-center">Organization Profile</p>
	<div class="flex items-center justify-start gap-2">
		<OrgHomeIcon iconWidth={26} iconHeight={26}></OrgHomeIcon>
		<p>{organization.name}</p>
	</div>
	<p class="self-center">Update Profile</p>
	<p>Leave Organization</p>
	<button class="col-span-2 text-start font-medium text-[#db0202] active:opacity-50"
		>Leave Organization</button
	>
	{#if isOwner}
		<p class="self-center">Delete Organization</p>

		<button
			class="relative self-center justify-self-start rounded-md bg-linear-to-b from-[#e63232] to-[#cf0202] p-1.5 text-start font-medium text-white enabled:active:opacity-50 disabled:from-[#e63232]/60 disabled:to-[#cf0202]/60"
			onclick={deleteOrganization}
            disabled={isDeleting}
		>
			<!-- invisible keeps the text's space, so the button doesn't change size while loading. -->
			<span class={[isDeleting && 'invisible']}>Delete Organization</span>
			{#if isDeleting}
				<span class="absolute inset-0 flex items-center justify-center">
					<SpinningLoader size={18} strokeColor="#e5e7eb"></SpinningLoader>
				</span>
			{/if}
		</button>
	{/if}
</div>

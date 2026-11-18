<script lang="ts">
	import { authClient } from '#lib/auth-client.ts';
	import { goto } from '$app/navigation';
	import AddLogoSection from './AddLogoSection.svelte';
    import { resolve } from '$app/paths';
	import CreateOrgBtn from './components/CreateOrgBtn.svelte';
	import CustomTextField from './components/CustomTextField.svelte';

	let organizationName = $state('');
	let orgSlug = $state('');
	let canCreateOrganization = $derived(
		organizationName.trim().length > 0 && orgSlug.trim().length > 0
	);

	async function createOrganization() {
		try {
			await authClient.organization.create({
				name: organizationName,
				slug: orgSlug
			});
            await goto(resolve("/dashboard/conversations"))
		} catch (error) {
            //TODO, add UI to display the error
            console.log(error);
        }
	}
</script>

<main class="flex min-h-dvh w-full items-center justify-center p-5">
	<div
		class="flex max-w-180 grow flex-col gap-4 rounded-xl p-6 shadow-[8px_8px_11px_8px_rgba(0,0,0,0.09)]"
	>
		<h2 class="text-xl font-bold">Create Organization</h2>
		<AddLogoSection></AddLogoSection>
		<CustomTextField
			label="Name"
			placeholder="Organization name"
			bind:value={organizationName}
		></CustomTextField>

		<CustomTextField label="Slug" placeholder="my-org" bind:value={orgSlug}></CustomTextField>
		<CreateOrgBtn isDisabled={!canCreateOrganization} createOrgHandler={createOrganization}
		></CreateOrgBtn>
	</div>
</main>

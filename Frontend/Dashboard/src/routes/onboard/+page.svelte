<script lang="ts">
	import AddLogoSection from "./AddLogoSection.svelte";
	import CreateOrgBtn from "./components/CreateOrgBtn.svelte";
	import CustomTextField from "./components/CustomTextField.svelte";

    let organizationName = $state("")
    let orgSlug = $state("")
    let canCreateOrganization = $derived(organizationName.trim().length > 0 && orgSlug.trim().length > 0)

</script>
<main class="flex w-full min-h-dvh justify-center items-center p-5">
    <div class="p-6 flex flex-col  grow max-w-[45rem] rounded-xl gap-4 shadow-[8px_8px_11px_8px_rgba(0,0,0,0.09)]">
        <h2 class="font-bold text-xl">Create Organization</h2>
        <AddLogoSection></AddLogoSection>
        <CustomTextField 
            label="Name" 
            placeholder="Organization name"
            bind:value={organizationName}>
        </CustomTextField>

        <CustomTextField 
            label="Slug" 
            placeholder="my-org"
            bind:value={orgSlug}>
        </CustomTextField>
        <CreateOrgBtn isDisabled={!canCreateOrganization}></CreateOrgBtn>
    </div>
</main>

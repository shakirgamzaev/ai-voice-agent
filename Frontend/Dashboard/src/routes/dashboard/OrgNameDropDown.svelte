<script lang="ts">
	import OrgHomeIcon from '#lib/ui/components/OrgHomeIcon.svelte';
	import { ChevronDown } from '@lucide/svelte';
	import UserProfileMenu from '#lib/ui/components/UserProfileDropDown/UserProfileMenu.svelte';
	import OrgNameDropDownDetail from './OrgNameDropDownDetail.svelte';

	let {
		organizationName,
		userName,
		email,
		role
	}: { organizationName: string; userName: string; email: string; role: string } = $props();
	let isOpenOrgDropDown = $state(false);

	function displayOrgDropDown() {
		isOpenOrgDropDown = !isOpenOrgDropDown
	}

</script>

<div class="flex flex-col gap-2">
	<UserProfileMenu {userName} {email}></UserProfileMenu>
	<div class="relative">
		<button class="w-full hover:bg-[#0000000b] rounded-md cursor-pointer transition-colors duration-100" onclick={displayOrgDropDown}>
			<div class="flex items-center justify-between gap-2 p-1">
				<div class="flex items-center justify-start gap-2">
					<OrgHomeIcon iconWidth={13} iconHeight={15} padding={7}></OrgHomeIcon>
					<p class="text-[16px]">{organizationName}</p>
				</div>
				<ChevronDown size={20}></ChevronDown>
			</div>
		</button>
		{#if isOpenOrgDropDown}
			<OrgNameDropDownDetail {organizationName} {role} bind:isOpen={isOpenOrgDropDown}></OrgNameDropDownDetail>
		{/if}
	</div>
</div>

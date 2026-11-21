<script lang="ts">
	import ProfileCircleIcon from '#lib/ui/icons/ProfileCircleIcon.svelte';
	import UserProfileDropDown from './UserProfileDropDown.svelte';

	let { userName, email }: { userName: string; email: string } = $props();

	let showUserProfileDropDown = $state(false);
</script>

<!-- relative + self-start: the dropdown is positioned against a box exactly the size of the circle. -->
<div class="relative self-start">
	<button
		type="button"
		class="block cursor-pointer rounded-full"
		aria-haspopup="true"
		aria-expanded={showUserProfileDropDown}
		aria-label="User profile menu"
		onclick={() => (showUserProfileDropDown = !showUserProfileDropDown)}
	>
		<ProfileCircleIcon {userName} size={37}></ProfileCircleIcon>
	</button>

	{#if showUserProfileDropDown}
		<UserProfileDropDown {userName} {email}></UserProfileDropDown>
	{/if}
</div>

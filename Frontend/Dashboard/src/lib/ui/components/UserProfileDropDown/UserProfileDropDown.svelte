<script lang="ts">
    import { Settings, LogOut } from "@lucide/svelte";
	import UserProfileBtn from "./UserProfileBtn.svelte";
	import ProfileCircleIcon from "#lib/ui/icons/ProfileCircleIcon.svelte";
    import { authClient } from '#lib/auth-client.ts';
    import { goto } from '$app/navigation';
    import { resolve } from '$app/paths';

    let {userName, email}: {userName: string, email: string} = $props()
    
    async function logOut() {
        try {
            const { error } = await authClient.signOut()
            if (error) {throw error}
            await goto(resolve("/auth/sign-in"))
        }
        catch(error) {
            console.log(error);
        }

    }

    function manageAccount() {
        
    }

</script>

<div class="absolute left-0 top-full z-10 mt-[10px] grid grid-cols-[1fr] w-[22.5rem] rounded-md border border-gray-300 bg-white shadow-[0_0_10px_rgba(0,0,0,0.15)]">
    <div class="flex gap-4 items-center mb-[10px] px-3 pt-2.5">
        <ProfileCircleIcon userName={userName} size={28}></ProfileCircleIcon>
        <div class="flex flex-col">
            <p class="text-[0.97rem]">{userName}</p>
            <p class="text-[0.83rem] text-gray-500">{email}</p>
        </div>
    </div>

    <UserProfileBtn icon={Settings} iconSize={18} text="Manage Account" handler={manageAccount}></UserProfileBtn>
    <UserProfileBtn icon={LogOut} iconSize={18} text="Sign Out" handler={logOut}></UserProfileBtn>

</div>
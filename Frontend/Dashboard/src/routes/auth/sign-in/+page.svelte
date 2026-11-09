<script lang="ts">
	import AuthButton from '#lib/ui/components/AuthButton.svelte';
	import GoogleButton from '#lib/ui/components/GoogleButton.svelte';
	import TextField from '#lib/ui/components/TextField.svelte';
	import { resolve } from '$app/paths';
	import BottomSection from './BottomSection.svelte';
	import { signUserIn } from '#lib/utils/auth/sign-in.ts';
	import type { authClient } from '#lib/auth-client.ts';
	import { goto } from '$app/navigation';
	import { ENVIRONMENT } from "$app/env/public"
	type AuthError = NonNullable<
		Awaited<ReturnType<typeof authClient.signIn.email>>['error']
	>;
	const isDevEnvironment = ENVIRONMENT == "dev" 

	let credentials = $state({
		email: '',
		password: ''
	});
	let isError = $state<AuthError | null>(null);
	let isAuthenticating = $state(false)


	async function signIn() {
		if (isAuthenticating) {
			return
		}
		if (isDevEnvironment) {
			console.log("signIn called");
		}

		isError = null;
		isAuthenticating = true
		
		//simulate network call
		await new Promise<void>((resolve) => setTimeout(resolve, 1000));
		
		try {
			await signUserIn(credentials.email, credentials.password);
			await goto(resolve("/dashboard/conversations"))
		} catch (error) {
			isError = error as AuthError;
		}
		finally{
			isAuthenticating = false
		}
	}
	
</script>

<main class="flex items-center justify-center p-8 lg:justify-end">
	<div
		class="flex max-w-[40rem] grow flex-col gap-5 rounded-2xl bg-white p-6 shadow-[3px_3px_8px_4px_rgba(0,0,0,0.14)]"
	>
		<div class="grid grid-cols-[1fr] justify-items-start">
			<h1 class="text-4xl">Welcome Back</h1>
			<h3 class="text-[#5f5f5f]">Sign in to your workspace</h3>
		</div>
		<div class="grid grid-cols-[1fr] gap-y-5">
			<GoogleButton logoSize={30} text="Continue with Google"></GoogleButton>
			<div class="flex items-center">
				<div class="h-[1px] grow bg-[#a5a5a5]"></div>
				<p class="px-3">or sign in with email</p>
				<div class="h-[1px] grow bg-[#a5a5a5]"></div>
			</div>
		</div>
		<div class="grid grid-cols-[1fr] gap-y-5">
			<TextField 
				text="Email" 
				inputFieldType="email" 
				bind:value={credentials.email}>
			</TextField>
			<TextField 
				text="Password" 
				inputFieldType="password" 
				bind:value={credentials.password}>
			</TextField>
			{#if isError}
				<p role="alert" class="text-red-600">{isError.message ?? 'Sign-in failed. Please try again.'}</p>
			{/if}
		</div>
		<BottomSection></BottomSection>
		<div class="grid grid-cols-[1fr] gap-y-4">
			<AuthButton 
				text="Sign In" 
				authHandler={signIn} 
				bgColor="#278256"
				isAuthenticating={isAuthenticating}
				>
			</AuthButton>
			<div class="flex self-center items-center justify-center gap-3">
				<p>New to Mira?</p>
				<a href={resolve('/auth/sign-up')} class="text-green-800">Create an account</a>
			</div>
		</div>
	</div>
</main>

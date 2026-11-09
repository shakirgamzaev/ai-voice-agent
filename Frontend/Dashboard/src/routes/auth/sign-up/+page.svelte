<script lang="ts">
	import AuthButton from '#lib/ui/components/AuthButton.svelte';
	import GoogleButton from '#lib/ui/components/GoogleButton.svelte';
	import TextField from '#lib/ui/components/TextField.svelte';
	import { resolve } from '$app/paths';
	import { goto } from '$app/navigation';
	import { signUserUp } from '#lib/utils/auth/sign-up.ts';
	import type { authClient } from '#lib/auth-client.ts';

	type AuthError = NonNullable<
		Awaited<ReturnType<typeof authClient.signUp.email>>['error']
	>;

	let credentials = $state({
		name: '',
		email: '',
		password: ''
	});
	let isError = $state<AuthError | null>(null);
	let isAuthenticating = $state(false);

	async function signUp() {
		if (isAuthenticating) return;

		isError = null;
		isAuthenticating = true;
		await new Promise<void>((resolve) => setTimeout(resolve, 1000));

		try {
			await signUserUp(credentials.name, credentials.email, credentials.password);
			await goto(resolve('/dashboard/conversations'));
		} catch (error) {
			isError = error as AuthError;
		} finally {
			isAuthenticating = false;
		}
	}
</script>

<main class="flex items-center justify-center p-8 lg:justify-end">
	<div
		class="flex max-w-[40rem] grow flex-col gap-5 rounded-2xl bg-white p-6 shadow-[3px_3px_8px_4px_rgba(0,0,0,0.14)]"
	>
		<div class="grid grid-cols-[1fr] justify-items-start">
			<h1 class="text-4xl">Create your account</h1>
			<h3 class="text-[#5f5f5f]">Sign up to get started</h3>
		</div>
		<div class="grid grid-cols-[1fr] gap-y-5">
			<GoogleButton logoSize={30} text="Continue with Google"></GoogleButton>
			<div class="flex items-center">
				<div class="h-[1px] grow bg-[#a5a5a5]"></div>
				<p class="px-3">or sign up with email</p>
				<div class="h-[1px] grow bg-[#a5a5a5]"></div>
			</div>
		</div>
		<div class="grid grid-cols-[1fr] gap-y-5">
			<TextField text="Name" inputFieldType="text" bind:value={credentials.name}></TextField>
			<TextField text="Email" inputFieldType="email" bind:value={credentials.email}></TextField>
			<TextField text="Password" inputFieldType="password" bind:value={credentials.password}></TextField>
			{#if isError}
				<p role="alert" class="text-red-600">{isError.message ?? 'Sign-up failed. Please try again.'}</p>
			{/if}
		</div>
		<div class="grid grid-cols-[1fr] gap-y-4">
			<AuthButton 
				text="Sign Up" 
				authHandler={signUp} 
				bgColor="#278256"
				{isAuthenticating}
				>
				</AuthButton>
			<div class="flex items-center justify-center gap-3 self-center">
				<p>Already have an account?</p>
				<a href={resolve('/auth/sign-in')} class="text-green-800">Sign in</a>
			</div>
		</div>
	</div>
</main>

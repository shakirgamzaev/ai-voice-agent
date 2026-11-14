<script lang="ts">
	import AuthButton from '#lib/ui/components/AuthButton.svelte';
	import TextField from '#lib/ui/components/TextField.svelte';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';
	import { requestPasswordReset } from '#lib/utils/auth/request-password-reset.ts';
	import type { authClient } from '#lib/auth-client.ts';

	type AuthError = NonNullable<
		Awaited<ReturnType<typeof authClient.requestPasswordReset>>['error']
	>;

	let email = $state('');
	let isError = $state<AuthError | null>(null);
	let isSubmitting = $state(false);
	let isSent = $state(false);

	async function sendResetLink() {
		if (isSubmitting) return;

		isError = null;
		isSubmitting = true;

		try {
			await requestPasswordReset(email, `${page.url.origin}${resolve('/auth/reset-password')}`);
			// Always show the sent state so we never reveal whether an account exists.
			isSent = true;
		} catch (error) {
			isError = error as AuthError;
		} finally {
			isSubmitting = false;
		}
	}
</script>

<main class="flex items-center justify-center p-8 lg:justify-end">
	<div
		class="flex max-w-[40rem] grow flex-col gap-5 rounded-2xl bg-white p-6 shadow-[3px_3px_8px_4px_rgba(0,0,0,0.14)]"
	>
		{#if isSent}
			<div class="grid grid-cols-[1fr] justify-items-start gap-y-2">
				<h1 class="text-4xl">Check your inbox</h1>
				<h3 class="text-[#5f5f5f]">
					If an account exists for <span class="font-medium text-black">{email}</span>, we've
					sent a link to reset your password. The link expires in 1 hour.
				</h3>
			</div>
			<p class="text-[0.9rem] text-[#5f5f5f]">
				Didn't get it? Check your spam folder, or
				<button
					type="button"
					onclick={() => (isSent = false)}
					class="cursor-pointer text-green-800 underline-offset-2 hover:underline"
				>
					try a different email
				</button>.
			</p>
			<div class="flex items-center justify-center gap-3 self-center">
				<a href={resolve('/auth/sign-in')} class="text-green-800">Back to sign in</a>
			</div>
		{:else}
			<div class="grid grid-cols-[1fr] justify-items-start">
				<h1 class="text-4xl">Forgot your password?</h1>
				<h3 class="text-[#5f5f5f]">
					Enter your email and we'll send you a link to reset it
				</h3>
			</div>
			<div class="grid grid-cols-[1fr] gap-y-5">
				<TextField text="Email" inputFieldType="email" bind:value={email}></TextField>
				{#if isError}
					<p role="alert" class="text-red-600">
						{isError.message ?? 'Something went wrong. Please try again.'}
					</p>
				{/if}
			</div>
			<div class="grid grid-cols-[1fr] gap-y-4">
				<AuthButton
					text="Send reset link"
					authHandler={sendResetLink}
					bgColor="#278256"
					isAuthenticating={isSubmitting}
				></AuthButton>
				<div class="flex items-center justify-center gap-3 self-center">
					<p>Remembered it?</p>
					<a href={resolve('/auth/sign-in')} class="text-green-800">Back to sign in</a>
				</div>
			</div>
		{/if}
	</div>
</main>

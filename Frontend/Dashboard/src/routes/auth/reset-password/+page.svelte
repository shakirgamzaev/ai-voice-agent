<script lang="ts">
	import AuthButton from '#lib/ui/components/AuthButton.svelte';
	import TextField from '#lib/ui/components/TextField.svelte';
	import { resetUserPassword } from '#lib/utils/auth/reset-password.ts';
	import type { authClient } from '#lib/auth-client.ts';
	import { resolve } from '$app/paths';
	import { page } from '$app/state';

	type AuthError = NonNullable<Awaited<ReturnType<typeof authClient.resetPassword>>['error']>;

	const token = $derived(page.url.searchParams.get('token')?.trim() ?? '');
	const hasQueryError = $derived(page.url.searchParams.has('error'));
	let credentials = $state({ password: '', confirmPassword: '' });
	let isError = $state<AuthError | null>(null);
	let validationError = $state<string | null>(null);
	let isSubmitting = $state(false);
	let rejectedToken = $state<string | null>(null);
	let completedToken = $state<string | null>(null);

	const isInvalidLink = $derived(hasQueryError || !token || rejectedToken === token);
	const isReset = $derived(Boolean(token) && completedToken === token);

	async function resetPassword() {
		if (isSubmitting || isInvalidLink || isReset) return;

		isError = null;
		validationError = null;

		// Match Better Auth's current default password length limits.
		if (credentials.password.length < 8 || credentials.password.length > 128) {
			validationError = 'Use a password between 8 and 128 characters.';
			return;
		}
		if (credentials.password !== credentials.confirmPassword) {
			validationError = 'Passwords do not match.';
			return;
		}

		const submittedToken = token;
		isSubmitting = true;

		try {
			// The server validates expiry and consumes the token; the query string alone is not proof.
			await resetUserPassword(credentials.password, submittedToken);
			if (token !== submittedToken) return;

			credentials = { password: '', confirmPassword: '' };
			completedToken = submittedToken;
		} catch (error) {
			if (token !== submittedToken) return;
			const authError = error as AuthError;

			if (authError.code === 'INVALID_TOKEN' || authError.code === 'USER_NOT_FOUND') {
				// Better Auth uses INVALID_TOKEN for expired, unknown, and already-used tokens.
				rejectedToken = submittedToken;
				credentials = { password: '', confirmPassword: '' };
			} else {
				isError = authError;
			}
		} finally {
			isSubmitting = false;
		}
	}
</script>

<svelte:head>
	<title>Reset password | Mira</title>
	<meta name="referrer" content="no-referrer" />
</svelte:head>

<main class="flex items-center justify-center p-8 lg:justify-end">
	<div
		class="flex max-w-[40rem] grow flex-col gap-5 rounded-2xl bg-white p-6 shadow-[3px_3px_8px_4px_rgba(0,0,0,0.14)]"
	>
		{#if isReset}
			<div class="grid grid-cols-[1fr] justify-items-start gap-y-2" role="status">
				<h1 class="text-4xl">Password reset</h1>
				<p class="text-[#5f5f5f]">
					Your password has been updated. Sign in with your new password to continue.
				</p>
			</div>
			<a href={resolve('/auth/sign-in')} class="text-center text-green-800">Back to sign in</a>
		{:else if isInvalidLink}
			<div class="grid grid-cols-[1fr] justify-items-start gap-y-2">
				<h1 class="text-4xl">Reset link unavailable</h1>
				<p role="alert" class="text-red-600">
					This password reset link is missing, invalid, or expired. Please request a new link.
				</p>
			</div>
			<a href={resolve('/auth/forgot-password')} class="text-center text-green-800">
				Request a new reset link
			</a>
			<a href={resolve('/auth/sign-in')} class="text-center text-green-800">Back to sign in</a>
		{:else}
			<div class="grid grid-cols-[1fr] justify-items-start gap-y-2">
				<h1 class="text-4xl">Choose a new password</h1>
				<p class="text-[#5f5f5f]">Use between 8 and 128 characters for your new password.</p>
			</div>
			<form
				class="flex flex-col gap-5"
				onsubmit={(event) => {
					event.preventDefault();
					void resetPassword();
				}}
			>
				<fieldset disabled={isSubmitting} class="grid min-w-0 grid-cols-[1fr] gap-y-5">
					<TextField
						text="New password"
						inputFieldType="password"
						autocomplete="new-password"
						required
						minlength={8}
						maxlength={128}
						bind:value={credentials.password}
					/>
					<TextField
						text="Confirm new password"
						inputFieldType="password"
						autocomplete="new-password"
						required
						minlength={8}
						maxlength={128}
						bind:value={credentials.confirmPassword}
					/>
				</fieldset>
				{#if validationError || isError}
					<p role="alert" class="text-red-600">
						{validationError ??
							isError?.message ??
							'Unable to reset your password. Please try again.'}
					</p>
				{/if}
				<AuthButton
					type="submit"
					text="Reset password"
					bgColor="#278256"
					isAuthenticating={isSubmitting}
				/>
			</form>
			<a href={resolve('/auth/sign-in')} class="text-center text-green-800">Back to sign in</a>
		{/if}
	</div>
</main>

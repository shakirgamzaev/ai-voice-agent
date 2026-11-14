import { authClient } from '#lib/auth-client.ts';

export async function requestPasswordReset(email: string, redirectTo: string) {
	const { data, error } = await authClient.requestPasswordReset({
		email,
		redirectTo
	});
	if (error) {
		throw error;
	}
	return data;
}

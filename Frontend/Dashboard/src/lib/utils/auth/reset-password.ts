import { authClient } from '#lib/auth-client.ts';

export async function resetUserPassword(newPassword: string, token: string) {
	const { data, error } = await authClient.resetPassword({ newPassword, token });

	if (error) {
		throw error;
	}

	return data;
}

import { authClient } from '#lib/auth-client.ts';

export async function signUserUp(name: string, email: string, password: string) {
	const { data, error } = await authClient.signUp.email({
		name,
		email,
		password
	});

	if (error) {
		throw error;
	}

	return data;
}

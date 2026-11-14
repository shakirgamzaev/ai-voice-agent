import { authClient } from "#lib/auth-client.ts";


export async function signUserIn(email: string, password: string) {
    const { data, error } = await authClient.signIn.email({
        email: email,
        password: password
    })

    if (error) {
        throw error;
    }

    return data;
}

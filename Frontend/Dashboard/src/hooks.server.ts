import { auth } from "#lib/auth.js";
import { svelteKitHandler } from "better-auth/svelte-kit";
import { building } from "$app/env"; // SvelteKit 2: "$app/environment"
import { redirect } from "@sveltejs/kit";

export async function handle({ event, resolve }) {
    const pathname = event.url.pathname;

    const isDashboardRoute =
        pathname === '/dashboard' ||
        pathname.startsWith('/dashboard/');

    //intercept and check that a user's cookie has an active browser session. If the session is expired take him to the sign in page, else allow to proceed
    if (!building && isDashboardRoute) {
        const session = await auth.api.getSession({
            headers: event.request.headers
        });

        if (!session) {
            redirect(303, '/auth/sign-in');
        }
    }


    return svelteKitHandler({ event, resolve, auth, building });
}
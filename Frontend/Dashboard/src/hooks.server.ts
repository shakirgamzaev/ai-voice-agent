import { auth } from "#lib/auth.js";
import { svelteKitHandler } from "better-auth/svelte-kit";
import { building } from "$app/env"; 
import { redirect } from "@sveltejs/kit";

export async function handle({ event, resolve }) {
    const pathname = event.url.pathname;
    const isRootPath = pathname === "/"
    const isDashboardRoute =
        pathname === '/dashboard' ||
        pathname.startsWith('/dashboard/');

    const isOrganizationCreateRoute =
        pathname === '/onboard' ||
        pathname.startsWith('/onboard/');

    // Both routes require a valid session from the incoming request's cookies.
    if(!building && isRootPath) {
        const session = await auth.api.getSession({
            headers: event.request.headers
        });
        if (!session) {
            redirect(303, "/auth/sign-in")
        }
        else {
            redirect(303, "/dashboard/conversations")
        }
    }

    if (!building && (isDashboardRoute || isOrganizationCreateRoute)) {
        const session = await auth.api.getSession({
            headers: event.request.headers
        });
        if (!session) {
            redirect(303, '/auth/sign-in');
        }

        const userOrganizations = await auth.api.listOrganizations({
            headers: event.request.headers
        });

        if (isDashboardRoute && userOrganizations.length === 0) {
            redirect(303, '/onboard');
        }
        if (isOrganizationCreateRoute && userOrganizations.length > 0) {
            redirect(303, '/dashboard/conversations');
        }
    }
    return svelteKitHandler({ event, resolve, auth, building });
}

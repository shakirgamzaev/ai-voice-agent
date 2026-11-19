import { auth } from "#lib/auth.js";
import { svelteKitHandler } from "better-auth/svelte-kit";
import { building } from "$app/env"; 
import { redirect } from "@sveltejs/kit";

export async function handle({ event, resolve }) {
    // Match on the resolved route, not the raw URL: an encoded path such as /%64ashboard
    // still resolves to /dashboard but would slip past a pathname string check.
    const routeId: string = event.route.id ?? '';
    const isRootPath = routeId === "/"
    const isDashboardRoute =
        routeId === '/dashboard' ||
        routeId.startsWith('/dashboard/');

    const isOrganizationCreateRoute =
        routeId === '/onboard' ||
        routeId.startsWith('/onboard/');

    // These routes require a valid session from the incoming request's cookies.
    if (!building && (isRootPath || isDashboardRoute || isOrganizationCreateRoute)) {
        const session = await auth.api.getSession({
            headers: event.request.headers
        });
        if (!session) {
            redirect(303, '/auth/sign-in');
        }

        const userOrganizations = await auth.api.listOrganizations({
            headers: event.request.headers
        });
        const hasOrganization = userOrganizations.length > 0;

        // A signed-in user without an organization can only be on the onboard page.
        if (!hasOrganization && !isOrganizationCreateRoute) {
            redirect(303, '/onboard');
        }
        // Once an organization exists, the root and onboard pages lead to the dashboard.
        if (hasOrganization && !isDashboardRoute) {
            redirect(303, '/dashboard/conversations');
        }

        event.locals.user = session.user;
        event.locals.organization =
            userOrganizations.find((org) => org.id === session.session.activeOrganizationId) ??
            userOrganizations[0];
    }
    
    return svelteKitHandler({ event, resolve, auth, building });
}

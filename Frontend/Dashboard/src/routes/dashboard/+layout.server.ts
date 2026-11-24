import type { LayoutServerLoad } from './$types';
import { redirect } from '@sveltejs/kit';
export const prerender = false;

// Runs on the first load of the dashboard, not on each navigation between dashboard pages:
// it reads nothing from the URL, so SvelteKit has no reason to rerun it when the path changes.
export const load: LayoutServerLoad = ({ locals }) => {
    const {user, organization, role} = locals
    if (!user || !organization || !role) {
        redirect(303, '/auth/sign-in')
    }
    return {user, organization, role}
}


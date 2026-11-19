import { redirect } from '@sveltejs/kit';
import { resolve } from '$app/paths';
import type { PageServerLoad } from './$types';

// Catches /dashboard itself and any dashboard path without its own page.
// The session and organization checks in hooks.server.ts run before this.
export const load: PageServerLoad = () => {
	redirect(307, resolve('/dashboard/conversations'));
};

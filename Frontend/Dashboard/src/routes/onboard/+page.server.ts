import type { PageServerLoad } from './$types';

export const prerender = false;

// Make client-side navigation request the server and run the session check in hooks.server.ts.
export const load: PageServerLoad = () => ({});

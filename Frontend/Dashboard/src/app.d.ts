// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces
import type { auth } from '#lib/auth.js';

declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
		interface Locals {
			user?: typeof auth.$Infer.Session.user;
            organization?: typeof auth.$Infer.Organization;
        }
	}
}


export {};

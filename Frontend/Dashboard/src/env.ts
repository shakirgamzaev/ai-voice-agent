import { defineEnvVars } from '@sveltejs/kit/env';

export const variables = defineEnvVars({
	DATABASE_URL: {
		description: 'Postgres connection string used by Better Auth'
	},
	BETTER_AUTH_SECRET: {},
	BETTER_AUTH_URL: {}
});

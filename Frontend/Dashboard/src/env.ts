import { defineEnvVars } from '@sveltejs/kit/env';

export const variables = defineEnvVars({
	DATABASE_URL: {
		description: 'Postgres connection string used by Better Auth'
	},
	BETTER_AUTH_SECRET: {},
	BETTER_AUTH_URL: {},
	ENVIRONMENT: {
		public: true
	},
	AWS_REGION:{
		schema: (value) => {
			if (typeof value !== "string" || value.trim() === "") {
				throw new Error("AWS_REGION must be a non empty string")
			}
			return value.trim()
		}
	}
});

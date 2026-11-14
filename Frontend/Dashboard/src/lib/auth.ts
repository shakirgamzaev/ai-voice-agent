import { betterAuth } from 'better-auth';
import { Pool } from 'pg';
import { DATABASE_URL, 
		BETTER_AUTH_SECRET,
		BETTER_AUTH_URL 
} from "$app/env/private"
import { PostgresDialect } from "kysely";
import { sendPasswordResetEmail } from './server/sendPasswordResetEmail';

export const auth = betterAuth({
	database: {
    	dialect: new PostgresDialect({
     	 pool: new Pool({
       		 connectionString: DATABASE_URL,
      	}),
    }	),
    	type: "postgres",
        schemaName: "authentication", 
 	},
	secret: BETTER_AUTH_SECRET,
	baseURL: BETTER_AUTH_URL,
	emailAndPassword: {
		enabled: true,
		revokeSessionsOnPasswordReset: true,
		sendResetPassword: async ({user, url}, request) => {
			await sendPasswordResetEmail(
				user.email, 
				url, 
				"mail@shakmira.com"
			)
		}
	}
});

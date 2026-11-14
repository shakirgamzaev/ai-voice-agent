import {
	SESv2Client,
	SendEmailCommand,
	type SESv2ClientConfig,
	type SendEmailCommandInput
} from '@aws-sdk/client-sesv2';

import { AWS_REGION } from '$app/env/private';

const sesClientConfig: SESv2ClientConfig = {
	region: AWS_REGION,
	maxAttempts: 2
};

const client = new SESv2Client(sesClientConfig);

export async function sendPasswordResetEmail(email: string, url: string, fromEmail: string) {
	const input: SendEmailCommandInput = {
		// Use a sender address covered by a verified SES identity in AWS_REGION.
		FromEmailAddress: fromEmail,
		Destination: {
			ToAddresses: [email]
		},
		Content: {
			Simple: {
				Subject: {
					Data: 'Reset your Mira password',
					Charset: 'UTF-8'
				},
				Body: {
					Text: {
						Data: [
							'You requested a password reset for your Mira account.',
							'Use this link to choose a new password:',
							url,
							'If you did not request this, you can ignore this email.'
						].join('\n\n'),
						Charset: 'UTF-8'
					}
				}
			}
		}
	};

	return client.send(new SendEmailCommand(input));
}

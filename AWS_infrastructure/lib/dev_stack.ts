import * as cdk from 'aws-cdk-lib/core';
import { Construct } from 'constructs';
import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as ecr from 'aws-cdk-lib/aws-ecr';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import { SqsEventSource } from 'aws-cdk-lib/aws-lambda-event-sources';
import * as secretsmanager from 'aws-cdk-lib/aws-secretsmanager';

export class DevStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const queue = new sqs.Queue(this, 'mira-test-queue', {
      visibilityTimeout: cdk.Duration.seconds(180),
    });

    const agentRepository = new ecr.Repository(this, 'MiraDevRepository', {
      repositoryName: 'mira-test/text-agent',
      emptyOnDelete: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const agent = new lambda.DockerImageFunction(this, 'TextAgent', {
      code: lambda.DockerImageCode.fromEcr(agentRepository, { tagOrDigest: 'test-002' }),
      architecture: lambda.Architecture.ARM_64,
      timeout: cdk.Duration.seconds(30),
      memorySize: 512,
    });
    const openaiSecret = secretsmanager.Secret.fromSecretNameV2(this, 'OpenAISecret', 'openai_api_key');
    openaiSecret.grantRead(agent);
    agent.addEventSource(new SqsEventSource(queue, { batchSize: 1 }));

    new cdk.CfnOutput(this, 'RepositoryUri', { value: agentRepository.repositoryUri });
    new cdk.CfnOutput(this, 'QueueUrl', { value: queue.queueUrl });
  }
}

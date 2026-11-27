#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib/core';
import { DevStack } from '../lib/dev_stack';

const app = new cdk.App();

new DevStack(app, 'mira-test', {
  env: { account: process.env.CDK_DEFAULT_ACCOUNT, region: process.env.CDK_DEFAULT_REGION },
});

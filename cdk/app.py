#!/usr/bin/env python3

from aws_cdk import core
from data_mgmt_stack import DataMgmtStack
from pipeline_stack import PipelineStack
from s3_stack import S3Stack
from web_portal_stack import WebPortalStack

app = core.App()

# Define the S3 bucket to use for pipeline input/output
pipeline_bucket_name = 'my-pipeline-bucket'
pipeline_bucket = core.Bucket(
    app, 'PipelineBucket',
    bucket_name=pipeline_bucket_name,
    removal_policy=core.RemovalPolicy.DESTROY
)

# Define the S3 bucket to use for the web portal
web_portal_bucket_name = 'my-web-portal-bucket'
web_portal_bucket = core.Bucket(
    app, 'WebPortalBucket',
    bucket_name=web_portal_bucket_name,
    removal_policy=core.RemovalPolicy.DESTROY
)

# Define the Athena database name
athena_database_name = 'my_athena_database'

# Deploy the CDK stacks
data_mgmt_stack = DataMgmtStack(
    app, 'DataMgmtStack',
    pipeline_bucket=pipeline_bucket,
    athena_database_name=athena_database_name
)

pipeline_stack = PipelineStack(
    app, 'PipelineStack',
    pipeline_bucket=pipeline_bucket,
    athena_database_name=athena_database_name
)

s3_stack = S3Stack(
    app, 'S3Stack',
    pipeline_bucket=pipeline_bucket,
    web_portal_bucket=web_portal_bucket
)

web_portal_stack = WebPortalStack(
    app, 'WebPortalStack',
    web_portal_bucket=web_portal_bucket,
    athena_database_name=athena_database_name
)

app.synth()


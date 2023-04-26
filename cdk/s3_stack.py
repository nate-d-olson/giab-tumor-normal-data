from aws_cdk import (
    core,
    aws_s3 as s3
)


class OutputBucketStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the S3 bucket to store the output files
        output_bucket = s3.Bucket(
            self, 'OutputBucket',
            removal_policy=core.RemovalPolicy.DESTROY
        )

        # Add a bucket policy to allow read access from the Athena service principal
        output_bucket.add_to_resource_policy(
            statement=iam.PolicyStatement(
                actions=['s3:GetObject'],
                principals=[iam.ServicePrincipal('athena.amazonaws.com')],
                resources=[output_bucket.arn_for_objects('*')]
            )
        )

        # Output the bucket name and ARN
        core.CfnOutput(
            self, 'OutputBucketName',
            value=output_bucket.bucket_name
        )

        core.CfnOutput(
            self, 'OutputBucketArn',
            value=output_bucket.bucket_arn
        )


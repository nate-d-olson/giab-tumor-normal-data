from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_iam as iam,
    aws_stepfunctions as stepfunctions,
    aws_stepfunctions_tasks as tasks,
)
import os


class PipelineStack(core.Stack):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        fastq_pipeline_definition: str,
        alignment_pipeline_definition: str,
        variant_pipeline_definition: str,
        genome_assembly_pipeline_definition: str,
        output_bucket: s3.Bucket,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a Step Functions state machine for running the fastq pipeline
        fastq_pipeline = stepfunctions.StateMachine(
            self, 'FastqPipeline',
            definition=self.create_pipeline_definition(fastq_pipeline_definition, output_bucket),
            timeout=core.Duration.minutes(30)
        )

        # Create a Step Functions state machine for running the alignment pipeline
        alignment_pipeline = stepfunctions.StateMachine(
            self, 'AlignmentPipeline',
            definition=self.create_pipeline_definition(alignment_pipeline_definition, output_bucket),
            timeout=core.Duration.minutes(30)
        )

        # Create a Step Functions state machine for running the variant pipeline
        variant_pipeline = stepfunctions.StateMachine(
            self, 'VariantPipeline',
            definition=self.create_pipeline_definition(variant_pipeline_definition, output_bucket),
            timeout=core.Duration.minutes(30)
        )

        # Create a Step Functions state machine for running the genome assembly pipeline
        genome_assembly_pipeline = stepfunctions.StateMachine(
            self, 'GenomeAssemblyPipeline',
            definition=self.create_pipeline_definition(genome_assembly_pipeline_definition, output_bucket),
            timeout=core.Duration.minutes(30)
        )

        # Grant permissions to the Step Functions state machines to read from and write to the output bucket
        output_bucket.grant_read_write(fastq_pipeline)
        output_bucket.grant_read_write(alignment_pipeline)
        output_bucket.grant_read_write(variant_pipeline)
        output_bucket.grant_read_write(genome_assembly_pipeline)

    def create_pipeline_definition(self, pipeline_definition_file, output_bucket):
        # Define the pipeline definition
        definition = tasks.SnsPublish(
            self, 'PublishTaskToSNS',
            topic=topic,
            message=tasks.SfnToJson(
                task=stepfunctions_tasks.EcsRunTask(
                    self, 'RunNextflow',
                    integration_pattern=stepfunctions.ServiceIntegrationPattern.RUN_JOB,
                    cluster=self.ecs_cluster,
                    task_definition=self.nextflow_task_definition,
                    launch_target=stepfunctions.EcsFargateLaunchTarget(),
                    container_overrides={
                        'command': [
                            '/bin/bash',
                            '-c',
                            f"nextflow run {pipeline_definition_file} --output {output_bucket.bucket_name}"
                        ],
                        'environment': [
                            {
                                'name': 'AWS_REGION',
                                'value': self.region
                            }
                        ]
                    },
                )
            ),
        )

        return definition

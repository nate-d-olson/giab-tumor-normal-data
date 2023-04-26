from aws_cdk import (
    core,
    aws_athena as athena,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_iam as iam,
    aws_stepfunctions as stepfunctions,
    aws_stepfunctions_tasks as tasks,
)
import os


class DatabaseStack(core.Stack):
    def __init__(
        self,
        scope: core.Construct,
        id: str,
        output_bucket: s3.Bucket,
        fastq_results_bucket: s3.Bucket,
        alignment_results_bucket: s3.Bucket,
        variant_results_bucket: s3.Bucket,
        genome_assembly_results_bucket: s3.Bucket,
        metadata_database_name: str,
        **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the Athena database for the metadata
        metadata_database = athena.CfnDatabase(
            self, 'MetadataDatabase',
            database_input={
                'name': metadata_database_name
            }
        )

        # Create the Athena tables for the different data types
        self.create_athena_table(fastq_results_bucket, metadata_database)
        self.create_athena_table(alignment_results_bucket, metadata_database)
        self.create_athena_table(variant_results_bucket, metadata_database)
        self.create_athena_table(genome_assembly_results_bucket, metadata_database)

    def create_athena_table(self, results_bucket, metadata_database):
        # Create the Athena table for the specified results bucket
        table = athena.CfnTable(
            self, f'{results_bucket.bucket_name}Table',
            database_name=metadata_database.database_name,
            table_input={
                'name': f'{results_bucket.bucket_name}Table',
                'parameters': {
                    'classification': 'parquet'
                },
                'storage_descriptor': {
                    'location': f's3://{results_bucket.bucket_name}/',
                    'input_format': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat',
                    'output_format': 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat',
                    'compressed': False,
                    'stored_as_sub_directories': False,
                    'columns': [
                        {
                            'name': 'file_path',
                            'type': 'string'
                        },
                        {
                            'name': 'sample_id',
                            'type': 'string'
                        },
                        {
                            'name': 'file_type',
                            'type': 'string'
                        },
                        {
                            'name': 'run_id',
                            'type': 'string'
                        },
                        {
                            'name': 'read_num',
                            'type': 'string'
                        },
                        {
                            'name': 'fastq_stats',
                            'type': 'struct<basic_statistics:struct<>, per_base_sequence_quality:array<struct<>>, 
per_tile_sequence_quality:array<struct<>>, per_sequence_quality_scores:array<struct<>>, per_base_sequence_content:array<struct<>>, 
per_sequence_gc_content:array<struct<>>, per_base_n_content:array<struct<>>, sequence_length_distribution:array<struct<>>, 
sequence_duplication_levels:array<struct<>>, overrepresented_sequences:array<struct<>>, adapter_content:array<struct<>>, 
kmer_content:array<struct<>>>'
                        }
                    ],
                    'output_compression': 'org.apache.hadoop.io.compress.SnappyCodec',
                },
                'table_type': 'EXTERNAL_TABLE',
                'parameters': {
                    'classification': 'parquet'
                }
            }
       


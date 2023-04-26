import boto3
import pandas as pd

# Set up a boto3 Athena client
client = boto3.client('athena')

# Set up the S3 bucket and folder where the output data is stored
bucket = 'your-bucket-name'
folder = 'your-folder-name'

# Set up the name of the database to create or use
database = 'your-database-name'

# Set up the name of the metadata table to create or use
metadata_table = 'metadata'

# Set up the name of the data table to create or use
data_table = 'data'

# Set up the metadata file paths
fastq_metadata_file = 'fastq_metadata.csv'
bam_metadata_file = 'bam_metadata.csv'
vcf_metadata_file = 'vcf_metadata.csv'
fasta_metadata_file = 'fasta_metadata.csv'

# Set up the data file paths
fastqc_reports_folder = 'fastqc_reports'
samtools_stats_folder = 'samtools_stats'
bcftools_stats_folder = 'bcftools_stats'
quast_reports_folder = 'quast_reports'

# Set up the Athena queries to create the metadata and data tables
metadata_query = f"""
CREATE EXTERNAL TABLE IF NOT EXISTS {metadata_table} (
    sample_id STRING,
    file_type STRING,
    file_name STRING,
    file_path STRING,
    metadata_file_path STRING
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
LOCATION 's3://{bucket}/{folder}/metadata/'
"""

data_query = f"""
CREATE EXTERNAL TABLE IF NOT EXISTS {data_table} (
    sample_id STRING,
    file_type STRING,
    file_name STRING,
    file_path STRING,
    summary_stats_file_path STRING
)
PARTITIONED BY (file_type STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
LOCATION 's3://{bucket}/{folder}/data/'
"""

# Create or use the database
try:
    response = client.create_database(
        DatabaseInput={
            'Name': database
        }
    )
except client.exceptions.AlreadyExistsException:
    pass

# Create or use the metadata table
try:
    response = client.start_query_execution(
        QueryString=metadata_query,
        ResultConfiguration={
            'OutputLocation': f's3://{bucket}/{folder}/athena/'
        }
    )
except client.exceptions.InvalidRequestException:
    pass

# Create or use the data table
try:
    response = client.start_query_execution(
        QueryString=data_query,
        ResultConfiguration={
            'OutputLocation': f's3://{bucket}/{folder}/athena/'
        }
    )
except client.exceptions.InvalidRequestException:
    pass

# Compile the metadata into a pandas DataFrame
fastq_metadata = pd.read_csv(f's3://{bucket}/{folder}/metadata/{fastq_metadata_file}')
bam_metadata = pd.read_csv(f's3://{bucket}/{folder}/metadata/{bam_metadata_file}')
vcf_metadata = pd.read_csv(f's3://{bucket}/{folder}/metadata/{vcf_metadata_file}')
fasta_metadata = pd.read_csv(f's3://{bucket}/{folder}/metadata/{fasta_metadata_file}')
metadata = pd.concat([fastq_metadata, bam_metadata, vcf_metadata, fasta_metadata])

# Upload the metadata to the metadata table in Athena
metadata.to_csv(f's3://{bucket}/{folder}/metadata.csv', index=False, header=False)
client.start_query_execution(
    QueryString=f"""
    ALTER TABLE {metadata_table} ADD PARTITION (file_type='metadata') LOCATION 's3://{bucket}/{

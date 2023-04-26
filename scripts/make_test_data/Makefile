SHELL := /bin/bash

# Define the S3 bucket to use for testing
S3_BUCKET = my-test-bucket

# Define the directory to use for generating the test data
TEST_DATA_DIR = test_data

# Define the number of files to generate for each data type
NUM_FASTQ_FILES = 10
NUM_BAM_FILES = 10
NUM_VCF_FILES = 10

# Define the default target to run the entire workflow
all: generate-data upload-data

# Define the target to generate the test data
generate-data: generate-fastq generate-bam generate-vcf

generate-fastq:
	python generate_fastq.py --num-files $(NUM_FASTQ_FILES) --output-dir $(TEST_DATA_DIR)/fastq_files

generate-bam:
	python generate_bam.py --num-files $(NUM_BAM_FILES) --output-dir $(TEST_DATA_DIR)/bam_files

generate-vcf:
	python generate_vcf.py --num-files $(NUM_VCF_FILES) --output-dir $(TEST_DATA_DIR)/vcf_files

# Define the target to upload the test data to the S3 bucket
upload-data:
	aws s3 sync $(TEST_DATA_DIR)/ s3://$(S3_BUCKET)/test_data/


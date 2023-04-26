import os
import random

# Define the number of fastq files to generate
num_files = 10

# Define the number of reads per file
num_reads = 100000

# Define the list of possible read numbers
read_nums = ['1', '2']

# Define the list of possible quality scores
quality_scores = [chr(x) for x in range(33, 74)]

# Create the output directory for the fastq files
output_dir = 'fastq_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate the fastq files
for i in range(num_files):
    # Generate a random sample ID and run ID
    sample_id = f'sample_{i+1}'
    run_id = f'run_{i+1}'

    # Generate the fastq file name
    file_name = f'{sample_id}_{run_id}.fastq'

    # Generate the fastq file contents
    fastq_file = ''
    for j in range(num_reads):
        # Generate a random read sequence and quality score string
        read_seq = ''.join(random.choices(['A', 'C', 'G', 'T'], k=100))
        quality_str = ''.join(random.choices(quality_scores, k=100))

        # Append the read to the fastq file
        fastq_file += f'@read{j+1}/{read_nums[j%2]} {sample_id} {run_id}\n'
        fastq_file += f'{read_seq}\n'
        fastq_file += '+\n'
        fastq_file += f'{quality_str}\n'

    # Write the fastq file to disk
    with open(os.path.join(output_dir, file_name), 'w') as f:
        f.write(fastq_file)


import os
import random

# Define the number of bam files to generate
num_files = 10

# Define the number of reads in the bam file
num_reads = 100000

# Define the list of possible chromosomes
chromosomes = [f'chr{i}' for i in range(1, 23)] + ['chrX', 'chrY']

# Define the list of possible mapping qualities
mapping_qualities = [random.randint(0, 60) for i in range(num_reads)]

# Define the list of possible reference positions
ref_positions = [random.randint(1, 1000000) for i in range(num_reads)]

# Create the output directory for the bam files
output_dir = 'alignment_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate the bam files
for i in range(num_files):
    # Generate a random sample ID and run ID
    sample_id = f'sample_{i+1}'
    run_id = f'run_{i+1}'

    # Generate the bam file name
    file_name = f'{sample_id}_{run_id}.bam'

    # Generate the bam file contents
    bam_file = ''
    for j in range(num_reads):
        # Generate a random chromosome and reference position
        chromosome = random.choice(chromosomes)
        ref_pos = ref_positions[j]

        # Append the read to the bam file
        bam_file += f'{chromosome}\t{ref_pos}\t.\tA\t.\t.\t.\t.\t.\t{sample_id}\t{run_id}\t{mapping_qualities[j]}\n'

    # Write the bam file to disk
   


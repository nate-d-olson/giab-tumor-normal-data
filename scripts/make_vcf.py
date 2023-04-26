import os
import random

# Define the number of VCF files to generate
num_files = 10

# Define the number of variants per file
num_variants = 1000

# Define the list of possible chromosomes
chromosomes = [f'chr{i}' for i in range(1, 23)] + ['chrX', 'chrY']

# Define the list of possible reference bases
ref_bases = ['A', 'C', 'G', 'T']

# Define the list of possible alternate bases
alt_bases = ['A', 'C', 'G', 'T']

# Create the output directory for the VCF files
output_dir = 'vcf_files'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate the VCF files
for i in range(num_files):
    # Generate a random sample ID and run ID
    sample_id = f'sample_{i+1}'
    run_id = f'run_{i+1}'

    # Generate the VCF file name
    file_name = f'{sample_id}_{run_id}.vcf'

    # Generate the VCF file header
    vcf_header = '##fileformat=VCFv4.3\n'
    vcf_header += f'##SAMPLE=<ID={sample_id},Run={run_id}>\n'
    vcf_header += '#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n'

    # Generate the VCF file contents
    vcf_file = vcf_header
    for j in range(num_variants):
        # Generate a random chromosome and position
        chromosome = random.choice(chromosomes)
        position = random.randint(1, 1000000)

        # Generate a random reference base and alternate base
        ref_base = random.choice(ref_bases)
        alt_base = random.choice(alt_bases)

        # Append the variant to the VCF file
        vcf_file += f'{chromosome}\t{position}\t.\t{ref_base}\t{alt_base}\t.\t.\t.\n'

    # Write the VCF file to disk
    with open(os.path.join(output_dir, file_name), 'w') as f:
        f.write(vcf_file)


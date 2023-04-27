import os
import random

# Define the genome size
genome_size = 1000000

# Define the list of possible nucleotides
nucleotides = ['A', 'C', 'G', 'T']

# Create the output directory for the genome assembly
output_dir = 'genome_assembly'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate the genome assembly
genome_file = ''
for i in range(genome_size):
    # Generate a random nucleotide and append it to the genome
    nucleotide = random.choice(nucleotides)
    genome_file += nucleotide

    # Add a newline character every 60 nucleotides for readability
    if i % 60 == 59:
        genome_file += '\n'

# Write the genome assembly to disk
with open(os.path.join(output_dir, 'genome.fasta'), 'w') as f:
    f.write(f'>genome\n{genome_file}\n')


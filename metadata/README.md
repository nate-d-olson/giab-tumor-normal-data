# Proposed metadata schema for the project
To facilitate the generation, collection, and collating metadata for this project 
we have provided a proposed the following metadata schema for the sample, data files,
and qa/qc metrics.

Please provide feedback on this schema either by creating a github issue, a pull request
or emailing Nate Olson at nolson@nist.gov

## Proposed sample and analysis file metadata schema
Here are some suggested metadata fields for the samples and analysis file types
### Sample Metadata
- Sample ID: Unique identifier for the sample
- Sample type: DNA or RNA
- Tumor cell line: Name or identifier of the tumor cell line
- Institution: Name of the institution that prepared and sequenced the sample
- Contact person: Name and email of the person responsible for the sample

### Sequencing Technology Metadata
- Sequencing platform: Name of the sequencing platform used (e.g., Illumina, PacBio, Oxford Nanopore)
- Sequencing technology: Type of sequencing technology employed (e.g., short-read, long-read, linked-read)
- Sequencing kit: Name and version of the sequencing kit used
- Sequencing library preparation: Library preparation method and kit used
- Read length: Read length of the sequencing run

### Basecall Metadata (FASTQ files)
- File name: Name of the FASTQ file
- Read type: Paired-end or single-end
- Read direction: Forward or reverse (for paired-end data)
- File format: FASTQ file format version
- File size: Size of the FASTQ file

### Alignment Metadata (BAM files)
- File name: Name of the BAM file
- Reference genome: Name and version of the reference genome used for alignment
- Alignment tool: Name and version of the alignment software used
- Alignment parameters: Parameters used in the alignment process
- File format: BAM file format version
- File size: Size of the BAM file

### Variant Call Metadata (VCF files)
- File name: Name of the VCF file
- Variant caller: Name and version of the variant calling software used
- Variant calling parameters: Parameters used in the variant calling process
- Genomic regions: Targeted or whole-genome sequencing
- File format: VCF file format version
- File size: Size of the VCF file

### Genome Assembly Metadata (FASTA files)
- File name: Name of the FASTA file
- Assembly method: Name and version of the genome assembly software used
- Assembly parameters: Parameters used in the genome assembly process
- Assembly type: De novo, reference-guided, or hybrid
- File format: FASTA file format version
- File size: Size of the FASTA file

# Proposed QA/QC Metadata Schema 
Summary statistics and quality control metrics are essential for assessing the 
quality and reliability of the generated data. Here is a list of suggested 
summary statistics and quality control metrics for the different data types 
in your project:

### Raw Sequencing Data (FASTQ files)
- Total number of reads
- Average read length
- Read length distribution
- Base quality distribution
- GC content distribution
- Adapter content
- Overrepresented sequences
- Ambiguous base call (N) content
- Duplicate read rate

### Alignment Data (BAM files)
- Total number of aligned reads
- Alignment rate (percentage of aligned reads)
- Mean mapping quality
- Distribution of mapping quality scores
- Coverage depth and uniformity
- Percentage of bases covered at different depths (e.g., 1x, 10x, 20x, etc.)
- Insert size distribution (for paired-end data)
- Chimeric read pairs rate (for paired-end data)
- Duplicate read rate
- Mismatch rate and distribution
- Indel rate and distribution
- Strand balance

### Variant Calls (VCF files)
- Total number of called variants (SNVs, InDels, and others)
- Transition/Transversion (Ti/Tv) ratio
- Variant allele frequency distribution
- Variant quality distribution
- Genotype quality distribution
- Depth distribution of called variants
- Homozygous/heterozygous variant ratio
- Functional annotation of variants (e.g., synonymous, non-synonymous, splice site, etc.)
- Number of variants in coding regions, introns, intergenic regions, etc.
- Known/novel variant ratio (based on existing databases)

## Genome Assemblies (FASTA files)
- Total number of contigs/scaffolds
- Total assembled genome size
- N50, L50, and other assembly statistics
- Longest and shortest contig/scaffold
- Contig/scaffold length distribution
- GC content distribution
- Genome completeness assessment (e.g., BUSCO or other gene content-based metrics)
- Contamination check (e.g., presence of non-target organism sequences)


Proposed data management workflow for GIAB tumor sample.
This is a work in progress. Most of the files were initially generated by chatGPT with promots from ND Olson. 
Feel free to explore this repository and provide feedback but know that most of the scripts are raw chatGPT and will require significant revisions for use.

# Project Overview
The aim of this project is to characterize genomic variants in a batch of 
reference material DNA and RNA obtained from a tumor cell line. The project 
involves multiple institutions utilizing different sequencing technologies. 
The generated data will be made publicly available via an FTP server, where 
collaborators can access it to generate variant call sets and genome 
assemblies. These variant call sets and genome assemblies will be used for 
downstream analysis and reference characterizations.

# Project Data Management Workflow

This README provides an overview of the data management workflow for the project
characterizing genomic variants in reference material DNA and RNA. The workflow
describes how data will be organized, shared, evaluated, and preserved throughout
the project.

# Proposed Data Management Workflow Diagram
```mermaid
graph TD
  A[Data generators] --> B[Upload data to FTP]
  B --> C[Execute fastq pipeline]
  C --> D[Execute BAM pipeline]
  D --> E[Execute VCF pipeline]
  E --> F[Execute genome assembly pipeline]
  F --> G[Combine pipeline output]
  G --> H[Load metadata into Athena]
  A --> H(Metadata collection)
  C --> H(Metadata collection)
  D --> H(Metadata collection)
  E --> H(Metadata collection)
  F --> H(Metadata collection)
  H --> I[Deploy web portal]
```

# Directory structure for this data management workflow
```
project/
├── data/
│   ├── fastq_files/
│   ├── alignment_files/
│   ├── variant_call_sets/
│   ├── genome_assemblies/
│   └── metadata/
├── scripts/
│   ├── generate_fastq.py
│   ├── generate_bam.py
│   ├── generate_vcf.py
│   ├── generate_genome_assembly.py
│   └── collect_metadata.py
├── pipelines/
│   ├── fastq_pipeline.nf
│   ├── bam_pipeline.nf
│   ├── vcf_pipeline.nf
│   └── genome_assembly_pipeline.nf
├── web_portal/
│   ├── index.html
│   ├── style.css
│   └── main.js
├── cdk/
│   ├── app.py
│   ├── data_mgmt_stack.py
│   ├── pipeline_stack.py
│   ├── s3_stack.py
│   └── web_portal_stack.py
├── README.md
├── LICENSE
└── requirements.txt
```


## Proposed Data Organization and Naming Conventions

The data may be organized in the following directory structure on the FTP server:

```
project_root/
│
├── README.md
├── metadata/
│   ├── sample_metadata.tsv
│   └── sequencing_technology_metadata.tsv
│
├── raw_data/
│   ├── institution_1/
│   │   ├── dna_sequencing/
│   │   │   ├── sample_1_1.fastq.gz
│   │   │   └── sample_1_2.fastq.gz
│   │   └── rna_sequencing/
│   │       ├── sample_1_1.fastq.gz
│   │       └── sample_1_2.fastq.gz
│   └── institution_2/
│       ├── dna_sequencing/
│       │   ├── sample_2_1.fastq.gz
│       │   └── sample_2_2.fastq.gz
│       └── rna_sequencing/
│           ├── sample_2_1.fastq.gz
│           └── sample_2_2.fastq.gz
│
├── processed_data/
│   ├── alignments/
│   │   ├── institution_1/
│   │   │   ├── sample_1.bam
│   │   │   └── sample_1.bam.bai
│   │   └── institution_2/
│   │       ├── sample_2.bam
│   │       └── sample_2.bam.bai
│   ├── variant_calls/
│   │   ├── institution_1/
│   │   │   ├── sample_1.vcf.gz
│   │   │   └── sample_1.vcf.gz.tbi
│   │   └── institution_2/
│   │       ├── sample_2.vcf.gz
│   │       └── sample_2.vcf.gz.tbi
│   └── genome_assemblies/
│       ├── institution_1/
│       │   └── sample_1.fasta.gz
│       └── institution_2/
│           └── sample_2.fasta.gz
│
└── analysis/
    ├── reference_characterization/
    │   ├── internal_evaluation/
    │   │   ├── comparison_results.tsv
    │   │   └── discrepancy_report.txt
    │   └── external_evaluation/
    │       ├── orthogonal_comparison_results.tsv
    │       └── manual_curation_report.txt
    └── downstream_analysis/
        ├── analysis_1/
        │   ├── input_data/
        │   ├── scripts/
        │   └── results/
        └── analysis_2/
            ├── input_data/
            ├── scripts/
            └── results/
```

__File Naming Convention:__

Raw data: `sample_[sample_number]_[read_pair].fastq.gz`
Example: `sample_1_1.fastq.gz`

Variant call files: `sample_[sample_number].vcf.gz and sample_[sample_number].vcf.gz.tbi`
Example: `sample_1.vcf.gz`

Genome assembly files: `sample_[sample_number].fasta.gz`
Example: `sample_1.fasta.gz`

Analysis and evaluation files: descriptive file names with appropriate file extensions, such as .tsv, .txt, or .csv
Example: `comparison_results.tsv`

Alignment files: `sample_[sample_number].bam` and `sample_[sample_number].bam.bai`
Example: `sample_1.bam`

The naming convention uses a combination of sample identifiers, sequencing 
technology or analysis type, and file format extensions to clearly and 
consistently label files.

## Data Sharing

The following types of data will be shared via the FTP server:

1. Raw Data: Raw sequencing data (FASTQ files) generated from different sequencing
   technologies will be stored in separate directories labeled with relevant metadata.

2. Variant Call Sets and Genome Assemblies: Collaboratively generated variant call
   sets (VCF files) and genome assemblies (FASTA files) will be uploaded to the FTP
   server. Each file will include appropriate metadata and versioning information.

## Quality Control

1. Internal Evaluation: The project team will internally evaluate the reference
   characterizations. This will involve assessing the quality of variant call sets
   and genome assemblies, comparing results across sequencing technologies, and
   verifying consistency with expected findings.

2. External Evaluation: External collaborators will generate orthogonal variant call
   sets for comparison with the reference characterizations. Discrepancies will be
   manually curated using a genome viewer (e.g., IGV) to ensure accuracy.

## Long-Term Preservation

1. Data Backup: Regular backups of the FTP server will be performed to ensure data
   integrity and availability. Multiple copies of the data will be stored on separate
   storage systems.

2. Version Control: The FTP server will employ version control mechanisms to track
   changes in the data, ensuring traceability and reproducibility.

3. Persistent Identifiers: Data files, including variant call sets and genome
   assemblies, will be assigned persistent identifiers (e.g., DOIs or DataCite) for
   long-term discoverability and accessibility.

## Data Access and Collaboration

1. Collaboration Agreement: Collaborators accessing the data on the FTP server will
   be required to sign a collaboration agreement or data access agreement outlining
   the terms of data usage, including proper citation, data handling, and publication
   policies.

2. Access Control: The FTP server will implement access controls to restrict data
   access to authorized collaborators based on project roles and responsibilities.

3. Collaboration Platform: A dedicated collaboration platform will be used to facilitate
   effective communication, data sharing, and coordination among project members and
   collaborators.

## Ethical Considerations and Data Privacy

1. Ethical Compliance: The project will adhere to relevant ethical guidelines,
   regulations, and institutional policies regarding the handling, storage, and sharing
   of genomic data.

2. Anonymization: Personal identifiers will be removed or de-identified from the data
   to protect patient privacy and comply with data protection regulations.

3. Informed Consent: If applicable, appropriate informed consent will be obtained from
   the individuals involved in providing the reference material DNA and RNA.

For more detailed information, please refer to the full Data Management Plan (DMP).


## Proposed Data Management workflow CI/CD framework
A CI/CD framework for this data management workflow, will help ensure 
that changes to the source code are thoroughly tested and deployed in a controlled 
and repeatable manner, reducing the risk of errors and improving the reliability of the workflow.

1. Source code repository: A Git repository to store the code for the data management workflow, including the CDK stacks, Python scripts, web portal, and any other components.

1. Code review: A code review process to ensure that changes to the source code are reviewed and approved by one or more team members before they are merged into the main branch.

1. Continuous integration: A CI process to automatically build and test the source code whenever changes are pushed to the repository. This could include running unit tests, linting the code, and building the Docker images for the different pipelines.

1. Artifact repository: A repository to store the artifacts generated by the CI process, such as the Docker images, Nextflow config files, and other artifacts.

1. Continuous deployment: A CD process to automatically deploy the changes to a development or staging environment for testing. This could involve deploying the CDK stacks using the AWS CLI or CDK CLI, running the Nextflow pipelines on a cloud-based cluster, and deploying the web portal to a cloud-based hosting service.

1. Automated testing: Automated tests to verify that the deployment was successful and that the data management workflow is working as expected. This could include testing the Nextflow pipelines using test data, testing the web portal using automated UI tests, and testing the Athena queries using automated SQL queries.

1. Manual testing: Manual testing to verify that the data management workflow is working correctly and meets the requirements. This could involve manual testing of the Nextflow pipelines, manual testing of the web portal, and manual testing of the Athena queries.

1. Production deployment: A production deployment process to deploy the data management workflow to a production environment after it has been tested and approved. This could involve deploying the CDK stacks, running the Nextflow pipelines, and deploying the web portal to a production hosting service.


## TODO 
- Add reference to currently available data https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/technical/MGH3066_TumorNormal/
- Revise filenaming conventions - currently too simplistic and not informative
- get feedback on metadata schema
- Create dev environment for this workflow
- Potentially break project up into multiple repositories: nextflow pipelines, cdn stack, metadata management, and test data generation.
- Impliment ci/cd framework

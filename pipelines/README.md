
Data Management Workflow Diagram

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


Directory structure for tumor sample data management workflow
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

TODO 
- Add schema check for metadata json
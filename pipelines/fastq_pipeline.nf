#!/usr/bin/env nextflow

params.input_dir = './input_data'
params.output_dir = './output_data'

Channel
    .fromPath("${params.input_dir}/**/*.fastq.gz", maxDepth: 1)
    .ifEmpty { error("No FASTQ files found in ${params.input_dir}.") }
    .into { fastq_files }

process fastqc {
    tag { "FastQC for sample: ${sample_id}" }
    publishDir "${params.output_dir}/fastqc_reports", mode: 'copy', pattern: '*.html'

    input:
    path(fastq_file) from fastq_files

    output:
    path("*.html") into fastqc_reports

    script:
    def sample_id = fastq_file.baseName.replaceAll(/(_R1|_R2)/, '')
    """
    fastqc -q $fastq_file -o .
    """
}

fastqc_reports.subscribe { println "Generated FastQC report: ${it}" }

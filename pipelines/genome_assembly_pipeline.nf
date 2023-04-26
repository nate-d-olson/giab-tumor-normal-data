#!/usr/bin/env nextflow

params.input_dir = './input_data'
params.output_dir = './output_data'

Channel
    .fromPath("${params.input_dir}/**/*.fasta", maxDepth: 1)
    .ifEmpty { error("No FASTA files found in ${params.input_dir}.") }
    .into { fasta_files }

process quast {
    tag { "QUAST for assembly: ${assembly_id}" }
    publishDir "${params.output_dir}/quast_reports", mode: 'copy', pattern: '*/report.txt'

    input:
    path(fasta_file) from fasta_files

    output:
    path("*/report.txt") into quast_reports

    script:
    def assembly_id = fasta_file.baseName
    """
    quast -o ${assembly_id}_quast_report $fasta_file
    """
}

quast_reports.subscribe { println "Generated QUAST report: ${it}" }

#!/usr/bin/env nextflow

params.input_dir = './input_data'
params.output_dir = './output_data'

Channel
    .fromPath("${params.input_dir}/**/*.vcf.gz", maxDepth: 1)
    .ifEmpty { error("No VCF files found in ${params.input_dir}.") }
    .into { vcf_files }

process bcftools_stats {
    tag { "BCFtools stats for sample: ${sample_id}" }
    publishDir "${params.output_dir}/bcftools_stats", mode: 'copy', pattern: '*.stats'

    input:
    path(vcf_file) from vcf_files

    output:
    path("*.stats") into bcftools_stats_files

    script:
    def sample_id = vcf_file.baseName
    """
    bcftools index $vcf_file
    bcftools stats $vcf_file > ${sample_id}.stats
    """
}

bcftools_stats_files.subscribe { println "Generated BCFtools stats report: ${it}" }

#!/usr/bin/env bash

# Tools:
#	samtools (v. 1.13)
#	Qualimap (v. 2.2.2)

# This script runs 1) samtools sort and 2) qualimap bamqc, starting with the
#   minimap2 results file (*.sam) as input. Output files are a bam file and
#   qualimap output.

# Input should be the directory name, i.e. sample name and barcode.

# Usage:
#  ./sam_quali_pipe.sh [SAM_FILE_DIR_NAME]

INPUT=$1

samtools sort -O BAM -o $INPUT/${INPUT}_pacbio.bam $INPUT/${INPUT}_pacbio.sam
samtools view -bt ../../../Pf3D7_08_v3_HRP2_ann_v1_extraction_060121.fasta.fai -q 30 -o $INPUT/${INPUT}_pacbio_mq30.bam $INPUT/${INPUT}_pacbio.bam
qualimap bamqc -bam $INPUT/${INPUT}_pacbio_mq30.bam
qualimap bamqc -bam $INPUT/${INPUT}_pacbio.bam

gzip $INPUT/${INPUT}_pacbio.sam

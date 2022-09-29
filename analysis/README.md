# Analysis

This folder contains scripts and Jupyter notebooks used to analyze MinION sequencing data following basecalling and barcoding with MinKnow (Oxford Nanopore Technologies), as performed during sequencing.

- *alignment* with minimap2
	- *alignment cleanup and assessment* with samtools and Qualimap
- *de novo assembly* with canu
- figure generation and *coverage threshold calculations* with python
	- MinION sequencing summary files used to generate figures are available on Zenodo (https://zenodo.org/record/6780399)
- *repeat typing* with python
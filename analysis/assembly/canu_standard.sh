#! /usr/bin/env bash

# canu v. 2.1.1

# Basic canu script for pfhrp2 assembly

OUTPRE=$1
OUTDIR=$2
INPUT=$3

canu -p $OUTPRE -d $OUTDIR genomeSize=1.3k -nanopore $INPUT

#!/usr/bin/env bash

# minimap2 v. 2.21-r1071

# Basic minimap2 script for aligning nanopore sequenced data to pfhrp2 reference sequences

REF=$1
INPUT=$2
OUTPUT=$3

minimap2 -ax map-ont --secondary=no --sam-hit-only $REF $INPUT > $OUTPUT

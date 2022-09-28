#!/usr/bin/env bash

# Basic minimap2 script for aligning nanopore sequenced data to pfhrp2 reference sequences

REF=$1
INPUT=$2
OUTPUT=$3

minimap2 -ax map-pb --sam-hit-only $REF $INPUT > $OUTPUT

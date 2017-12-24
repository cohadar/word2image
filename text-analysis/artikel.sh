#!/bin/bash
./german_stream.sh | tr ' ' '\n' | sed -E '/^ *$/d'| sed -E '/^.$/d' | sed -E '/.*[\].*/d' | sort -u | python3 count-curr.py dewiki-20170920-pages-articles.freq.tsv

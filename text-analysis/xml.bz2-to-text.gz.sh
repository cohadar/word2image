#!/bin/bash
if ! [[ "$1" =~ .xml.bz2$ ]]; then
	echo "you must specify wikipedia xml.bz2 archive"
	exit 1
fi
name=${1%.xml.bz2}
bzcat "${name}.xml.bz2" | ./wiki_xml_filter.pl | awk 'length($0)>=100' | ./german_stream.sh | gzip > "${name}.text.gz"

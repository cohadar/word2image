#!/bin/bash
set -e
if ! [[ "$1" =~ .text.gz$ ]]; then
	echo "you must specify .text.gz file"
	exit 1
fi
name=${1%.text.gz}
# split each word on new line
# remove blank lines: ' ', '   '
# remove single char words: 'a', 'f'
# remove uppercased words: 'MCMLX', 'VII', 'APFEL'
gzcat "${name}.text.gz" |
	tr ' ' '\n' |
	sed -E '/^ *$/d' |
	sed -E '/^.$/d' |
	sed -E '/^[[:upper:]]+$/d' |
	gzip > "${name}.words.gz"

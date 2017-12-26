#!/bin/bash
if [[ -s "verben/$1.html" ]]; then
	exit 0
fi
wget https://www.verbformen.de/konjugation/?w="$1" -O "verben/$1.html"
sleep 10

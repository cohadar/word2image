#!/bin/bash
printf "$1\t"
wget https://www.verbformen.de/konjugation/?w="$1" -O- | grep 'meta.*Konjugation des Verbs' | sed -E 's/^.*Konjugation des Verbs (.*) usw[.].*$/\1/'
sleep 1

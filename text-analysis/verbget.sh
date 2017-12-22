#!/bin/bash
wget https://www.verbformen.de/konjugation/?w="$1" -O "verben/$1.html"
sleep 1

#!/bin/bash
printf "$1\t"
dict -d fd-deu-eng "$1" | grep -E '^   .*' | tr '\n' ';' | tr -s ' ' | sed -E 's/^ (.*)$/\1/' | sed -E 's/^(.*);$/\1/'
printf "\n"

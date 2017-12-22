#!/bin/bash
dict -Cd fd-deu-eng "$1" | grep -E '^   .*' | tr '\n' ';' | tr -s ' ' | sed -E 's/^ (.*)$/\1/' | sed -E 's/^(.*);$/\1/'

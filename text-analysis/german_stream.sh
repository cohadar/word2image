#!/bin/sh
# everything except german alphabet letters gets translated to spaces.
# start and end whitespaces are trimmed and midlle ones reducet to one space.
sed 's/[^a-zA-ZäÄöÖüÜß\n]/ /g' |
sed 's/^ *//' |
sed 's/ *$//' |
tr -s ' '

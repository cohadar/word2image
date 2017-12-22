#!/bin/bash
res=$(./translate_one.sh "$1")
if [[ "$res" ]]; then
	printf "$1\t$res\n"
	exit 0
fi
if [ ${#1} -le 3 ]; then exit 0; fi
res=$(./translate_one.sh "${1%?}")
if [[ "$res" ]]; then
	printf "$1\t${1%?}?: $res\n"
	exit 0
fi
if [ ${#1} -le 4 ]; then exit 0; fi
res=$(./translate_one.sh "${1%??}")
if [[ "$res" ]]; then
	printf "$1\t${1%??}??: $res\n"
	exit 0
fi
if [ ${#1} -le 5 ]; then exit 0; fi
res=$(./translate_one.sh "${1%???}")
if [[ "$res" ]]; then
	printf "$1\t${1%???}???: $res\n"
	exit 0
fi
printf "$1\t\n"

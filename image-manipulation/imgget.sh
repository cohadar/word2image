#!/bin/bash
if [[ -s "images/$1.base64" ]]; then
	exit 0
fi
python3 get-image-base64.py "$1" 4 > "images/$1.base64"
echo "images/$1.base64"
sleep 5

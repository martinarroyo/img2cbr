#!/bin/bash
# Adds all directories in the folder to cbr files
for dir in */;do
if [ -d "$dir" ]
then
	python ../img2cbr.py "$dir" "$@"
fi
done

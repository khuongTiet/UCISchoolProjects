#!/bin/sh

# Check that the user only passes in one argument to validate
if [ "$#" -ne 1 ]; then
	echo "valid can only take one argument"
else
	if grep -Eq ^[a-zA-Z_][a-zA-Z0-9_]*$ <<< "$1"; then # check argument against regex and ignore the output of grep
		echo "Yes"
	else
		echo "No"
	fi
fi

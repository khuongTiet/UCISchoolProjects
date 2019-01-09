#!/bin/bash
# unrm
# Restores the specified file(s) within the TRASH directory into the current directory of where this script was called

# Check to make sure that TRASH environment variable has been set
if [[ -z "${TRASH}" ]]; then
	echo "unrm: Environment error -- Environment variable TRASH not set"
else
	# Ensures that TRASH points to a directory before executing the command
	if [[ -d ${TRASH} ]]; then
		for file in "$@"
		do
			# Restores file by moving the specified file name from the TRASH directory
			# back into the current working directory
			echo "Restoring $file from the $TRASH"
			mv $TRASH/$file ./$file
		done
	else
		echo "unrm: Environment error -- TRASH must be a directory"
		exit 1
fi

#!/bin/bash
# trash
# Simple shell script that removes from disk all of the files that are currently inside the TRASH directory

# Check to see if the TRASH variable has been set
if [[ -z "${TRASH}" ]]; then
	echo "trash: Environment error -- Environment variable TRASH must be set"
else
	# Check that there are no arguments passed into trash
	# if there are any, exit the script
	if [ ! "$#" == "0" ]; then
		echo "trash: Execution error - trash does not take any arguments"
		exit 1
	fi
	# Ensures that the TRASH variable points to a directory before performing the command
	if [[ -d ${TRASH} ]]; then
		# call rm with -r and -f options to delete any and everything within the TRASH directory without and interruptions
		rm -rf $TRASH/*		
	else
		echo "trash: Environment error -- TRASH must be a directory"
		exit 1
	fi
fi

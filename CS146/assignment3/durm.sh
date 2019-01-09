#!/bin/bash
# durm
# Simple script that displays the disk usage of the trash directory used by the srm suite

# Checks if user has set the environment variable, TRASH
if [[ -z "${TRASH}" ]]; then
	echo "durm: Environment error -- Environment variable TRASH must be set"
	exit 1
else
	# Check that no arguments are passed to durm
	# if there are any, exit the script
	if [ ! "$#" == "0" ]; then
		echo "durm: Execution error -- durm does not take any arguments"
		exit 1
	fi
	# Make sure that TRASH is a directory before executing the command
	if [[ -d ${TRASH} ]]; then
		du $TRASH
	else
		echo "durm: Environment error -- TRASH must be a directory"
		exit 1
	fi
fi

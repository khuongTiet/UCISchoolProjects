#!/bin/bash
# lsrm
# Simple script that displays all the files, using ls -l on each file, in the TRASH directory used by the srm suite.

if [[ -z "${TRASH}" ]]; then
	echo "lsrm: Environment error -- Environment variable TRASH must be set"
	exit 1
else
	# Checks if there are any arguments passed into lsrm
	# if there are any, exit the script
	if [ ! "$#" == "0" ]; then
		echo "lsrm: Execution error -- lsrm does not take any arguments"
		exit 1
	fi
	# Make sure that TRASH is a directory before executing the command
	if [[ -d ${TRASH} ]]; then
		# Iterate over each file within TRASH and call ls -l on it
		for file in $TRASH/*
		do
			ls -l $file
		done
	else
		echo "lsrm: Environment error -- TRASH must be a directory"
		exit 1
	fi
fi

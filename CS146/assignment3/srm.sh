#!/bin/bash
# srm
# Script that safely removes any file(s) passed to it to a trash directory, from which it can be restored or removed from disk

# Checks to make sure that there is a TRASH environment variable defined
if [[ -z "${TRASH}" ]] && [[ ! -d "${TRASH}" ]]; then
	echo "srm: Environment error -- Environment variable TRASH must be set to directory path"
else
	# Ensures that TRASH points to a directory before executing any commands
	if [[ -d ${TRASH} ]]; then
		user_options=""
		while getopts 'fiIrRdv' OPTION; do
			case "$OPTION" in
				?)
					user_options+="$OPTION";;
			esac
		done
		# Checks if there are any options passed to srm; if there are any, then pass them all to rm
		if [[ ! -z $user_options ]]; then
			rm -$user_options
		else
			for file in "$@"
			do
				if [ ! -d $file ]; then
					if [ ! -f $file ]; then
						echo "srm: Execution error -- '$file' is not a valid file or directory"
						exit 1
					fi
				fi
				# Moves files into the specifed TRASH directory
				# Uses -f / --force here to overwrite a file in the TRASH directory if it already exists
				# This prevents the mv command from prompting the user and ensures smooth execution of the command
				echo "Safely removing $file to TRASH directory"
				mv -f $file $TRASH/$file
			done
		fi
	else
		echo "srm: Environment error -- TRASH must be a directory"
		exit 1
	fi
fi

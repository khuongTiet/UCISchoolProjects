#!/bin/sh

# Iterating through each separate command argument
# Using $@ as opposed to $* to get each value separately
for file in "$@"
do
	if [ -f "$file" ] # Check if this is a valid file before giving permissions
	then
		chmod +x "$file"
	else
		>&2 echo "File $file does not exist" # Give usage message if not valid
	fi
done

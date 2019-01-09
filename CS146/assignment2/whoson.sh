#!/bin/sh

# Iterating through each active user on the machine
# Use who piped to cut to take only the first column of who's output and then we
# use sort -u on this to only get unique results.
# who must be used because sort works only on lines and not input on the same line
for user in $(who | cut -f 1 -d " " | sort -u);
do
	if groups $user 2> /dev/null | grep -q ugrad; then # redirect groups: cannot find errors, check if user is part of the ugrad group
		printf "$user " # use printf to avoid newlines that echo produces in order to have a horizontal output
	fi
done
printf "\n" # used to place the command line back at the normal spot


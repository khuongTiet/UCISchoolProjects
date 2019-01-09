#!/bin/sh

# A separate variable to track the current line number is initialized here as well as the printing of the 0th argument, the name of the script
currentLine=1
echo "0: $0"
for input in "$@" # use $@ here instead of $* to get each argument separately in order to deal with possible errors
do
	echo "$currentLine: $input" # use echo instead of printf for simplicity and to make use of the newline that echo produces
	currentLine=$((currentLine += 1)) # increment variable to keep track of the line number
done

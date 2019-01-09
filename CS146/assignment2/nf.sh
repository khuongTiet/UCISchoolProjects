#!/bin/sh
# Another simple script that utilizes the wc command in order to count each separate line
# that is returned from ls in order to effectively count all the files in the current directory
ls | wc -l 

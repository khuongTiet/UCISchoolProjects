#!/bin/sh

# A simple script the utilizes the previous script piped into wc, counting each separate word to give the number of current users that are in the ugrad group
sh ./whoson.sh | wc -w

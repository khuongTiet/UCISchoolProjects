#!/bin/sh

nsh test_pipes.sh > nsh_pipes
sh test_pipes.sh > sh_pipes

if cmp -s "nsh_pipes" "sh_pipes"; then
	echo SAME
else
	echo DIFFERENT
fi

rm -f nsh_pipes
rm -f sh_pipes

#!/bin/sh

# The outputs of this may differ because sh's ls picks up hidden files due to alias
nsh test_cd.sh > nsh_cd
sh test_cd.sh > sh_cd

if cmp -s "nsh_cd" "sh_cd"; then
	echo SAME
else
	echo DIFFERENT
fi

rm -f nsh_cd
rm -f sh_cd

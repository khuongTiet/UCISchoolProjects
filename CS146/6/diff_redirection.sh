#!/bin/sh
nsh test_redirection.sh > nsh_redirect
sh test_redirection.sh > sh_redirect

if cmp -s "nsh_redirect" "sh_redirect"; then
	echo SAME
else
	echo DIFFERENT
fi

rm -f nsh_redirect
rm -f sh_redirect

#!/bin/sh

execute_options=""
temp="/tmp/INTERP_KT"

trap cleanup 0 1 2 3 15

cleanup() {
    rm -rf $temp
}

if [ ! -d $temp ]; then
    mkdir $temp
fi
gcc -o $temp/run "${0}.c"
$temp/run $@

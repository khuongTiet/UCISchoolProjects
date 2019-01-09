default:
	gcc -o nsh main.c parse.c nsh_help.c
	
run:
	gcc -o nsh main.c parse.c nsh_help.c
	nsh
	rm nsh

test_cd:
	gcc -o nsh main.c parse.c nsh_help.c
	diff_cd.sh

test_pipes:
	gcc -o nsh main.c parse.c nsh_help.c
	diff_pipes.sh

test_redirection:
	gcc -o nsh main.c parse.c nsh_help.c
	diff_redirection.sh


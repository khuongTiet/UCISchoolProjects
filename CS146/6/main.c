#include "parse.h"
#include <assert.h>
#include <stdio.h>

#include <sys/wait.h>
#include "nsh_help.h"
/*
** A very simple main program that re-prints the line after it's been scanned and parsed.
*/
int main(int argc, char *argv[])
{
    FILE *input;
    char line[MAX_LINE];

    if(argc == 2)
    {
	input = fopen(argv[1], "r");
	if(input == NULL)
	{
	    perror(argv[1]);
	    exit(1);
	}
    }
    else
    {
	assert(argc == 1);
	input = stdin;
	printf("? ");
	/* By default, printf will not "flush" the output buffer until
	* a newline appears.  Since the prompt does not contain a newline
	* at the end, we have to explicitly flush the output buffer using
	* fflush.
	*/
	fflush(stdout);
    }

    setlinebuf(input);
    while(fgets(line, sizeof(line), input))
    {
	int i;
	struct commandLine cmdLine;

	if(line[strlen(line)-1] == '\n')
	    line[strlen(line)-1] = '\0';   /* zap the newline */

	Parse(line, &cmdLine);

	int parent = getpid();
	if (strcmp(cmdLine.argv[0], "cd") == 0) {
	    change(cmdLine);
	} else {
	    int status;
	    int child = fork();
	    if (child == 0) {
	        if (cmdLine.numCommands == 0) {
		          ;
	        } else if (cmdLine.numCommands == 1) {
		          single(cmdLine);
	        } else if (cmdLine.numCommands == 2) {
		          onePipe(cmdLine);
	        } else {
		          multiplePipes(cmdLine);
	        }
	    } else {
		      waitpid(child, &status, 0);
	    }
	}

	if(input == stdin)
	{
	    printf("? ");
	    fflush(stdout);
	}
    }

    return 0;
}

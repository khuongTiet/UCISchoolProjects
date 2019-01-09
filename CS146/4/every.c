#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// every [-n,m] [files...]
// Prints out M lines out of every N of the supplied file(s)
// If no files are given, then it takes input from stdin
// n should always be greater than m, if not then program will fail
// if -n,m is given after the file, then the program will fail

void every(int n, int m, FILE* target) {
    char *status;
    char input[255];
    int line_count = n;
    int print_count = 0;
    do {
    	status = fgets(input, sizeof(input), target);
	line_count--;
	if (line_count == 0) {
            while (print_count != m) {
	        if (status != 0) {
	            printf("%s", input);
	        }
         	    print_count++;
	    }
	    line_count = n;
	    print_count = 0;
	}
    } while (status);
}

int main(int argc, char* argv[]) {
    FILE *infile;
    int n = 1;
    int m = 1;
    int start = 1;
    char every_nm[] = "-1,1\0";
    if (getenv("EVERY")) {
	strcpy(every_nm, getenv("EVERY"));
    } else {
	if (argc > 2) {
            if (argv[1][0] == '-') {
		strcpy(every_nm, argv[1]);
		start = 2;
	    } else if (argv[2][0] == '-') {
		printf("lss: Argument error -- -n,m must come before file\n");
		exit(1);
	    }
	}
    }
    char* nm = strtok(every_nm + 1, ",");
    n = atoi(nm);
    nm = strtok(NULL, ",");
    m = atoi(nm);
    if (m > n) {
        printf("ERROR: m must be <= n\n");
 	exit(1);
    }
    if (argc > 3) {
        for (int i = start; i < argc; i++) {
	    infile = fopen(argv[i], "r");
            if (infile == NULL) {
                printf("Cannot open file: %s\n", argv[i]);
	    } else {
	        every(n, m, infile);
	    }
	    fclose(infile);
        }
    } else {
	infile = stdin;
	every(n, m, infile);
	fclose(infile);
    }
    return 0;
}

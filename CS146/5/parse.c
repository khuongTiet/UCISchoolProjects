#include <stdio.h>
#include <string.h>
#include "parse.h"

// Implementation of the nsh shell for Assignment 5 Part 1

void Parse(char *line) {
  struct commandLine cl;
  char *savechar;
  char *saved;
  cl.pipes = 0;
  cl.commands = 0;
  cl.redirect_in = 0;
  cl.redirect_out = 0;
  cl.redirect_from = "";
  cl.redirect_to = "";
  char *p_buf[100];
  char *commands[100];
  int ccount = 0;
  int read_in = 0;
  int read_out = 0;
  int out_count = 0;


  // Get each individual section based on pipes and count pipes + sections
  for (char *curr = strtok_r(line, "|", &savechar); curr != NULL; curr = strtok_r(NULL, "|", &savechar)) {
    p_buf[cl.commands] = curr;
    cl.pipes++;
    cl.commands++;
  }

  // Parse through each section, setting redirections
  for (int i = 0; i < cl.commands; i++) {
    for (char *inv = strtok_r(p_buf[i], " ", &saved); inv != NULL; inv = strtok_r(NULL, " ", &saved)) {
        if (inv[0] == '<') {
	    if (strlen(inv) != 1) {
		while (inv[0] == '<') {
		    inv++;
		}
		if (strcmp(inv, "") != 0 ) {
		    cl.redirect_from = inv;
		    read_in = 0;
		}
                cl.redirect_in = 1;
		read_in = 1;
	    } else {
		cl.redirect_in = 1;
		read_in = 1;
	    }
	}
	else if (inv[0] == '>') {
	    if (strlen(inv) != 1) {
		while (inv[0] == '>') {
		    inv++;
		    out_count++;
		}
		if (strcmp(inv, " ") != 0) {
		    cl.redirect_to = inv;
		    read_out = 0;
		}
		cl.redirect_out =1;
		read_out = 1;
	    } else {
	        cl.redirect_out = 1;
                read_out = 1;
	    }
	} else {
	    if (cl.redirect_in && read_in) {
		cl.redirect_from = inv;
                read_in = 0;
	    } else if (cl.redirect_out && read_out) {
		cl.redirect_to = inv;
                read_out = 0;
	    } else {
  	        if (inv != " ") {
	    	    commands[ccount++] = inv;
	        }
	    }
	}
    }
    if (i != cl.commands - 1) {
      commands[ccount++] = "|";
    }
  }

 // Display number of commands
 printf("%d: ", cl.commands);

 // Display redirection, if any
 if (cl.redirect_in) {
     printf("%s'%s' ", "<", cl.redirect_from);
 }

 // Display all the commands parsed and the pipes
 for (int i = 0; i < ccount; i++) {
     if (commands[i] == "|") {
	printf("| ");
     } else {
        printf("'%s' ", commands[i]);
     }
 }

 // Display redirection, if any
 if (cl.redirect_out) {
     if (out_count % 2 == 0) {
	printf("%s'%s' ", ">>", cl.redirect_to);
     } else {
        printf("%s'%s' ", ">", cl.redirect_to);
     }
 }

  printf("\n");
  
}

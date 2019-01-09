#include <stdio.h>
#include <string.h>
#include "parse.h"

int main(int argc, char* argv) {
  char input_line[1024];			// User input buffer

  while (1) {
    printf("? ");				// Prompt
    fgets(input_line, 1024, stdin);		// Take in input
    size_t ln = strlen(input_line) - 1;		// Remove trailing newline
    if (input_line[ln] == '\n') {
      input_line[ln] = '\0';
    }
    Parse(input_line);
  }
  return 0;
}

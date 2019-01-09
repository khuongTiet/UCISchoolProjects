#ifndef PARSE_H
#define PARSE_H

struct commandLine {
  int pipes;
  int commands;
  char line[1024];
  int redirect_in;
  int redirect_out;
  char *redirect_from;
  char *redirect_to;
};

void Parse(char *line);

#endif /* PARSE_H */

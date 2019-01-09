#include <sys/wait.h>
#include "parse.h"

void change(struct commandLine cl) {
    if (cl.argv[1] == NULL) {
	     chdir(getenv("HOME"));
    } else {
	     chdir(cl.argv[1]);
    }
}

void setIO(struct commandLine cl) {
    if (cl.infile) {
	     int in_fd = open(cl.infile, O_RDONLY);
	     if (in_fd < 0) {
		       perror("Error opening");
	     }
	     dup2(in_fd, 0);
	     close(in_fd);
    }
    if (cl.outfile) {
      int out_fd;
      if ((int)cl.append) {
        out_fd = open(cl.outfile, O_WRONLY | O_APPEND | O_CREAT , S_IRUSR | S_IWUSR);
      	if (out_fd < 0) {
      	    perror("Error opening");
      	}
      } else {
        out_fd = open(cl.outfile, O_WRONLY | O_TRUNC | O_CREAT , S_IRUSR | S_IWUSR);
      	if (out_fd < 0) {
      	    perror("Error opening");
      	}
      }
      dup2(out_fd, 1);
      close(out_fd);
    }
}

void single(struct commandLine cl) {
    setIO(cl);
    execvp(cl.argv[cl.cmdStart[0]], &(cl.argv[cl.cmdStart[0]]));
    exit(1);
}

void onePipe(struct commandLine cl) {
    int fd[2];
    pipe(fd);
    int status;
    int child = fork();
    if (child == 0) {
      	dup2(fd[1], STDOUT_FILENO);
      	close(fd[0]);
      	close(fd[1]);
      	execvp(cl.argv[cl.cmdStart[0]], &(cl.argv[cl.cmdStart[0]]));
	exit(1);
    } else {
      	child = fork();
      	if (child == 0) {
      	    dup2(fd[0], STDIN_FILENO);
      	    close(fd[1]);
      	    close(fd[0]);
      	    execvp(cl.argv[cl.cmdStart[1]], &(cl.argv[cl.cmdStart[1]]));
	    exit(1);
      	}
      	close(fd[0]);
      	close(fd[1]);
      	waitpid(child, &status, 0);
    }
}

void multiplePipes(struct commandLine cl) {
  int current_fd = 0;
  for (int i = 0; i < cl.numCommands; i++) {
    int fd[2];
    int status;
    int child;
    pipe(fd);
    if ((child = fork()) == 0) {
      dup2(current_fd, STDIN_FILENO);
      if (i != cl.numCommands - 1) {
        dup2(fd[1], STDOUT_FILENO);
      }
      close(fd[0]);
      execvp(cl.argv[cl.cmdStart[i]], &(cl.argv[cl.cmdStart[i]]));
      exit(1);
    } else {
      waitpid(child, &status, 0);
      close(fd[1]);
      current_fd = fd[0];
    }
  }
}

#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <pwd.h>
#include <grp.h>
#include <stdint.h>
#include <time.h>
#include <unistd.h>

// Helper function to print out the permissions of each file
// Checks if each file has permission, if so then print corresponding
// character, else print out -
void get_perms(mode_t mode) {
    printf( (S_ISDIR(mode))  ? "d" : "-");
    printf( (mode & S_IRUSR) ? "r" : "-");
    printf( (mode & S_IWUSR) ? "w" : "-");
    printf( (mode & S_IXUSR) ? "x" : "-");
    printf( (mode & S_IRGRP) ? "r" : "-");
    printf( (mode & S_IWGRP) ? "w" : "-");
    printf( (mode & S_IXGRP) ? "x" : "-");
    printf( (mode & S_IROTH) ? "r" : "-");
    printf( (mode & S_IWOTH) ? "w" : "-");
    printf( (mode & S_IXOTH) ? "x" : "-");
}

// Helper function to print out the owner of the current file
void get_pwd(uid_t id) {
    struct passwd *pwd;
    if ((pwd = getpwuid(id)) != NULL) {
        printf(" %s", pwd->pw_name);
    } else {
        printf("%d", id);
    }
}

// Helper function that prints out the group that the owner belongs to
void get_group(gid_t id) {
    struct group *grp;
    if ((grp = getgrgid(id)) != NULL) {
	     printf(" %s", grp->gr_name);
    } else {
	     printf("%d", id);
    }
}

// Helper function that retrieves the time that the file was last modified
// and then prints it into a formatted string
void get_time(struct stat statbuf) {
    char date[1024];
    struct tm *tm;
    tm = localtime(&statbuf.st_mtime);
    strftime(date, sizeof(date), "%B %d %H:%M", tm);
    printf(" %s", date);
}

// Gets the size of the file, if the file is larger than 1024 bytes
// then it will append K to the file
void get_size(off_t size) {
    int file_size = (int)size;
    char size_string[1024];
    if (file_size > 1024) {
	     sprintf(size_string, "%dK", file_size / 1024);
    } else {
	     sprintf(size_string, "%d", file_size);
    }
    printf(" %4s", size_string);
}

// Comparator function used in qsort
// Sorts based on the returned file size found in
// the lstat struct of the specified files
int size_compare(const void *p, const void *q) {
    struct stat pstat;
    struct stat qstat;
    lstat((*(struct dirent **) p)->d_name, &pstat) == -1;
    lstat((*(struct dirent **) q)->d_name, &qstat) == -1;
    int l = pstat.st_size;
    int r = qstat.st_size;
    if (l > r)
	     return -1;
    else if (l < r)
	     return 1;
    else
	     return 0;
}

// Helper function that prints a formatted version of the file name
void get_filename(struct dirent *cwd) {
    printf(" %-8s\n", cwd->d_name);
}

// Helper function that displays each column of the listed ls command
// except for the file name
void list_file(struct stat statbuf) {
  get_perms(statbuf.st_mode);
  printf(" %-2d", statbuf.st_nlink);
  get_pwd(statbuf.st_uid);
  get_group(statbuf.st_gid);
  get_size(statbuf.st_size);
  get_time(statbuf);
}

// Helper function that performs ls on a directory
// It will first compile all the files into an array that it then
// qsorts based upon file size, then it checks against the options
// to determine formatting of the displayed files
void ls(DIR *target, int option_a, int option_L) {
    struct dirent *cwd;
    struct stat statbuf;
    struct dirent *files[4096];
    int count = 0;
    while ((cwd = readdir(target)) != NULL) {
      if (cwd->d_name[0] == '.') {
          if (option_a) {
        files[count++] = cwd;
          }
      } else {
          files[count++] = cwd;
      }
    }
    qsort(files, count, sizeof(*files), size_compare);
    for (int i = 0; i < count; i++) {
      struct stat tempbuf;
      lstat(files[i]->d_name, &statbuf);
      if (S_ISDIR(statbuf.st_mode) && stat(files[i]->d_name, &tempbuf) == -1) {
        perror("lss: Link error - Broken link found");
      } else {
          list_file(statbuf);
          if (S_ISLNK(statbuf.st_mode)) {
              if (!option_L) {
                char buffer[2048];
                ssize_t r = readlink(files[i]->d_name, buffer, 2048);
                printf(" %-4s -> %-4s\n", files[i]->d_name, buffer);
              } else {
                printf(" %s*\n", files[i]->d_name);
              }
          } else {
            get_filename(files[i]);
          }
      }
   }
}

// Checks options using getopt and then loops through each file or directory
// given to it, performing ls on the file
int main(int argc, char *argv[]) {
    DIR *target;
    struct stat main_statbuf;
    int option_a = 0;
    int option_L = 0;
    int opt;
    while ((opt = getopt (argc, argv, "aAL")) != -1) {
	     switch (opt) {
	        case 'a':
      		  option_a = 1;
      		  break;
      	  case 'A':
      		  option_a = 0;
      		  break;
      	  case 'L':
      		  option_L = 1;
      		  break;
      	  case '?':
            printf("lss: Argument error -- not a valid option\n");
            exit(1);
      		  break;
      }
    }
    if (argc == 1) {
      target = opendir(".");
      ls(target, option_a, option_L);
      closedir(target);
    } else {
        for (int i = optind; i < argc; i++) {
          if (argc - optind > 1) {
            printf("%s:\n", argv[i]);
          }
          if (lstat(argv[i], &main_statbuf) == -1) {
            perror("lstat");
            return -1;
          }
          if (S_ISDIR(main_statbuf.st_mode)) {
            target = opendir(argv[i]);
            ls(target, option_a, option_L);
            closedir(target);
          } else {
            struct stat tempbuf;
            if (stat(argv[i], &tempbuf) == -1) {
              perror("lss: Link error - Broken link found");
            } else {
                list_file(main_statbuf);
                if (S_ISLNK(main_statbuf.st_mode)) {
                      if (!option_L) {
                        char buffer[1024];
                        ssize_t r = readlink(argv[i], buffer, 1024);
                        printf(" %-4s -> %-4s\n", argv[i], buffer);
                      } else {
                        printf(" %s*\n", argv[i]);
                      }
                } else {
                  printf(" %-8s\n", argv[i]);
                }
              }
          }
          if (argc - i > 1) {
            printf("\n");
          }
        }
    }
    return 0;
}

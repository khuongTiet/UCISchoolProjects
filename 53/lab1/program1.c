#include <stdio.h>

struct record
{
	char recEntry[101][81];
	int recSize;
};

struct record read(FILE *fp)
{
	char line[81];
	struct record readFile;
	
	readFile.recSize = 0;

	while( fgets(line, sizeof(line), fp) != NULL)
	{
		sscanf(line, "%[^\n]s", readFile.recEntry[readFile.recSize++]);
	}

	return readFile;
}

void write(char* name, struct record storage)
{
	FILE *fp;
	fp = fopen(name, "w+");
	int i = 0;

	for (i; i < storage.recSize; i++)
		fprintf(fp, "%s\n", storage.recEntry[i]);

	fclose(fp);
}

void print(struct record storage)
{
	int i = 0;
	for (i; i < storage.recSize; i++)
		printf("%d %s\n", i+1 , storage.recEntry[i]);
}

struct record delete(struct record storage, int to_delete)
{
	for (to_delete; to_delete < storage.recSize - 1; to_delete++)
	{
		snprintf(storage.recEntry[to_delete], 
			sizeof(storage.recEntry[to_delete]),
			storage.recEntry[to_delete + 1]);
	}
	storage.recSize--;
	print(storage);
	
	return storage;
}

int main ()
{	
	char command[BUFSIZ];
	char command1[10];
	char command2[BUFSIZ];	
	struct record storage;
	int recorded_bool = 0;
	int to_delete;

	while(strcmp(command1, "quit") != 0){
		printf("> ");
		fgets(command, sizeof command, stdin);
		sscanf(command, "%s %s", command1, command2);

		if (strcmp(command1, "read") == 0)
		{
			FILE *fp;
			fp = fopen(command2, "r");
			if (fp)
			{
				storage = read(fp);	
				recorded_bool = 1;
				fclose(fp);
			}
		}
		else if (strcmp(command1, "write") == 0)
		{
			if (recorded_bool == 1)
				write(command2, storage);
		}
		else if (strcmp(command1, "print") == 0)
		{
			if (recorded_bool == 1)
				print(storage);
		}
		else if (strcmp(command1, "delete") == 0)
		{
			if (recorded_bool == 1)
				to_delete = atoi(command2) - 1;
				if (to_delete >= 0)
					storage = delete(storage, atoi(command2) - 1);
		}
	}
}


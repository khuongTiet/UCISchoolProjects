/*
	Description : Lab 2 LetterGrade
*/

#include <stdio.h>

int main()
{
	int a = 0, b = 0, c = 0, d = 0, f = 0, count = 0;
	int collect = 0;
	char grade;
	while (collect == 0)
	{
		scanf_s(" %c", &grade, 1);
		if (grade == 'Z')
			collect = 1;
		else if (grade == 'A')
			a += 1, count +=1;
		else if (grade == 'B')
			b += 1, count += 1;
		else if (grade == 'C')
			c += 1, count += 1;
		else if (grade == 'D')
			d += 1, count += 1;
		else if (grade == 'F')
			f += 1, count += 1;
	}
	printf("Total Number of Scores Entered: %d\n", count);
	printf("A: %d\n", a);
	printf("B: %d\n", b);
	printf("C: %d\n", c);
	printf("D: %d\n", d);
	printf("F: %d\n", f);
	return 0;
}
/*
	Description : Lab 2 Accumulator
*/

#include <stdio.h>

int main()
{
	int sum = 0, n;
	scanf_s("%d", &n);
	for (int i = 1; i <= n*2; i += 2)
		sum = sum + i;
		printf("%d\n", sum);
	return 0;
}
/*
	Description : Lab 2 Parity example
*/

#include <stdio.h>

int main()
{
	int num1;
	printf("Enter an integer: ");
	scanf_s("%d", &num1);
	if (num1 % 2 == 0)
		printf("Even\n");
	else
		printf("Odd\n");

	return 0;
}
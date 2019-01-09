/*
	Author			: Khuong Tiet
	Description		: Lab 1 - Reading Input
	Date			: 09/29/2015
*/

#include<stdio.h>

int main()
{
	int myvariable;

	printf("Enter a number:");
	scanf_s("%d", &myvariable);
	printf("You entered: %d\n", myvariable);

	return 0;
}
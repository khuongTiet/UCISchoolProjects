/*
	Description : Lab 2 Fibonacci
*/

#include <stdio.h>

int main()
{
	int n, next, first = 1, second = 1;
	printf("Enter the number of terms: ");
	scanf_s("%d", &n);
	for (int fibonacci = 0; fibonacci < n; fibonacci++)
		{
			if (fibonacci <= 1)
				{
					next = 1;
				}

			else
			{
				next = first + second;
				first = second;
				second = next;
			}

			printf("%d\n", next);
		}

	return 0;
}
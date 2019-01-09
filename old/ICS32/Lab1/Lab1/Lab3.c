#include <stdio.h>

int findMin(int A[20], int i, int j)
{
	int minimum, lowest;
	minimum = A[i];
	lowest = i;
	for (i; i < j; i++)
	{
		if (A[i] < minimum)
		{
			minimum = A[i];
			lowest = i;
		}
	}
	return lowest;
}

int main()
{
	printf("Part 1 - findMin");
	int A[20];
	int i, number, n, temp;
	for (i = 0; i<20; i++)
	{
		printf("Please enter a number: ");
		scanf_s("%d", &number);
		A[i] = number;
	}

	for (i = 0; i < 20; i++)
	{
		n = findMin(A, i, 20);
		temp = A[i];
		A[i] = A[n];
		A[n] = temp;
	}

	for (i = 0; i < 20; i++)
	{
		printf("%d\n", A[i]);
	}

	return 0;
}
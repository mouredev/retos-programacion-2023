#include <stdio.h>

int	calculate_spaces(int n1, int number)
{
	int	spaces;

	spaces = 2;
	if (number < 10)
		spaces++;
	return (spaces);
}

int	main(void)
{
	for (int i = 1; i <= 10; i++)
	{
		printf("\n-----------------\n");
		if (i == 10)
			printf("| Tabla del %d  |\n", i);
		else
			printf("|  Tabla del %d  |\n", i);
		printf("-----------------\n");
		for (int j = 1; j <= 10; j++)
		{
			printf("|");
			for (int k = 0; k < calculate_spaces(i, i * j); k++)
			{
				printf(" ");
				if (i == 10 && j == 10)
					k++;
			}
			printf("%d x %d = %d", i, j, i * j);
			for (int k = 0; k < calculate_spaces(j, i * j); k++)
			{
				printf(" ");
				if (i == 10 && j == 10)
					k++;
			}
			if (i > 1 && i < 10 && j < 10 && i * j > 9)
				printf(" ");
			printf("|\n");
		}
		printf("-----------------\n");
	}
	return (0);
}
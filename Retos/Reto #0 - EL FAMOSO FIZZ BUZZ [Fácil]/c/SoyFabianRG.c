#include <stdio.h>

int main()
{
	int numeroEntero;

	for(numeroEntero = 1; numeroEntero <= 100; numeroEntero++)
	{
		if (numeroEntero % 5 == 0 && numeroEntero % 3 == 0)
		{
			printf("fizzbuzz\n");
		}

		else if (numeroEntero % 3 == 0)
		{
			printf("fizz\n");
		}

		else if (numeroEntero % 5 == 0)
		{
			printf("buzz\n");
		}

		else
		{
			printf("%i\n", numeroEntero);
		}
	}

	return 0;
}

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

#include <stdio.h>
#include <stdbool.h>

bool	prime(int number);
bool	fibonacci(int number);
bool	even(int number);

int	main(void)
{
	int		number;
	bool	isPrime;
	bool	isFibonacci;
	bool	isEven;

	printf("Introduce a number: ");
	scanf(" %d", &number);
	isPrime = prime(number);
	isFibonacci = fibonacci(number);
	isEven = even(number);
	if (isPrime && isFibonacci && isEven)
	{
		printf("%d is prime, fibonacci and even\n", number);
	}
	else if (isPrime && isFibonacci && !isEven)
	{
		printf("%d is prime, fibonacci and odd\n", number);
	}
	else if (isPrime && !isFibonacci && isEven)
	{
		printf("%d is prime, not fibonacci and even\n", number);
	}
	else if (isPrime && !isFibonacci && !isEven)
	{
		printf("%d is prime, not fibonacci and odd\n", number);
	}
	else if (!isPrime && isFibonacci && isEven)
	{
		printf("%d is not prime, fibonacci and even\n", number);
	}
	else if (!isPrime && isFibonacci && !isEven)
	{
		printf("%d is not prime, fibonacci and odd\n", number);
	}
	else if (!isPrime && !isFibonacci && isEven)
	{
		printf("%d is not prime, not fibonacci and even\n", number);
	}
	else if (!isPrime && !isFibonacci && !isEven)
	{
		printf("%d is not prime, not fibonacci and odd\n", number);
	}
	return (0);
}

bool	prime(int number)
{
	int	divisor;

	if (number == 2)
	{
		return (true);
	}
	else if (number < 2 || even(number)) 
	{
		return (false);
	}
	else if (number < 9)
	{
		return (true);
	}
	divisor = 1;
	for (int i = 3; i <= number; i++)
	{
		if (number % i == 0 && i != number)
		{
			return (false);
		}
		if (i % 2 == 0)
		{
			i++;
		}
	}
	return (true);
}

bool	fibonacci(int number)
{
	int	n1;
	int	n2;
	int	temp;

	n1 = 1;
	n2 = 1;
	while (n1 <= number)
	{
		if (n1 == number)
		{
			return (true);
		}
		temp = n1;
		n1 += n2;
		n2 = temp;
	}
	return (false);
}

bool	even(int number)
{
	if (number % 2 == 0)
	{
		return (true);
	}
	return (false);
}

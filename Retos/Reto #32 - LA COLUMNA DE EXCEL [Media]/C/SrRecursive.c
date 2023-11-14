#include <unistd.h>
#include <stdlib.h>

int		validColumn(const char *str);
void	columnToNumber(const char *str);
void	ft_putnbr(int number);
void	ft_putchar(int c);

int	main(void)
{
	char	*str;
	size_t	bytes_read;

	str = (char *)malloc(256 * sizeof(char));
	if (str == NULL)
	{
		write(1, "Error allocating memory\n", 25);
		return (0);
	}
	write(1, "Introduce the column: ", 23);
	bytes_read = read(0, str, 256);
	if (bytes_read < 0)
	{
		write(1, "Error reading\n", 15);
		return (0);
	}
	str[bytes_read] = '\0';
	if (validColumn(str) == 0)
	{
		free(str);
		write(1, "Invalid column\n", 16);
		return (0);
	}
	columnToNumber(str);
	free(str);
	return (0);
}

int	validColumn(const char *str)
{
	int	counter = 0;
	
	if (str == NULL)
	{
		return (0);
	}
	if (str[counter] == '\0' || str[counter] == '\n')
	{
		return (0);
	}
	while (str[counter] != '\0' && str[counter] != '\n')
	{
		if (str[counter] < 'A' || str[counter] > 'Z')
		{
			return (0);
		}
		counter++;
	}
	return (1);
}

void	ft_putchar(int c)
{
	write(1, &c, 1);
	return ;
}

void	ft_putnbr(int number)
{
	if (number >= 0)
	{
		if (number > 9)
		{
			ft_putnbr(number / 10);
			ft_putchar(number % 10 + '0');
		}
		else
		{
			ft_putchar(number % 10 + '0');
		}
	}
	return ;
}

void	columnToNumber(const char *str)
{
	int index, length, number;

	index = 0;
	length = 0;
	number = 0;
	while (str[length] != '\0' && str[length] != '\n')
	{
		length++;
	}
	while (str[index] != '\0' && str[index] != '\n')
	{
		number = (int)(str[index] - 'A') + 1 + number * 26 * length;
		index++;
		length--;
	}
	ft_putnbr(number);
	return ;
}

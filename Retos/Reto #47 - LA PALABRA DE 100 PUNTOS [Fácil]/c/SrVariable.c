#define WORD_LENGTH 1024
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int	add_points(char *word)
{
	int	counter;

	counter = 0;
	for (int i = 0; word[i]; i++)
	{
		if (word[i] == ' ')
			break ;
		else if (isupper(word[i]))
			counter += word[i] - 'A' + 1;
		else if (islower(word[i]))
			counter += word[i] - 'a' + 1;
	}
	return (counter);
}

int	main(void)
{
	int		points;
	char	*word;

	points = 0;
	word = calloc(WORD_LENGTH, 1);
	if (!word)
		return (1);
	while (points != 100)
	{
		printf("Introduce a word: ");
		if (!fgets(word, WORD_LENGTH, stdin))
		{
			free(word);
			return (2);
		}
		points = add_points(word);
		printf("Word Score: %d\n", points);
		if (points > 100)
			printf("Too high!\n");
		else if (points < 100)
			printf("Too low!\n");
	}
	printf("You won!");
	free(word);
	return (0);
}

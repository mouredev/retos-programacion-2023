#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char	questions[16][1024] = {"\nWhen was Github launched?\na. 2008\nb. 2009\nc. 2010\nd. 2011\n\n",
								"\n25 + 5 / 5 = ?\na. 0\nb. 6\nc. 25\nd. 26\n\n",
								"\nWhat is the command to list all files in a directory?\na. ls\nb. dir\nc. list\nd. cd\n\n",
								"\nWhat is the command to create a new directory?\na. mkdir\nb. newdir\nc. md\nd. cd\n\n",
								"\nWhat is the command to remove a directory?\na. removedir\nb. rmdir\nc. rd\nd. cd\n\n",
								"\nWhat is the command to see the commit history from a repository?\na. git log\nb. git commit\nc. git history\nd. git show\n\n",
								"\nWhat is the correct spelling? \na. git pul\nb. git pull\nc. git pool\nd. git pule\n\n",
								"\nWhat is the command to add a file to the staging area?\na. git pull\nb. git commit\nc. git push\nd. git add\n\n",
								"\n1 + 1 + 1 - 3 * (5 + 1) - 25 + (5 * 5) = ?\na. -18\nb. 25\nc. 0\nd. 10\n\n",
								"\nWhen Halloween is celebrated?\na. 31 October\nb. 1 November\nc. 31 December\nd. 25 December\n\n",
								"\nWhat is H2O in chemistry?\na. Water\nb. Oxygen\nc. Hydrogen\nd. Carbon\n\n",
								"\nWhat is the capital of Spain?\na. Barcelona\nb. Madrid\nc. Sevilla\nd. Valencia\n\n",
								"\nWhat is the capital of France?\na. Paris\nb. Lyon\nc. Marseille\nd. Toulouse\n\n",
								"\nWhat is an integer?\na. A number with decimals\nb. A number without decimals\nc. A number with letters\nd. A number with symbols\n\n",
								"\nWhat is the command to create a new branch?\na. git branch\nb. git new branch\nc. git create branch\nd. git new\n\n",
								"\nWhen was the first version of C released?\na. 1974\nb. 1972\nc. 1970\nd. 1976\n\n"};
char	answers[16] = {'a',
						'd',
						'a',
						'b',
						'a',
						'a',
						'b',
						'd',
						'c',
						'a',
						'a',
						'b',
						'a',
						'b',
						'a',
						'c'};

enum	e_house
{
	PLAYER = 'P',
	GHOST = 'G',
	TREAT = 'T',
	ENIGMA = '?',
	EXPLORED = 'X'
};

enum	e_movement
{
	UP = 'w',
	DOWN = 's',
	LEFT = 'a',
	RIGHT = 'd',
	HELP = 'h',
	QUIT = 'q'
};

enum	e_answer
{
	SUCCESS = 1,
	FAIL = 0,
	WIN = 2
};

int		move_up(char house[4][4]);
int		move_down(char house[4][4]);
int		move_left(char house[4][4]);
int		move_right(char house[4][4]);
int		show_help(void);
int		handle_input(char input, char house[4][4]);
int		handle_event(int event, int playerXpos, int playerYpos);
void	show_house(char house[4][4]);
int		question_generator(void);
void	random_house(char house[4][4]);

int	main(void)
{
	char	house[4][4] = {0, 0, 0, 0,
							0, 0, 0, 0,
							0, 0, 0, 0,
							0, 0, 0, 0};
	char	input;
	int		win;

	srand(time(NULL));
	input = 0;
	win = 0;
	random_house(house);
	while (!win && input != QUIT)
	{
		show_house(house);
		printf("Introduce a movement: ");
		input = fgetc(stdin);
		getchar();
		win = handle_input(input, house);
	}
	return (0);
}

void	show_house(char house[4][4])
{
	for (int i = 0 ; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
			printf("%c ", house[i][j]);
		printf("\n");
	}
}

int	show_help(void)
{
	printf("Movement:\n");
	printf("w - Up\n");
	printf("s - Down\n");
	printf("a - Left\n");
	printf("d - Right\n");
	printf("h - Help\n");
	printf("q - Quit\n");
	return (0);
}

int	handle_event(int event, int playerXpos, int playerYpos)
{
	int	success_answers;

	success_answers = 0;
	switch (event)
	{
	case GHOST:
		printf("You found a ghost, you have to answer two questions.\n");
		success_answers += question_generator();
		success_answers += question_generator();
		if (success_answers == 2)
			return (SUCCESS);
		else
			return (FAIL);
	case TREAT:
		printf("You found the treat, you won.\n");
		return (WIN);
	case ENIGMA:
		printf("You found an enigma, you have to solve it.\n");
		success_answers += question_generator();
		return (success_answers);
	case EXPLORED:
		printf("You already explored this place.\n");
		return (EXPLORED);
	default:
		printf("Invalid event.\n");
		return (0);
	return (0);
	}
}

int	move_up(char house[4][4])
{
	int	playerXpos;
	int	playerYpos;
	int	event;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (house[i][j] == PLAYER)
			{
				playerXpos = j;
				playerYpos = i;
			}
		}
	}
	if (playerYpos == 0)
	{
		printf("You can't move up.\n");
		return (0);
	}
	event = handle_event(house[playerYpos - 1][playerXpos], playerXpos, playerYpos);
	if (event == 0)
	{
		printf("You didn't answer correctly, you stay in the same place!\n");
		return (FAIL);
	}
	else if (event == WIN)
		return (WIN);
	house[playerYpos][playerXpos] = EXPLORED;
	house[playerYpos - 1][playerXpos] = PLAYER;
	return (0);
}

int	move_down(char house[4][4])
{
	int	playerXpos;
	int	playerYpos;
	int event;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
			if (house[i][j] == PLAYER)
			{
				playerXpos = j;
				playerYpos = i;
			}
	}
	if (playerYpos == 3)
	{
		printf("You can't move down.\n");
		return (0);
	}
	event = handle_event(house[playerYpos + 1][playerXpos], playerXpos, playerYpos);
	if (event == 0)
	{
		printf("You didn't answer correctly, you stay in the same place!\n");
		return (FAIL);
	}
	else if (event == WIN)
		return (WIN);
	house[playerYpos][playerXpos] = EXPLORED;
	house[playerYpos + 1][playerXpos] = PLAYER;
	return (0);
}

int	move_left(char house[4][4])
{
	int	playerXpos;
	int	playerYpos;
	int	event;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4 ; j++)
			if (house[i][j] == PLAYER)
			{
				playerXpos = j;
				playerYpos = i;
			}
	}
	if (playerXpos == 0)
	{
		printf("You can't move left.\n");
		return (0);
	}
	event = handle_event(house[playerYpos][playerXpos - 1], playerXpos, playerYpos);
	if (event == 0)
	{
		printf("You didn't answer correctly, you stay in the same place!\n");
		return (FAIL);
	}
	else if (event == WIN)
		return (WIN);
	house[playerYpos][playerXpos] = EXPLORED;
	house[playerYpos][playerXpos - 1] = PLAYER;
	return (0);
}

int	move_right(char house[4][4])
{
	int	playerXpos;
	int	playerYpos;
	int	event;

	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4 ; j++)
			if (house[i][j] == PLAYER)
			{
				playerXpos = j;
				playerYpos = i;
			}
	}
	if (playerXpos == 3)
	{
		printf("You can't move right.\n");
		return (0);
	}
	event = handle_event(house[playerYpos][playerXpos + 1], playerXpos, playerYpos);
	if (event == FAIL)
	{
		printf("You didn't answer correctly, you stay in the same place!\n");
		return (FAIL);
	}
	else if (event == WIN)
		return (WIN);
	house[playerYpos][playerXpos] = EXPLORED;
	house[playerYpos][playerXpos + 1] = PLAYER;
	return (0);
}

int	handle_input(char input, char house[4][4])
{
	int	status;
	switch (input)
	{
	case QUIT:
		printf("Quitting...\n");
		return (0);
	case HELP:
		status = show_help();
		break;
	case UP:
		status = move_up(house);
		break;
	case DOWN:
		status = move_down(house);
		break;
	case LEFT:
		status = move_left(house);
		break;
	case RIGHT:
		status = move_right(house);
		break;
	default:
		printf("Invalid movement, type h for help.\n");
		return (0);
	}
	if (status == 1)
		return (status);
	return (0);
}

int	question_generator(void)
{
	int		questionid;
	char	answer;

	questionid = rand() % 16;
	printf("%s", questions[questionid]);
	printf("Introduce your answer: ");
	answer = fgetc(stdin);
	getchar();
	if (answer == answers[questionid])
	{
		printf("Correct answer!\n");
		return (SUCCESS);
	}
	printf("Wrong answer!\n");
	return (FAIL);
}

void	random_house(char house[4][4])
{
	int	options[10] = {ENIGMA,
						ENIGMA,
						ENIGMA,
						ENIGMA,
						ENIGMA,
						ENIGMA,
						ENIGMA,
						ENIGMA,
						ENIGMA,
						GHOST};
	int	treatXpos;
	int	treatYpos;

	house[rand() % 4][rand() % 4] = PLAYER;
	treatXpos = rand() % 4;
	treatYpos = rand() % 4;
	while (house[treatYpos][treatXpos] == PLAYER)
	{
		treatXpos = rand() % 4;
		treatYpos = rand() % 4;
	}
	house[treatYpos][treatXpos] = TREAT;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4 ; j++)
		{
			if (house[i][j] != PLAYER && house[i][j] != TREAT)
				house[i][j] = options[rand() % 10];
		}
	}
}

/*
 * Crea un programa capaz de gestionar una pieza de Tetris.
 * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
 *   🔳
 *   🔳🔳🔳
 * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
 *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
 */

#define ROWS 10
#define COLS 10

#include <stdio.h>
#include <stdlib.h>

char	**createTable(void);
char	**putPiece(char **table);
char	**movePiece(char **table);
char	**moveDown(char **table);
char	**moveLeft(char **table);
char	**moveRight(char **table);
char	**firstRotation(char **table);
char	**secondRotation(char **table);
char	**thirdRotation(char **table);
char	**fourthRotation(char **table);
char	**rotate(char **table, int *state);
void	full_free(char **table, int index);
void	printTable(char **table);

int	main(void)
{
	char	**table;
	int		finish;

	finish = 0;
	table = createTable();
	if (table == NULL)
	{
		fprintf(stderr, "Error allocating memory\n");
		return (0);
	}
	putPiece(table);
	printTable(table);
	while (!finish)
	{
		printf("Introduce a move (a, s, d, w / h, j, l, k): ");
		movePiece(table);
		printTable(table);
		for (int i = 0; i < ROWS; i++)
		{
			if (table[9][i] == '1' ||
				table[9][i] == '2' ||
				table[9][i] == '3' ||
				table[9][i] == '4')
			{
				finish = 1;
			}
		}
	}
	full_free(table, ROWS);
	return (0);
}

void	full_free(char **table, int index)
{
	while (index--)
	{
		free(table[index]);
	}
	if (table != NULL)
	{
		free(table);
	}
	return ;
}

char	**createTable(void)
{
	char	**table;

	table = (char **)malloc(ROWS * sizeof(char *));
	for (int index = 0; index < ROWS; index ++)
	{
		table[index] = (char *)malloc(COLS * sizeof(char));
		if (table[index] == NULL)
		{
			full_free(table, index);
			return (NULL);
		}
		for (int index2 = 0; index2 < COLS; index2++)
		{
			if (index2 == COLS)
			{
				table[index][index2] = '\0';
			}
			else
			{
				table[index][index2] = '-';
			}
		}
	}
	return (table);
}

char	**putPiece(char **table)
{
	table[0][0] = '1';
	table[1][0] = '2';
	table[1][1] = '3';
	table[1][2] = '4';
	return (table);
}

char	**moveDown(char **table)
{
	for (int i = ROWS - 1; i >= 0; i--)
	{
		for (int j = 0; j < COLS; j++)
		{
			if (table[i][j] == '1' ||
				table[i][j] == '2' ||
				table[i][j] == '3' ||
				table[i][j] == '4'
				&& i + 1 != COLS)
			{
				table[i + 1][j] = table[i][j];
				table[i][j] = '-';
			}
		}
	}
	return (table);
}

char	**moveLeft(char **table)
{
	for (int i = 0; i < ROWS; i++)
	{
		if (table[i][0] == '1' ||
			table[i][0] == '2' ||
			table[i][0] == '3' ||
			table[i][0] == '4')
		{
			return (table);
		}
	}
	for (int i = 0; i < ROWS; i++)
	{
		for (int j = 1; j < COLS; j++)
		{
			if (table[i][j] == '1' ||
				table[i][j] == '2' ||
				table[i][j] == '3' ||
				table[i][j] == '4')
			{
				table[i][j - 1] = table[i][j];
				table[i][j] = '-';
			}
		}
	}
	return (table);
}

char	**moveRight(char **table)
{
	char	temp;
	for (int i = 0; i < ROWS; i++)
	{
		if (table[i][9] == '1' ||
			table[i][9] == '2' ||
			table[i][9] == '3' ||
			table[i][9] == '4')
		{
			return (table);
		}
	}
	for (int i = 0; i < ROWS; i++)
	{
		for (int j = COLS - 1; j >= 0; j--)
		{
			if ((table[i][j] == '1' ||
				table[i][j] == '2' ||
				table[i][j] == '3' ||
				table[i][j] == '4') &&
				j + 1 != COLS &&
				(table[i][j + 1] != '1' ||
				table[i][j + 1] != '2' ||
				table[i][j + 1] != '3' ||
				table[i][j + 1] != '4'))
			{
				temp = table[i][j];
				table[i][j + 1] = temp;
				table[i][j] = '-';
			}
		}
	}
	return (table);
}

char	**firstRotation(char **table)
{
	int	xpos = 0;
	int	ypos = 0;

	for (int i = 0; i < COLS; i++)
	{
		for (int j = 0; j < ROWS; j++)
		{
			if (table[i][j] == '3')
			{
				xpos = i;
				ypos = j;
			}
			table[i][j] = '-';
		}
	}
	if ((xpos > 0 && xpos < ROWS - 1) || (ypos > 0 && ypos < COLS - 1))
	{
		table[xpos - 1][ypos - 0] = '4';
		table[xpos][ypos] = '3';
		table[xpos + 1][ypos - 1] = '1';
		table[xpos + 1][ypos - 0] = '2';
	}
	return (table);
}

char	**secondRotation(char **table)
{
	int	xpos = 0;
	int	ypos = 0;

	for (int i = 0; i < COLS; i++)
	{
		for (int j = 0; j < ROWS; j++)
		{
			if (table[i][j] == '3')
			{
				xpos = i;
				ypos = j;
			}
			if (ypos + 1 == ROWS)
			{
				ypos--;
			}
			table[i][j] = '-';
		}
	}
	if ((xpos > 0 && xpos < ROWS - 1) || (ypos > 0 && ypos < COLS - 1))
	{
		table[xpos - 1][ypos - 1] = '4';
		table[xpos - 1][ypos - 0] = '3';
		table[xpos - 1][ypos + 1] = '2';
		table[xpos][ypos + 1] = '1';
	}
	return (table);
}

char	**thirdRotation(char **table)
{
	int	xpos = 0;
	int	ypos = 0;

	for (int i = 0; i < COLS; i++)
	{
		for (int j = 0; j < ROWS; j++)
		{
			if (table[i][j] == '3')
			{
				xpos = i + 1;
				ypos = j;
			}
			table[i][j] = '-';
		}
	}
	if ((xpos > 0 && xpos < ROWS - 1) || (ypos > 0 && ypos < COLS - 1))
	{
		table[xpos - 1][ypos - 0] = '2';
		table[xpos - 1][ypos + 1] = '1';
		table[xpos][ypos] = '3';
		table[xpos + 1][ypos - 0] = '4';
	}
	return (table);
}

char	**fourthRotation(char **table)
{
	int	xpos = 0;
	int	ypos = 0;

	for (int i = 0; i < COLS; i++)
	{
		for (int j = 0; j < ROWS; j++)
		{
			if (table[i][j] == '3')
			{
				xpos = i;
				ypos = j;
			}
			if (ypos == 0)
			{
				ypos++;
			}
			table[i][j] = '-';
		}
	}
	if ((xpos > 0 && xpos < ROWS - 1) || (ypos > 0 && ypos < COLS - 2))
	{
		table[xpos - 1][ypos - 1] = '1';
		table[xpos][ypos - 1] = '2';
		table[xpos][ypos] = '3';
		table[xpos][ypos + 1] = '4';
	}
	return (table);
}

char	**rotate(char **table, int *state)
{
	switch (*state)
	{
		case 0:
			*state = 1;
			table = firstRotation(table);
			break;
		case 1:
			*state = 2;
			table = secondRotation(table);
			break;
		case 2:
			*state = 3;
			table = thirdRotation(table);
			break;
		case 3:
			*state = 0;
			table = fourthRotation(table);
			break;
		default:
			break;
	}
	return (table);
}

char	**movePiece(char **table)
{
	char		movement;
	int			index;
	static int	state = 0;

	index = 0;
	scanf(" %c", &movement);
	if (movement == 'd' || movement == 'l')
	{
		table = moveRight(table);
	}
	else if (movement == 'a' || movement == 'h')
	{
		table = moveLeft(table);
	}
	else if (movement == 's' || movement == 'j')
	{
		table = moveDown(table);
	}
	else if (movement == 'r' || movement == 'k')
	{
		table = rotate(table, &state);
	}
	return (table);
}

void	printTable(char **table)
{
	printf("\n");
	for (int i = 0; i < ROWS; i++)
	{
		for (int j = 0; j < COLS; j++)
		{
			printf("%c", table[i][j]);
		}
		printf("\n");
	}
	return ;
}

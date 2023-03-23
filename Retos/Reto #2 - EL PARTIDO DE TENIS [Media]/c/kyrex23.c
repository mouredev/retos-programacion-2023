/*
 * # Reto #2: EL PARTIDO DE TENIS
 * #### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23
 *
 * ## Enunciado
 *
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 *
 * .....................................................................................................................
 *
 * Usage: ./kyrex23 P1 P1 P2 P2 P1 P2 P1 P1 (arguments other than P1 or P2 are ignored)
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
	int id;
	char *name;
	int score;
} Player;

const char *PUNCTUATIONS[] = {"Love", "15", "30", "40"};

int filter_points(char *[], int, Player, Player, int *[]);

// ---------------------------------------------------------------------------------------------------------------------

int main(int argc, char *argv[]) {
	if(argc < 2) {
		printf("[ERROR] Missing required input sequence\n");
		printf("Usage example: %s P1 P1 P2 P2 P1 P2 P1 P1\n", argv[0]);
		return 1;
	}

	Player player1 = { .id = 1, .name = "P1", .score = 0};
	Player player2 = { .id = 2, .name = "P2", .score = 0};

	int *points = NULL; // Let's filter and parse the input: int[] is better to collect the results than char*[]
	int num_points = filter_points(argv, argc, player1, player2, &points); // by reference to allocate dynamic memory

	if(num_points == 0) {
		printf("[ERROR] Invalid input: arguments must be a list of {%s, %s}\n", player1.name, player2.name);
		return 2;
	}

	Player *winner = NULL;
	for(int i = 0; i < num_points && !winner; ++i) {
		(points[i] == player1.id) ? player1.score++ : player2.score++;

		if(player1.score > 2 && player1.score == player2.score) {
			printf("Deuce\n");
		} else if(player1.score > 3 || player2.score > 3) {
			Player *temporal_winner = (player1.score > player2.score) ? &player1 : &player2;
			if(abs(player1.score - player2.score) < 2) {
				printf("Ventaja %s\n", temporal_winner->name);
			} else winner = temporal_winner;
		} else printf("%s - %s\n", PUNCTUATIONS[player1.score], PUNCTUATIONS[player2.score]);
	}

	if(winner) printf("Ha ganado el %s\n", winner->name);
	else printf("[WARN] El partido no ha terminado!!\n");

	free(points);
}

// ---------------------------------------------------------------------------------------------------------------------

int filter_points(char *inputs[], int num_inputs, Player p1, Player p2, int *valid_points[]) {
	int num_valid_points = 0;

	for(int i = 0; i < num_inputs; ++i) {
		int current_winner = (strcmp(inputs[i], p1.name) == 0) ? p1.id :
							 (strcmp(inputs[i], p2.name) == 0) ? p2.id : -1;

		if(current_winner != -1) {
			*valid_points = (int*)realloc(*valid_points, sizeof(int) * (num_valid_points + 1));
			(*valid_points)[num_valid_points++] = current_winner;
		}
	}

	return num_valid_points;
}

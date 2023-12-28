/*
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
 */

#include <stdio.h>
#include <string.h>

void printScore(int score);

int main() {
	char *results[] = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
	int results_count = sizeof(results) / 8;
	int p1 = 0;
	int p2 = 0;

	for (int i = 0; i < results_count; i++) {
		if (strcmp(results[i], "P1") == 0) p1++;
		else if (strcmp(results[i], "P2") == 0) p2++;
		else {
			printf("Dato ingresado no valido: %s\n", results[i]); // Si el dato es invalido, aviso y sigo
			continue;
		}

		if (p1 < 3 || p2 < 3) { 
			if (p1 >= 4) { 
				printf("Ha ganado el P1\n");
				break; // una vez que un jugador ha ganado, salgo del loop (Partido terminado)
			} else if (p2 >= 4) { 
				printf("Ha ganado el P2\n");
				break; // una vez que un jugador ha ganado, salgo del loop (Partido terminado)
			} else {
				printScore(p1);
				printf(" - ");
				printScore(p2);
				printf("\n");
			}
		} else {
			if (p1 == p2) {
				printf("Deuce\n");
			} else if (p1 > p2) {
				if (p1 >= p2+2) { 
					printf("Ha ganado el P1\n");
					break; // una vez que un jugador ha ganado, salgo del loop (Partido terminado)
				} else { 
					printf("Ventaja P1\n");
				}
			} else if (p2 > p1) {
				if (p2 >= p1+2) {
					printf("Ha ganado el P2\n");
					break; // una vez que un jugador ha ganado, salgo del loop (Partido terminado)
				} else {
					printf("Ventaja P2\n");
				}
			}
		}
	}
	return 0;
}

void printScore(int score) {
	switch(score) {
		case 0:
			printf("Love");
		break;
		case 1:
			printf("15");
		break;
		case 2:
			printf("30");
		break;
		case 3:
			printf("40");
		break;
	}
}

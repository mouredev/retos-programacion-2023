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
 * Usage: ./kyrex23 <input>
 * Example: ./kyrex23 P1 P1 P2 P2 P1 P2 P1 P1
*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char *KEY_PLAYER_1 = "P1";
const char *KEY_PLAYER_2 = "P2";
const int KEY_POINT_PLAYER_1 = 1; // Used to parse input -> 1 means point for player_1
const int KEY_POINT_PLAYER_2 = 2; // Used to parse input -> 2 means point for player_2
const char *PUNCTUATIONS[] = {"Love", "15", "30", "40"};

int filter_points(char*[], int, int**);

// ---------------------------------------------------------------------------------------------------------------------

int main(int argc, char *argv[]) {
    if(argc < 2) {
        printf("[ERROR] Missing required input sequence\n");
        printf("Usage example: %s P1 P1 P2 P2 P1 P2 P1 P1\n", argv[0]);
        return 1;
    }

    // Let's filter and parse the input: using int[] for points is easier to handle than using char*[]
    int *points = NULL;
    int num_points = filter_points(argv, argc, &points); // must be passed by reference to allocate dynamic memory

    if(num_points == 0) {
        printf("[ERROR] Invalid input: arguments must be a list of {P1, P2}");
        return 2;
    }

    int score_player_1 = 0;
    int score_player_2 = 0;

    for(int i = 0; i < num_points; ++i) {
        score_player_1 += (points[i] == KEY_POINT_PLAYER_1);
        score_player_2 += (points[i] == KEY_POINT_PLAYER_2);

        if(score_player_1 > 2 && score_player_1 == score_player_2) // Draws after 3 pints -> Deuce
            printf("Deuce\n");
        else if(score_player_1 > 3 || score_player_2 > 3) {
            if(abs(score_player_1 - score_player_2) < 2)
                printf("Ventaja %s\n", (score_player_1 > score_player_2 ? KEY_PLAYER_1 : KEY_PLAYER_2));
            else printf("Ha ganado el %s\n", (score_player_1 > score_player_2 ? KEY_PLAYER_1 : KEY_PLAYER_2));
        } else printf("%s - %s\n", PUNCTUATIONS[score_player_1], PUNCTUATIONS[score_player_2]);
    }

    free(points);
}

// ---------------------------------------------------------------------------------------------------------------------

int filter_points(char *original_inputs[], int num_original_inputs, int **parsed_inputs) {
    int num_parsed_inputs = 0;

    for(int i = 0; i < num_original_inputs; ++i) {
        int current_point = (strcmp(original_inputs[i], KEY_PLAYER_1) == 0) ? KEY_POINT_PLAYER_1 :
            (strcmp(original_inputs[i], KEY_PLAYER_2) == 0) ? KEY_POINT_PLAYER_2 : 0;

        if(current_point != 0) {
            *parsed_inputs = (int*)realloc(*parsed_inputs, sizeof(int) * (num_parsed_inputs + 1));
            (*parsed_inputs)[num_parsed_inputs++] = current_point;
        }
    }

    return num_parsed_inputs;
}

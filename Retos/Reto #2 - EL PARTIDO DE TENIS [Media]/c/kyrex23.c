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
const char *PUNCTUATIONS[] = {"Love", "15", "30", "40"};

// ---------------------------------------------------------------------------------------------------------------------

int main(int argc, char *argv[]) {
    int score_player1 = 0;
    int score_player2 = 0;

    if(argc < 2) {
        printf("[ERROR] Missing required input sequence\n");
        printf("Usage example: %s P1 P1 P2 P2 P1 P2 P1 P1\n", argv[0]);

        return 1;
    }

    for(int i = 1; i < argc; ++i) { // i starts in 1 because of argv[0] is the executable name
        score_player1 += (strcmp(argv[i], KEY_PLAYER_1) == 0);
        score_player2 += (strcmp(argv[i], KEY_PLAYER_2) == 0);

        if(score_player1 > 2 && score_player1 == score_player2)
            printf("Deuce\n");
        else if(score_player1 > 3 || score_player2 > 3) {
            if(abs(score_player1 - score_player2) < 2)
                printf("Ventaja %s\n", (score_player1 > score_player2 ? KEY_PLAYER_1 : KEY_PLAYER_2));
            else printf("Ha ganado el %s\n", (score_player1 > score_player2 ? KEY_PLAYER_1 : KEY_PLAYER_2));
        } else printf("%s - %s\n", PUNCTUATIONS[score_player1], PUNCTUATIONS[score_player2]);
    }

}

// ---------------------------------------------------------------------------------------------------------------------

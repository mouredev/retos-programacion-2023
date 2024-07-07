/* # Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
#### Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23

## Enunciado

/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */


#include<stdio.h>
#include<stdlib.h>

#define PIEDRA      0
#define PAPEL       1
#define TIJERA      2
#define LAGARTO     3
#define SPOCK       4

// Funcion que recibe los pares y determina el ganador
void recibePares(char* pares, int* player1,  int* player2);

int main(void){

    char pares[2];
    int player1_wins = 0;
    int player2_wins = 0;

    pares[0] = PIEDRA;
    pares[1] = TIJERA;

    recibePares(pares, &player1_wins, &player2_wins);

    if(player1_wins > player2_wins){
        printf("El jugador 1 ha ganado\n");
        printf("Victorias jugador 1: %d\n", player1_wins);
        printf("Victorias jugador 2: %d\n", player2_wins);
    }

    return 0;

}

void recibePares(char* pares, int* player1,  int* player2){

    if(pares[0] == PIEDRA && pares[1] == TIJERA){
        printf("Jugador 1 gana\n");
        *player1 = *player1 + 1;
    }

}



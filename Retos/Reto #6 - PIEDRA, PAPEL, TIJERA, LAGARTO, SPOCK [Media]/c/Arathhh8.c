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

typedef enum {
    PIEDRA = 1,
    PAPEL,
    TIJERA,
    LAGARTO,
    SPOCK
}Objeto;

// Funcion que recibe los pares y determina el ganador
void recibePares(char* par, int* player1,  int* player2);
void solicitaPar(char* par);
void imprimeObjetos();

int main(void){

    char par[2];
    int player1_wins = 0;
    int player2_wins = 0;
    int rondas;
    int i = 0;

    printf("Ingresa el numero de rondas a jugar: ");
    scanf("%d", &rondas);

    

    for(int i = 0; i < rondas; i++){
        solicitaPar(par);
        recibePares(par, &player1_wins, &player2_wins);
    }
    
    if(player1_wins > player2_wins){
        printf("Player 1 ha ganada");
    }
    

    return 0;
}

void recibePares(char* par, int* player1,  int* player2){

    if(par[0] == PIEDRA && par[1] == TIJERA){
        (*player1)++;
        printf("Player 1 Gana esta ronda\n");
        printf("\n");
    }

}


void solicitaPar(char* par){

    printf("Player 1. Selecciona tu objeto:\n");
    imprimeObjetos();
    scanf("%d", (int*)&par[0]);

    printf("Player 2. Selecciona tu objeto:\n");
    imprimeObjetos();
    scanf("%d", (int*)&par[1]);

}

void imprimeObjetos(){
    printf("1. Piedra  ");
    printf("2. Papel  ");
    printf("3. Tijera  ");
    printf("4. Lagarto  ");
    printf("5. Spock\n");
    printf("Seleccionar: ");
}


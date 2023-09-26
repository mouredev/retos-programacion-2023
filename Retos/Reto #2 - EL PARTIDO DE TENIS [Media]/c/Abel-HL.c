/*
 * Enunciado:
 *
 * 
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
 */

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void){

    char* secuencia[] = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
    int tamano = sizeof(secuencia) / sizeof(secuencia[0]);
    int P1 = 0, P2 = 0; //Contador de los puntos de cada uno de los jugadores

    //Recorremos el vector para ver que jugador gana cada punto
    for(int i = 0; i<tamano ; i++){
        if(secuencia[i] == "P1"){ //Aseguramos q la cadena este en mayusculas por si se introduce en minusculas
            P1 += 1;
        }else if(secuencia[i] == "P2"){
            P2 += 1;
        }else{  
            printf("Jugador Erroneo en la Secuencia dada\n");   //Si aparece un jugador u otra cadena q no sea ni "P1" o "P2"
        }

        switch(P1){
            case 0:
                printf(" Love -");
                break;

            case 1:
                printf(" 15 -");
                break;

            case 2:
                printf(" 30 -");
                break;

            case 3:
                if(P1==P2){
                    printf(" Deuce \n");
                }else{
                    printf(" 40 -");
                }
                break;

            default:
                if(P1 == P2+2){
                    printf(" Ha ganado el P1\n");
                }else if(P1 == P2){
                    printf(" Deuce \n");
                }else if(P1 > P2){
                    printf(" Ventaja P1 \n");
                }
        }

        switch(P2){
            case 0:
                printf(" Love\n");
                break;
            case 1:
                printf(" 15\n");
                break;
            case 2:
                printf(" 30\n");
                break;
            case 3:
                if(P1<P2){
                    printf(" 40\n");
                }
                break;

            default:
                if(P2 > P1){
                    printf(" Ventaja P2 \n");
                }
                if(P2 == P1+2){
                    printf(" Ha ganado el P1\n");
                }  
        }
    }

    return 0;
}

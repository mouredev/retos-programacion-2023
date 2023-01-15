#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
**Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
** El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
** gane cada punto del juego.
**
** - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
** - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
**   15 - Love
**   30 - Love
**   30 - 15
**   30 - 30
**   40 - 30
**   Deuce
**   Ventaja P1
**   Ha ganado el P1
** - Si quieres, puedes controlar errores en la entrada de datos.
** - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
*/

int main(int argc, char *argv[]) {
    FILE *parch = NULL;
    int jug1, jug2, cantJugadores, cantPuntos;
    char game[][6] = {{"Love"},{"15"},{"30"},{"40"}},player[2][3],playerTanto[3];
    parch = fopen("game.txt", "r");
    jug1 = jug2 = 0;
    if(parch == NULL){
        fprintf(stderr,"Error al abrir el archivo");
        return 1;
    }
    fscanf(parch,"%d",&cantJugadores);
    for (int i = 0; i < cantJugadores; i++) {
        fscanf(parch,"%s",player[i]);
    }
    fscanf(parch,"%d",&cantPuntos);
    fprintf(stdout,"COMIENZO DE LA SIMULACIÓN");
    for (int i = 0; i < cantPuntos; i++) {
        fscanf(parch,"%s",playerTanto);
        switch (strcmp(playerTanto,"P1")) {
            case 0:
                    jug1++;
                break;
            default:
                    jug2++;
        }
        if(jug1 <= 3 && jug2 <= 3)
            if(strcmp(game[jug1],"40") !=0 || strcmp(game[jug2],"40") !=0)
                fprintf(stdout,"\n\033[0m%s - %s",game[jug1],game[jug2]);
        if(jug1 >= 3 && jug2 >=3){
            if (jug1 == jug2){
                fprintf(stdout,"\n\033[0mDeuce");
            }
            if(jug1 > jug2 && jug1 -2 != jug2){
                fprintf(stdout,"\n\033[0mVentaja %s",player[0]);
            }
            if(jug2 > jug1 && jug2 -2 != jug1){
                fprintf(stdout,"\n\033[0mVentaja %s",player[1]);
            }
            if (jug1 - 2 == jug2) {
                fprintf(stdout,"\n\033[31mHa ganado el jugador %s",player[0]);
            }else if(jug2 -2 == jug1){
                fprintf(stdout,"\n\033[31mHa ganado el jugador %s",player[1]);
            }
        }
    }
    fclose(parch);
    return 0;
}

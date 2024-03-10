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

#include <iostream>
#include <string>
#include <map>

using namespace std;

// Inicializamos la tabla con las puntuaciones
map < int , string > Puntuaciones = {   
    {0, "Love"},
    {1, "15"},
    {2, "30"},
    {3, "40"}  
};

void PartidoTenis(string puntos[], int longitud) {
    int contadorP1 = 0;
    int contadorP2 = 0;

    for(int i = 0; i < longitud; i++) {
    
        // Tratamiento de errores
        if((puntos[i] != "P1") && (puntos[i] != "P2")) {
            cout << "Los datos no se han introducido correctamente." << endl;
            break;
        }
        // En caso de no haber error, contamos P1 y P2
        else if(puntos[i] == "P1") {
            contadorP1++;
        }
        else if(puntos[i] == "P2") {
            contadorP2++;
        }

        // Impresion de puntos
        if (contadorP1 == 3 && contadorP2 == 3) {
            cout << "Deuce" << endl;
        }

        else if (contadorP1 >= 4 || contadorP2 >= 4) {

            int diff = contadorP1-contadorP2; // Actualizando en cada iteracion

            if (diff == 0) {
                cout << "Deuce" << endl;
            }
            else if (diff == 1) {
                cout << "Ventaja P1" << endl;
            }
            else if (diff == -1) {
                cout << "Ventaja P2" << endl;
            }
            else if (diff >= 2) {
                cout << "Ha ganado P1" << endl;
                cout << "Fin del partido" << endl;
                return; // Termina la función cuando hay un ganador
            }
            else {
                cout << "Ha ganado P2" << endl;
                cout << "Fin del partido" << endl;
                return; // Termina la función cuando hay un ganador
            }
        }

        else {
            cout << Puntuaciones[contadorP1] << " - " << Puntuaciones[contadorP2] << endl;
        }
    }
}

int main() {

    string puntos[] = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"}; // Secuencia de puntos
    int longitud = sizeof(puntos) / sizeof(puntos[0]);  // Longitud del array de puntos
    
    PartidoTenis(puntos,longitud);  // Juego

    return 0;
}

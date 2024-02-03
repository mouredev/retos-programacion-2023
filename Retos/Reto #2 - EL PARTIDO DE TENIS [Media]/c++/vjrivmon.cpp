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
using namespace std;

int main() {
    string punto;
    int p1 = 0, p2 = 0;
    while (cin >> punto) {
        if (punto == "P1") {
            p1++;
        } else if (punto == "P2") {
            p2++;
        } else {
            cout << "Entrada no válida" << endl;
            return 1;
        }
        if (p1 == 4 && p2 == 4) {
            cout << "Deuce" << endl;
        } else if (p1 == 5 || p2 == 5) {
            if (p1 == p2) {
                cout << "Ventaja" << endl;
            } else if (p1 > p2) {
                cout << "Ha ganado el P1" << endl;
                return 0;
            } else {
                cout << "Ha ganado el P2" << endl;
                return 0;
            }
        } else {
            cout << p1 * 15 << " - " << p2 * 15 << endl;
        }
    }
    return 0;
}
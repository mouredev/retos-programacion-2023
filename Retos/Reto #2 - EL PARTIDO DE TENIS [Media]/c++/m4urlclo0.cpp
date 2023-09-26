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

int main() {
    const char* turns[] = { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" };
    int Size = sizeof(turns) / sizeof(turns[0]);
    int P1 = 0;
    int P2 = 0;

    for (int i = 0; i < Size; i++) {
        if (turns[i] == "P1") {
            P1 += 1;
        } else if (turns[i] == "P2") {
            P2 += 1;
        } else {
            std::cout << "Error, No corresponde a ningun jugador!!!" << std::endl;
        }
        switch (P1) {
            case 0: std::cout << "Love" << " - ";     break;
            case 1: std::cout << "15"   << " - ";     break;
            case 2: std::cout << "30"   << " - ";     break;
            case 3:
                if (P1 == P2) {
                    std::cout << "  Deuce" << std::endl;
                } else {
                    std::cout << "40 - ";
                }
                break;
            default:
                if (P1 == P2 + 2) {
                    std::cout << "Ha ganado el P1" << std::endl;
                } else if (P1 == P2) {
                    std::cout << "   Deuce" << std::endl;
                } else if (P1 > P2) {
                    std::cout << "Ventaja P1" << std::endl;
                }
                break;
        }
        switch (P2) {
            case 0: std::cout << "Love"<< std::endl;	break;
            case 1: std::cout << "15"  << std::endl;	break;
            case 2: std::cout << "30"  << std::endl;	break;
            case 3:
		        if (P1 < P2) {
                    std::cout << "40" << std::endl;
                }
                break;
            default:
                if (P1 < P2) {
                    std::cout << "Ventaja P2" << std::endl;
                }
		        if (P1 == P2) {
                    std::cout << "Ha ganado P1" << std::endl;
                }
                break;
        }
    }
    return 0;
}

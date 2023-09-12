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
 */
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void obtenerResultados(int puntosP1, int puntosP2)
{
    vector<string> puntuacion{"Love", "15", "30", "40", "Ventaja"}; // Definimos un vector con los distintos resultados posibles, salvo la victoria.
    int diferencia = puntosP1 - puntosP2; // Variable para ver la diferencia de puntos entre los jugadores.

    if (puntosP1 < 3 && puntosP2 < 3) // si puntosP1 y puntosP2 < 3 (es decir, ninguno tiene ventaja. Estamos en puntuación[0] hasta puntuación[2]. Love hasta 40)
    {
        cout << puntuacion[puntosP1] + " - " + puntuacion[puntosP2] << endl; // Printeamos el resultado actual
    }
    else if (puntosP1 == puntosP2) // Si estamos en empate, imprimimos Deuce.
    {
        cout << "Deuce" << endl;
    }
    else if (puntosP1 > 3 || puntosP2 > 3) // Estamos en situación de "Ventaja" para uno de los dos contrincantes. 
    {
        // Hay que comprobar que diferencia es 1 o -1 y que los puntos están por encima de 3. Solo entonces estamos en situación de ventaja.
        if (diferencia == 1) // Si es uno, significa ventaja para P1. Evaluado con la diferencia.
        {
            cout << (puntuacion[puntosP1] + " P1") << endl;
        }
        else if (diferencia == -1) // En caso de ser -1, significa ventaja para P2.
        {
            cout << (puntuacion[puntosP2] + "P2") << endl;
        }
    }
    if (puntosP1 > 4) // Finalmente, comprobamos cual de los dos jugadores está por encima de 4, significando la victoria.
    {
        cout << "Ha ganado el P1" << endl;
    }
    else if (puntosP2 > 4)
    {
        cout << "Ha ganado el P2" << endl;
    }
}


int main()
{
    vector<string> transcurso = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"}; // Definimos el vector con el transcurso del partido.
    int p1Score = 0, p2Score = 0; // Inicializamos variables para llevar recuento del partido.

    for (const string &point : transcurso) // Por cada valor del vector transcurso...
    {
        if (point == "P1") // Si el punto lo ha ganado P1, sumamos uno. 
        {
            p1Score++;
        }
        else if (point == "P2")
        {
            p2Score++;
        }
        obtenerResultados(p1Score, p2Score); // Actualizamos el resultado actual del partido.
    }
}
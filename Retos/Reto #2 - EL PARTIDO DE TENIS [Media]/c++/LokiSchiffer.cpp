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
#include <map>
#include <string>
using namespace std;

//Inicialización de los puntos de juego
map<int, string> pointsTable = {
  {0, "Love"}, {1, "15"}, {2, "30"}, {3, "40"}
};

bool score(int puntos1, int puntos2, int adv);

void juegoTenis(string arr[], int size);

  
int main() {
  //Secuencia de datos para enviar
  string juego[] = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P1",
                    "P1", "P1", "P1", "P2", "P2", "P1", "P2", "P2"};
  juegoTenis(juego, sizeof(juego)/sizeof(juego[0]));
}

bool score(int puntos1, int puntos2, int adv) {
  //Comprobación de si alguien ha ganado el juego y envía bandera para terminar
  if (adv == 2) {
    cout << "El jugador 1 ha ganado" << endl;
    return true;
  } else if (adv == -2) {
    cout << "El jugador 2 ha ganado" << endl;
    return true;
  }
  //Secuencia para mirar quien de los dos tiene la ventaja, si se tiene deuce o se imprimen los puntos
  if(puntos1 == 3 && puntos2 == 3) {
    if (adv > 0) {
      cout << "Ventaja P1" << endl;
    } else if (adv < 0) {
      cout << "ventaja P2" << endl;
    } else {
      cout << "Deuce" << endl;
    }
  } else {
    cout <<pointsTable[puntos1] << " - " <<pointsTable[puntos2] << endl;
  }
  return false;
}

void juegoTenis(string arr[], int size) {
  //Inicialización de variables
  int jugador1 = 0;
  int jugador2 = 0;
  int ventaja = 0;
  //Control de final de juego
  bool exit = false;
  for (int i = 0; i < size; i++) {
    //Si el juego no ha finalizado sigue contando puntos
	if (not exit) {
      //Por cada punto se sube el marcador, pero al llegar a 40, se deja de contar
	  if (arr[i] == "P1" && jugador1 < 3) {
        jugador1 += 1;
      } else if (arr[i] == "P2" && jugador2 < 3) {
        jugador2 += 1;
      //Si los dos jugadores llegan a 40, se pasa a los escenarios de ventaja
	  } else if (jugador1 == 3 && jugador2 == 3) {
        //Cuando el P1 tiene la ventaja se vuelve positivo y si repite, cumple la condición de victoria
		if (arr[i] == "P1") {
          ventaja += 1;
        //Cuando el P2 tiene la ventaja se vuelve negativo y si repite, cumple la condición de victoria
		} else {
          ventaja -= 1;
        }
      //Si el P1 ya tiene 40 puntos y el P2 dos no, cuando el P1 gana punto se cumple la condición de victoria
	  } else if (arr[i] == "P1") {
        ventaja += 2;
      //Si el P2 ya tiene 40 puntos y el P1 dos no, cuando el P2 gana punto se cumple la condición de victoria
	  } else if (arr[i] == "P2") {
        ventaja -= 2;
      //Mensaje cuando un valor no es valido
	  } else {
        cout << "Valor ingresado no valido" << endl;
      }
	  //Se envía la información de los puntajes al método de impresión
      exit = score(jugador1, jugador2, ventaja);
    //Mensaje especial cuando ya se termino el juego, pero siguen ingresando valores
	} else {
      cout << "El juego ya ha terminado" << endl;
    }
  }
}
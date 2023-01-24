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

import java.util.HashMap;
import java.util.Map;

class Main {
  //Inicialización de los puntos de juego
  static Map<Integer, String> pointsTable;
  static {
    pointsTable = new HashMap<>();
    pointsTable.put(0, "Love");
    pointsTable.put(1, "15");
    pointsTable.put(2, "30");
    pointsTable.put(3, "40");
  };
    
    
  public static void main(String[] args) {
    //Secuencia de datos para enviar
	String[] juego = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2",
                      "P1", "P1", "P1", "P1", "P2", "P2", "P1", "P2", "P2"};
    juegoTenis(juego);
  }
  
  //Método para comprobar los puntos del juego
  static boolean score(int puntos1, int puntos2, int adv) {
    //Comprobación de si alguien ha ganado el juego y envía bandera para terminar
	if (adv == 2) {
      System.out.println("El jugador 1 ha ganado");
      return true;
    } else if (adv == -2) {
      System.out.println("El jugador 2 ha ganado");
      return true;
    }
    //Secuencia para mirar quien de los dos tiene la ventaja, si se tiene deuce o se imprimen los puntos
	if(puntos1 == 3 && puntos2 == 3) {
      if (adv > 0) {
        System.out.println("Ventaja P1");
      } else if (adv < 0) {
        System.out.println("ventaja P2");
      } else {
       System.out.println("Deuce");
      }
    } else {
      System.out.println(pointsTable.get(puntos1) + " - " +
                         pointsTable.get(puntos2));
    }
    return false;
  }
  
  static void juegoTenis(String[] arr) {
    //Inicialización de variables
	int jugador1 = 0;
    int jugador2 = 0;
    int ventaja = 0;
	//Control de final de juego
    boolean exit = false;
    for (String point : arr) {
      //Si el juego no ha finalizado sigue contando puntos
	  if (!exit) {
        //Por cada punto se sube el marcador, pero al llegar a 40, se deja de contar
		if (point == "P1" && jugador1 < 3) {
          jugador1 += 1;
        } else if (point == "P2" && jugador2 < 3) {
          jugador2 += 1;
        //Si los dos jugadores llegan a 40, se pasa a los escenarios de ventaja
		} else if (jugador1 == 3 && jugador2 == 3) {
          //Cuando el P1 tiene la ventaja se vuelve positivo y si repite, cumple la condición de victoria
		  if (point == "P1") {
            ventaja += 1;
		  //Cuando el P2 tiene la ventaja se vuelve negativo y si repite, cumple la condición de victoria
		  } else {
            ventaja -= 1;
          }
        //Si el P1 ya tiene 40 puntos y el P2 dos no, cuando el P1 gana punto se cumple la condición de victoria
		} else if (point == "P1") {
          ventaja += 2;
        //Si el P2 ya tiene 40 puntos y el P1 dos no, cuando el P2 gana punto se cumple la condición de victoria
		} else if (point == "P2") {
          ventaja -= 2;
        //Mensaje cuando un valor no es valido
		} else {
          System.out.println("Valor ingresado no valido");
        }
		//Se envía la información de los puntajes al método de impresión
        exit = score(jugador1, jugador2, ventaja);
      //Mensaje especial cuando ya se termino el juego, pero siguen ingresando valores
	  } else {
        System.out.println("El juego ya ha terminado");
      }
    }
  }
}
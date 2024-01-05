package com.retos;

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
import java.util.Objects;
import java.util.Scanner;

public class Reto2PartidoTenis {

    public static void main(String[] args) {

        HashMap<Integer, String> jugador1 = inicializarJugador();
        HashMap<Integer, String> jugador2 = inicializarJugador();
        String puntosP1 = null;
        String puntosP2 = null;
        int contadorP1 = 0;
        int contadorP2 = 0;
        boolean empate = false;
        boolean victoriaP1 = false;
        boolean victoriaP2 = false;
        boolean ventajaP1 = false;
        boolean ventajaP2 = false;
        boolean P1Win = false;
        boolean P2Win = false;
        Scanner entrada = new Scanner(System.in);

        System.out.println("Introduce el jugador 1 (P1): ");
        String player1 = entrada.nextLine();

        System.out.println("Introduce el jugador 2 (P2): ");
        String player2 = entrada.nextLine();

        System.out.println("Introduce quien ha marcado punto (P1 o P2): ");

        while (!P1Win && !P2Win) {
            String jugador = entrada.nextLine().toUpperCase();


            if (Objects.equals(jugador, "P1")) {
                contadorP1++;
            } else if (Objects.equals(jugador, "P2")) {
                contadorP2++;
            }

            if (contadorP1 == 3 && contadorP2 == 3) {
                System.out.println("Deuce");
                empate = true;
            }

            if (contadorP1 == 4 && contadorP2 == 3) {
                System.out.println("Ventaja " + player1);
                ventajaP1 = true;
                contadorP2--;
                contadorP1--;
            } else if (contadorP1 == 3 && contadorP2 == 4) {
                System.out.println("Ventaja " + player2);
                ventajaP2 = true;
                contadorP1--;
                contadorP2--;
            }

            if (ventajaP1 && contadorP1 == 4) {
                System.out.println("Ha ganado " + player1);
                P1Win = true;
            } else if (ventajaP2 && contadorP2 == 4) {
                System.out.println("Ha ganado " + player2);
                P2Win = true;
            } else if (contadorP1 ==4 && contadorP2 < 3) {
                System.out.println("Ha ganado " + player1);
                P1Win = true;
            } else if (contadorP2 == 4 && contadorP1 < 3) {
                System.out.println("Ha ganado " + player2);
                P2Win = true;
            }

            for (Map.Entry<Integer, String> P1 : jugador1.entrySet()) {
                if (P1.getKey() == contadorP1) {
                    puntosP1 = P1.getValue();
                }
            }

            for (Map.Entry<Integer, String> P2 : jugador2.entrySet()) {
                if (P2.getKey() == contadorP2) {
                    puntosP2 = P2.getValue();
                }
            }

            if (!victoriaP1 && !victoriaP2 && !empate && !ventajaP1 && !ventajaP2 && !P1Win && !P2Win) {
                System.out.println(player1 + ": " + puntosP1 + " - " + player2 + ": " + puntosP2);
            }
        }
    }

    private static HashMap<Integer, String> inicializarJugador() {
        HashMap<Integer, String> jugador = new HashMap<>();
        jugador.put(0, "Love");
        jugador.put(1, "15");
        jugador.put(2, "30");
        jugador.put(3, "40");
        return jugador;
    }
}


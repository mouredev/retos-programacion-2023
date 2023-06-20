package org.example;

import java.util.*;

public class raclosDev {
    public static void main(String[] args) {
        String[] secuencia = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
        jugarJuego(secuencia);
    }

    public static void jugarJuego(String[] secuencia) {
        int puntuacionP1 = 0;
        int puntuacionP2 = 0;

        for (String punto : secuencia) {
            if (punto.equals("P1")) {
                puntuacionP1++;
            } else if (punto.equals("P2")) {
                puntuacionP2++;
            }

            mostrarPuntuacion(puntuacionP1, puntuacionP2);

            if (puntuacionP1 >= 4 && puntuacionP1 - puntuacionP2 >= 2) {
                System.out.println("Ha ganado el P1");
                break;
            } else if (puntuacionP2 >= 4 && puntuacionP2 - puntuacionP1 >= 2) {
                System.out.println("Ha ganado el P2");
                break;
            }
        }
    }

    public static void mostrarPuntuacion(int puntuacionP1, int puntuacionP2) {
        String[] puntuaciones = {"Love", "15", "30", "40", "Deuce", "Ventaja"};

        if (puntuacionP1 >= 3 && puntuacionP2 >= 3) {
            if (puntuacionP1 == puntuacionP2) {
                System.out.println("Deuce");
            } else if (puntuacionP1 > puntuacionP2) {
                System.out.println("Ventaja P1");
            } else {
                System.out.println("Ventaja P2");
            }
        } else {
            System.out.println(puntuaciones[puntuacionP1] + " - " + puntuaciones[puntuacionP2]);
        }
    }
}

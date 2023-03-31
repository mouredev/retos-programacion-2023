/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
*/

import java.util.Scanner;
import java.util.*;

public class Main {
    public static void main(String[] args) {
            jugar_partida(4);
        }

        public static String toString(char[] lista) {
        StringBuilder constructor =new StringBuilder();
        int longitud_lista = lista.length;
        for(int i = 0; i < longitud_lista; i++) {
            constructor.append(lista[i]);
        }
        String result = constructor.toString();
        return result;
        }

        public static ArrayList<Integer> posiciones_de_letra_palabra(char a, String palabra) {
        ArrayList<Integer> posiciones = new ArrayList();
        for (int i = 0; i < palabra.length(); i++) {
            if (palabra.charAt(i) == a) {
                posiciones.add(i);
            }
        }
        return posiciones;
        }

        public static void jugar_partida(int intentos) {
            String[] PALABRAS ={"escritorio", "ordenador", "libertad", "videojuegos", "jugador", "figura"};
            Scanner scan = new Scanner(System.in);
            int numero_palabra_seleccionada = (int) (Math.random()*PALABRAS.length);
            String palabra_seleccionada = PALABRAS[numero_palabra_seleccionada];
            int longitud_palabra = palabra_seleccionada.length();
            char[] letras_palabra = new char[longitud_palabra];
            int numero_letras_a_quitar = (int)Math.ceil(Math.random()*(longitud_palabra*(double)3/5));
            for(int i = 0; i < longitud_palabra; i++) {
                letras_palabra[i] = palabra_seleccionada.charAt(i);
            }
            while(numero_letras_a_quitar > 0) {
                int posicion_lista = (int) (Math.random()*(PALABRAS.length+1));
                if (letras_palabra[posicion_lista] == '_') {

                } else{
                    letras_palabra[posicion_lista] = '_';
                    numero_letras_a_quitar--;
                }
            }
            String palabra_a_adivinar = toString(letras_palabra);
            String opcion_jugador = "";
            while(intentos > 0) {
                if(opcion_jugador.equals(palabra_seleccionada) || palabra_a_adivinar.equals(palabra_seleccionada)) {
                    System.out.println("Has ganado!!");
                    break;
                } else {
                    System.out.println("Te quedan " +intentos + " intentos");
                    System.out.println("La palabra a adivinar es: ");
                    System.out.println(palabra_a_adivinar);
                    System.out.println("Escriba su respuesta;");

                    opcion_jugador = scan.nextLine();
                    if(opcion_jugador.length() == 1) {
                        if (posiciones_de_letra_palabra(opcion_jugador.charAt(0), palabra_seleccionada).isEmpty()) {
                            intentos--;
                            System.out.println("Has fallado!");
                        } else {
                            for(int i: posiciones_de_letra_palabra(opcion_jugador.charAt(0), palabra_seleccionada)) {
                                letras_palabra[i] = opcion_jugador.charAt(0);
                            }
                            palabra_a_adivinar = toString(letras_palabra);
                            System.out.println("Esa letra si estaba en la palabra!");
                            intentos--;
                        }
                    } else {
                        if(opcion_jugador.equals(palabra_seleccionada)) {
                            System.out.println("Has ganado!!");
                            break;
                        } else {
                            intentos--;
                            System.out.println("Has fallado!");
                        }
                    }
                }



            }
        }



}
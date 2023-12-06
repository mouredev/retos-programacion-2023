package reto13AdivinaLaPalabra;

import java.util.*;

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
public class Cflorezp {

    public static void main(String[] args) {

        //Genera una palabra aleatoria de la lista guardada
        char[] palabraAleatoria = generaPalabraAleatoria().toCharArray();

        int oportunidades = palabraAleatoria.length;

        //Genera las posiciones a ocultar de la palabra
        Random random = new Random();
        HashSet<Integer> posicionesEnBlanco = new HashSet<>();
        while (posicionesEnBlanco.size() < palabraAleatoria.length / 2) {
            posicionesEnBlanco.add(random.nextInt(palabraAleatoria.length));
        }

        System.out.println("Bienvenido a adivina la palabra, tienes " + oportunidades + " oportunidades para ganar");
        System.out.println("La palabra a divinar es...\n");

        do {
            //Imprime la palabra con las posiciones ocultas y asocia la posicion con el valor
            int[] arrayPosiciones = new int[palabraAleatoria.length];
            for (int i = 0; i < palabraAleatoria.length; i++) {
                if (posicionesEnBlanco.contains(i)) {
                    System.out.print("_");
                    arrayPosiciones[i] = 0;
                } else {
                    System.out.print(palabraAleatoria[i]);
                    arrayPosiciones[i] = 1;
                }
            }
            System.out.println();

            //Ingreso de la letra por el usuario
            System.out.println("Digite una letra:");
            Scanner entrada = new Scanner(System.in);
            String letraString = entrada.nextLine();

            letraString = letraString.equals("") ? "@$%" : letraString.toLowerCase();
            //Verifica la palabra completa
            char letra;
            if (letraString.length() > 1) {
                if (letraString.equalsIgnoreCase(String.valueOf(palabraAleatoria))) {
                    System.out.println("!!Ganaste la palabra es: " + letraString);
                    break;
                } else {
                    oportunidades--;
                    System.out.println("No acertaste ahora solo tienes " + oportunidades + " oportunidades");
                }
            } else {
                letra = letraString.charAt(0);
                boolean acierto = false;
                for (int i = 0; i < palabraAleatoria.length; i++) {
                    if (letra == palabraAleatoria[i] && arrayPosiciones[i] == 0) {
                        posicionesEnBlanco.remove(i);
                        arrayPosiciones[i] = 1;
                        acierto = true;
                        System.out.println("¡Acertaste una letra sigue asi!");
                        break;
                    }
                }
                if (posicionesEnBlanco.size() == 0) {
                    System.out.println("!!Ganaste la palabra es: " + String.valueOf(palabraAleatoria));
                    break;
                }
                if (!acierto) {
                    oportunidades--;
                    if (oportunidades == 0) {
                        System.out.println("Perdiste... la palabra era: " + String.valueOf(palabraAleatoria));
                        break;
                    } else {
                        System.out.println("No acertaste ahora solo tienes " + oportunidades + " oportunidades");
                    }
                }
            }
        } while (oportunidades > 0);


    }

    public static String generaPalabraAleatoria() {
        String[] palabras = {"java", "spring", "maven", "hibernate", "angular", "docker", "python", "javascript", "mouredev"};
        Random numeros = new Random();
        int aleatorio = numeros.nextInt(palabras.length);
        return palabras[aleatorio];
    }


}

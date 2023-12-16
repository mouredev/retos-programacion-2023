package reto_47;

import java.util.Scanner;

/*
 * La última semana de 2021 comenzamos la actividad de retos de programación,
 * con la intención de resolver un ejercicio cada semana para mejorar
 * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
 *
 * Crea un programa que calcule los puntos de una palabra.
 * - Cada letra tiene un value asignado. Por ejemplo, en el abecedario
 *   español de 27 letras, la A vale 1 y la Z 27.
 * - El programa muestra el valor de los puntos de cada palabra introducida.
 * - El programa finaliza si logras introducir una palabra de 100 puntos.
 * - Puedes usar la terminal para interactuar con el usuario y solicitarle
 *   cada palabra.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        int acc = 0;

        do {
            int value = 0;
            acc = 0;
            Scanner sc = new Scanner(System.in, "ISO-8859-1");
            System.out.print("Introduzca una palabra para calcular su valor ");
            String word = sc.next().toUpperCase();
            if (word.matches("[A-Z Ñ ÁÉÍÓÚÜ]+")) {
                for (int i = 0; i < word.length(); i++) {
                    value = (int) word.charAt(i) - 64;

                    if (value >= 15) value = value + 1;
                    if (value == 146) value = 15;
                    if (value == 130) value = 1;
                    if (value == 138) value = 5;
                    if (value == 142) value = 9;
                    if (value == 148) value = 16;
                    if (value == 155 || value ==157) value = 22;
                    acc += value;
                }
                
                System.out.println("el valor numérico de la palabra \"" + word + "\" es " + acc);
            } else {
                System.out.println("No se admiten otros caracteres que no sean letras.");
            }

        } while (acc != 100);

    }

}

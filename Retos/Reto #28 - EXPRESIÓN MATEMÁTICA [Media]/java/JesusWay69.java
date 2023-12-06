package reto_28;

import java.util.Scanner;

/**
 * Crea una función que reciba una expresión matemática (String) y compruebe si
 * es correcta. -Retornará true o false.
 * -Para que una expresión matemática sea
 * correcta debe poseer un número, una operación y otro número separados por
 * espacios.
 * 
 * -Tantos números y operaciones como queramos.
 * 
 * -Números positivos, negativos, enteros o decimales.
 * 
 * -Operaciones soportadas: + - * / %
 * 
 * Ejemplos: "5 + 6 / 7 - 4" -> true "5 a 6" -> false
 *
 * @author jesus
 */

public class JesusWay69 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in, "ISO-8859-1");
        String operacion;
        System.out.print("Introduzca operación: ");
        operacion = sc.nextLine().trim();
        System.out.println(operacion + " --> " + operacionCorrecta(operacion));

    }

    public static boolean operacionCorrecta(String er) {
        return er.matches("(^-?[0-9]+\\.[0-9]+|-?[0-9]+)[\\s]+(.+|-|.*|/|%)[\\s]+(-?[0-9]+\\.[0-9]+|-?[0-9]+$)*");
    }

}

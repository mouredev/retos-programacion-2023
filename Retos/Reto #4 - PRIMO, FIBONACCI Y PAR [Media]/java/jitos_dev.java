package reto4.java;

 /* Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Número primo: solo si es divisible entre 1 y entre sí mismo
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

public class jitos_dev {

    public static void main(String[] args) {
        String result1 = checkNumber(2);
        String result2 = checkNumber(7);
        String result3 = checkNumber(55);
        String result4 = checkNumber(73);

        System.out.println(result1);
        System.out.println(result2);
        System.out.println(result3);
        System.out.println(result4);
    }

    private static String checkNumber(int number) {
        String message = String.valueOf(number);

        //Si es primo
        message += isPrimo(number) ? " es primo, " : " no es primo, ";

        //Si es fibonacci
        message += isFibonacci(number) ? "fibonacci " : "no es fibonacci ";

        //Si es par
        message += (number % 2 == 0) ? "y es par" : "y es impar";

        return message;
    }

    private static boolean isPrimo(int number) {
        if (number == 0 || number == 1)
            return false;

        for (int i = 2; i < number / 2; i++) {
            if (number % i == 0)
                return false;
        }

        return true;
    }

    private static boolean isFibonacci(int number){
        //el número 0 y el número 1 son los primeros de fibonacci
        if (number == 0 || number == 1)
            return true;

        int previous = 1;
        int later = 1;
        int fibonacci;

        while (true) {
            fibonacci = previous + later;

            //Si el número es mayor es que no es fibonacci por que se ha pasado
            if (fibonacci > number)
                return false;

            //Si el número es igual es que si es fibonacci
            if (fibonacci == number)
                return true;

            //el número anterior le damos el valor del posterior para adelantar una posición
            previous = later;

            //al número posterior le damos el valor de fibonacci para actualizarlo en la siguiente vuelta
            later = fibonacci;
        }

    }
}

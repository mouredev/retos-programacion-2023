/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
public class reto00_FizzBuzz {
    private static void inicio() {
        for (int intCont = 1; intCont <= 100; intCont++) {
            if (intCont % 15 == 0) {
                System.out.println("FizzBuzz");
            } else if (intCont % 5 == 0) {
                System.out.println("Buzz");
            } else if (intCont % 3 == 0) {
                System.out.println("Fizz");
            } else {
                System.out.println(intCont);
            }
        }
    }

    public static void main(String[] args) {
        inicio();
    }
}

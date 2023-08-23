/*
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
 */

import java.util.stream.IntStream;

public class Darubiano {

    static void fizzBuzzJunior() {
        for (int number = 1; number <= 100; number++) {
            if (number % 3 == 0 && number % 5 == 0) {
                System.out.println("fizzbuzz");
            } else if (number % 3 == 0) {
                System.out.println("fizz");
            } else if (number % 5 == 0) {
                System.out.println("buzz");
            } else {
                System.out.println(number);
            }
        }
    }

    static void fizzBuzzSenior() {
        for (int number = 1; number <= 100; number++) {
            String output = "";
            output = (number % 3 == 0 ? "fizz" : "") + (number % 5 == 0 ? "buzz" : "");
            System.out.println(output.isEmpty() ? number : output);
        }
    }

    static void fizzBuzzChatgpt() {
        IntStream.rangeClosed(1, 100)
                .forEach(number -> {
                    String output = "";
                    output = (number % 3 == 0 ? "fizz" : "") + (number % 5 == 0 ? "buzz" : "");
                    System.out.println(output.isEmpty() ? number : output);
                });
    }

    public static void main(String[] args) {
        // * Solucion junior
        fizzBuzzJunior();

        // * Solucion senior
        fizzBuzzSenior();

        // * Solucion chatgpt 👀
        fizzBuzzChatgpt();
    }
}

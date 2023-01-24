<<<<<<< HEAD

/*
*  Autor: Valentin Lujambio (pachulujambio - github)
 * Fecha: 02/01/2022 
 * Version: 1.0.0
 *                      Enunciado:
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

class RetoFizzBuzz {

    public static void main(String... args) {
        for (int i = 1; i <= 100; i++) {
            System.out.println(
                    (i % 3 == 0 && i % 5 == 0) ? "fizzbuzz" : (i % 5 == 0) ? "buzz" : (i % 3 == 0) ? "fizz" : i);
        }
    }
}

class RetoFizzBuzzSecundario {

    // Misma finalidad, solo que el usuario define el número máximo e invoca una
    // función para que el main este mas limpio

    public static void FizzBuzzFunction(int numMax) {
        for (int i = 1; i <= numMax; i++) {
            System.out.println(
                    (i % 3 == 0 && i % 5 == 0) ? "fizzbuzz" : (i % 5 == 0) ? "buzz" : (i % 3 == 0) ? "fizz" : i);
        }
    }

    public static void main(String... args) {
        FizzBuzzFunction(100);
    }
=======

/*
*  Autor: Valentin Lujambio (pachulujambio - github)
 * Fecha: 02/01/2022 
 * Version: 1.0.0
 *                      Enunciado:
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

class RetoFizzBuzz {

    public static void main(String... args) {
        for (int i = 1; i <= 100; i++) {
            System.out.println(
                    (i % 3 == 0 && i % 5 == 0) ? "fizzbuzz" : (i % 5 == 0) ? "buzz" : (i % 3 == 0) ? "fizz" : i);
        }
    }
}

class RetoFizzBuzzSecundario {

    // Misma finalidad, solo que el usuario define el número máximo e invoca una
    // función para que el main este mas limpio

    public static void FizzBuzzFunction(int numMax) {
        for (int i = 1; i <= numMax; i++) {
            System.out.println(
                    (i % 3 == 0 && i % 5 == 0) ? "fizzbuzz" : (i % 5 == 0) ? "buzz" : (i % 3 == 0) ? "fizz" : i);
        }
    }

    public static void main(String... args) {
        FizzBuzzFunction(100);
    }
>>>>>>> 0854228e3df9e32435ff9f79907d1d6423da2a64
}
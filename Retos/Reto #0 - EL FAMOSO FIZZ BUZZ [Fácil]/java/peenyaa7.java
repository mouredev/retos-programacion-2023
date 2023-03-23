public class peenyaa7 {

    /*
     * Escribe un programa que muestre por consola (con un print) los
     * números de 1 a 100 (ambos incluidos y con un salto de línea entre
     * cada impresión), sustituyendo los siguientes:
     * - Múltiplos de 3 por la palabra "fizz".
     * - Múltiplos de 5 por la palabra "buzz".
     * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
     */
    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            String output = "";
            if (i % 3 == 0 && i % 5 == 0) {
                output = "fizzbuzz";
            } else if (i % 3 == 0) {
                output = "fizz";
            } else if (i % 5 == 0) {
                output = "buzz";
            } else {
                output = String.valueOf(i);
            }
            System.out.println(output);
        }
    }

}
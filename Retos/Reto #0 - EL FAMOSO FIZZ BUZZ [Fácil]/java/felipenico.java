
/**
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *
 * @author Felipe Niño Cortes
 */
public class felipenico {

    public static void main(String[] args) {
        imprimir();
    }

    public static void imprimir() {
        for (int i = 0; i < 101; i++) {
            if ((i % 3 == 0) && (i % 5 == 0)) {
                System.out.println("fizzbuzz");
            } else if (i % 3 == 0) {
                System.out.println("fizz");
            } else if (i % 5 == 0) {
                System.out.println("buzz");
            }
        }
    }
}

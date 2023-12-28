
/* RETO 40: TABLA DE MULTIPLICAR
 * Crea un programa que sea capaz de solicitarte un número y se encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

public class Nutegreen {

    private static void tablaMultiplicar(int numero) {
        System.out.println("Tabla de multiplicar del número " + numero);
        for (int i = 1; i < 11; i++) {
            System.out.println(numero + " x " + i + " = " + (numero * i));
        }
    }

    public static void main(String[] args) {
        if (args == null || args.length != 1) {
            System.out.println("Error: Debe indicar el número de la tabla de multiplicar");
            return;
        }
        try {
            int numero = Integer.parseInt(args[0]);
            tablaMultiplicar(numero);
        } catch (NumberFormatException e) {
            System.out.println("Error: El parámetro indicado no es válido. Debe ser un número");
        }
    }
}
/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */

import java.util.Scanner;

public class lz4n {
    public static void main(String[] agrs) {
        int longitudLado;

        //Pido la longitud del lado
        System.out.print("Longitud del lado: ");
        longitudLado = new Scanner(System.in).nextInt();

        //Dibujo la espiral
        System.out.println("═".repeat(longitudLado -1) + "╗");
        for (int fila = 0; longitudLado - 2 * fila -3 >= 0; fila++) {
            System.out.println("║".repeat(fila)
                    + "╔"
                    + "═".repeat(longitudLado - 2 * fila -3)
                    + "╗"
                    + "║".repeat(fila +1));
        }
        for (int fila = longitudLado / 2 -1; fila >= 0; fila--) {
            System.out.println("║".repeat(fila)
                    + "╚"
                    + "═".repeat(longitudLado - 2 * fila -2)
                    + "╝"
                    + "║".repeat(fila));
        }
    }
}

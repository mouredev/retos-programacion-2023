/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *
 *  Resultado: 1.302.790
 */

import java.text.NumberFormat;

public class AnNavNicolas {

    public static void main(String[] args) {
        String[] abaco = {"O---OOOOOOOO",
                "OOO---OOOOOO",
                "---OOOOOOOOO",
                "OO---OOOOOOO",
                "OOOOOOO---OO",
                "OOOOOOOOO---",
                "---OOOOOOOOO"};
        System.out.println(calculoAbaco(abaco));
    }

    private static String calculoAbaco(String[] numero) {
        StringBuilder total = new StringBuilder();
        for (String valor : numero) {
            total.append(valor.split("---")[0].length());
        }
        NumberFormat nf = NumberFormat.getInstance();
        return nf.format(Long.valueOf(total.toString()));
    }

}

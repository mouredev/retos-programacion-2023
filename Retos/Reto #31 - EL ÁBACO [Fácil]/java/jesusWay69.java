package reto_31;

import java.text.NumberFormat;

/**
 * Crea una función que sea capaz de leer el número representado por el ábaco. -
 * El ábaco se representa por un array con 7 elementos. - Cada elemento tendrá 9
 * "O" (aunque habitualmente tiene 10 para realizar operaciones) para las
 * cuentas y una secuencia de "---" para el alambre. - El primer elemento del
 * array representa los millones, y el último las unidades. - El número en cada
 * elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado: ["O---OOOOOOOO", "OOO---OOOOOO",
 * "---OOOOOOOOO", "OO---OOOOOOO", "OOOOOOO---OO", "OOOOOOOOO---",
 * "---OOOOOOOOO"]
 *
 * Resultado: 1.302.790
 *
 * @author jesus
 */
public class jesusWay69 {

    public static void main(String[] args) {
        String[] abacus = {
            "O---OOOOOOOO",
            "OOO---OOOOOO",
            "---OOOOOOOOO",
            "OO---OOOOOOO",
            "OOOOOOO---OO",
            "OOOOOOOOO---",
            "---OOOOOOOOO"};
        translator(abacus);
    }

    private static void translator(String[] abacus) {
        StringBuilder sum = new StringBuilder();
        NumberFormat num = NumberFormat.getNumberInstance();
        for (String row : abacus) {

            for (int index = 0; index < row.length(); index += 1) {

                if (row.charAt(index) == '-') {

                    sum.append(index);
                    break;
                    
                } if (row.startsWith("---")) 
                    sum.append(index);
              
            }

        }

        System.out.println(num.format(Integer.parseInt(sum.toString())));
    }

}

package vandresca;

import java.text.NumberFormat;

/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar
 *   operaciones) para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a
 *   la izquierda del alambre.
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
public class vandresca {

    static String[] abacus = {
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOO0---",
        "---OOOOOOOOO"
    };

    public static void main(String[] args) {
        print("Este es el ábaco: ");
        Arrays.stream(abacus).forEach(line -> print("\t" + line));
        print("\nResultado: " + formatNumber(extractNumberFromAbacus(abacus)));
    }

    public static String extractNumberFromAbacus(String[] abacus){
        StringBuilder stringBuilder = new StringBuilder();
        Arrays.stream(abacus).forEach(line -> {
            stringBuilder.append(line.indexOf("---"));
        });
        return stringBuilder.toString();
    }

    public static String formatNumber(String number){
        Locale locale = new Locale.Builder().setLanguage("es").
            setRegion("ES").build();
        NumberFormat formatter = NumberFormat.getInstance(locale);
        return formatter.format(Long.valueOf(number.toString()));
    }

    public static void print(String text) {
        System.out.println(text);
    }
}

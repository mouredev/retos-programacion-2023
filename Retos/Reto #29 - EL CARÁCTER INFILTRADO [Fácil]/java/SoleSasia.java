import java.util.ArrayList;

/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres.
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 *
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */

public class Main {
    public static void main(String[] args) {

        System.out.println(infiltratingCharacters("A que no me encuentras", "A qu3-no me encuentres")); // [3, -, e]

    }

    public static Object infiltratingCharacters(String text1, String text2) {
        ArrayList<String> infiltratingCharacters = new ArrayList<>();

        //comprobar longitud
        if (text1.length() != text2.length()) {
            return "Las cadenas de texto no tienen la misma longitud";
        } else {
            //comparar caracteres
            char[] charText1 = text1.toCharArray();
            char[] charText2 = text2.toCharArray();
            for (int i = 0; i < charText1.length; i++) {
                if (charText1[i] != charText2[i]) {
                    String str = String.valueOf(charText2[i]);
                    infiltratingCharacters.add(str);
                }
            }
            return infiltratingCharacters;
        }
    }
}

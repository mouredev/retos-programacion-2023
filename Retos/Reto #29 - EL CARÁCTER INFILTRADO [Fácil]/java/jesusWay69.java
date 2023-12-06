package reto_29;

import java.util.ArrayList;

/**
 * Crea una función que reciba dos cadenas de texto casi iguales, a excepción de
 * uno o varios caracteres. La función debe encontrarlos y retornarlos en
 * formato lista/array. - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento. - No se pueden
 * utilizar operaciones propias del lenguaje que lo resuelvan directamente.
 *
 * Ejemplos: - Me llamo mouredev / Me llemo mouredov -> ["e", "o"] - Me
 * llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 *
 * @author jesus
 */
public class jesusWay69 {

    public static void main(String[] args) {
        String text1 = "hola mundo";
        String text2 = "Hola mubdO";
        comparator(text1, text2);

    }

    private static void comparator(String text1, String text2) {

        var differentCharacters = new ArrayList<String>();

        if (text1.length() == text2.length()) {

            for (int i = 0; i < text1.length(); i++) 

                if ((text1.charAt(i) != text2.charAt(i))) 

                    differentCharacters.add(Character.toString(text2.charAt(i)));

        }
     
        if (differentCharacters.isEmpty()) System.out.println("Los 2 textos  son idénticos o tienen diferente longitud");
           
        else   System.out.println(differentCharacters);
       

    }

}

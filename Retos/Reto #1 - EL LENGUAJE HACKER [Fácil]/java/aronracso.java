import java.util.HashMap;
import java.util.Scanner;

/**
 * Reto #1: EL "LENGUAJE HACKER"
 * FÁCIL | Publicación: 02/01/23 | Resolución: 09/01/23
 * 
 * Enunciado
 * 
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
public class aronracso
{
    private static final HashMap<Character, String> DICCIONARIO = crearDiccionario();

    public static void main(String[] args)
    {
        System.out.println("Introduce el texto a transformar y pulsa [enter]:");
     
        try (Scanner scanner = new Scanner(System.in))
        {
            String texto = scanner.nextLine();
            String transformado = transformar(texto);
            
            System.out.println();
            System.out.println(transformado);
        }
    }

    private static String transformar(String texto)
    {
        StringBuilder ret = new StringBuilder();

        texto = texto.toUpperCase();

        for(int i = 0; i < texto.length(); i++)
        {
            char caracter = texto.charAt(i);
            String traduccion = DICCIONARIO.get(caracter);

            if(traduccion != null) {
                ret.append(traduccion);
            } else {
                ret.append(caracter);
            }
        }

        return ret.toString();
    }

    private static HashMap<Character, String> crearDiccionario()
    {
        HashMap<Character, String> dic = new HashMap<>();

        dic.put('A', "4");
        dic.put('B', "I3");
        dic.put('C', "[");
        dic.put('D', ")");
        dic.put('E', "3");
        dic.put('F', "|=");
        dic.put('G', "&");
        dic.put('H', "#");
        dic.put('I', "1");
        dic.put('J', ",_|");
        dic.put('K', ">|");
        dic.put('L', "1");
        dic.put('M', "/\\/\\");
        dic.put('N', "^/");
        dic.put('O', "0");
        dic.put('P', "|*");
        dic.put('Q', "(_,)");
        dic.put('R', "I2");
        dic.put('S', "5");
        dic.put('T', "7");
        dic.put('U', "(_)");
        dic.put('V', "\\/");
        dic.put('W', "\\/\\/");
        dic.put('X', "><");
        dic.put('Y', "j");
        dic.put('Z', "2");
        dic.put('1', "L");
        dic.put('2', "R");
        dic.put('3', "E");
        dic.put('4', "A");
        dic.put('5', "S");
        dic.put('6', "b");
        dic.put('7', "T");
        dic.put('8', "B");
        dic.put('9', "g");
        dic.put('0', "o");

        return dic;
    }
}
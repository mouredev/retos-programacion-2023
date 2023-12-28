import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

    /*
     * Escribe un programa que reciba un texto y transforme lenguaje natural a
     * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
     *  se caracteriza por sustituir caracteres alfanuméricos.
     * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
     *   con el alfabeto y los números en "leet".
     *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
     */

    //PRE  -- recibe texto por pantalla, mayusculas o minusculas, con numeros o letras.
    //POST -- cadena de texto en formato "leet".

    public static final Map<Character, String> map = new HashMap<>();

    static {
        map.put('a', "4");
        map.put('b', "I3");
        map.put('c', "[");
        map.put('d', ")");
        map.put('e', "3");
        map.put('f', "|=");
        map.put('g', "&");
        map.put('h', "#");
        map.put('i', "1");
        map.put('j', ",_|");
        map.put('k', ">|");
        map.put('l', "1");
        map.put('m', "/\\/\\");
        map.put('n', "^/");
        map.put('o', "0");
        map.put('p', "|*");
        map.put('q', "(_,)");
        map.put('r', "I2");
        map.put('s', "5");
        map.put('t', "7");
        map.put('u', "(_)");
        map.put('v', "\\/");
        map.put('w', "\\/\\/");
        map.put('x', "><");
        map.put('y', "j");
        map.put('1', "L");
        map.put('2', "R");
        map.put('3', "E");
        map.put('4', "A");
        map.put('5', "S");
        map.put('6', "b");
        map.put('7', "T");
        map.put('8', "B");
        map.put('9', "g");
        map.put('0', "o");

    }

    public static void main(String[] args) {
        String sInput = stringInput();
        System.out.println(translateToLeet(sInput));
    }

    private static String translateToLeet(String sInput) {
        StringBuilder bld = new StringBuilder();
        for (int i = 0; i < sInput.length(); i++) {
            bld.append(translateChar(sInput.charAt(i)));
        }
        return bld.toString();
    }

    private static String translateChar(char charIn) {
        return map.containsKey(charIn) ? map.get(charIn) : " ";
    }

    private static String stringInput() {
        System.out.println ("Por favor, introduzca una cadena por teclado: ");
        Scanner inputScanner = new Scanner (System.in); //Creación de un objeto Scanner
        return inputScanner.nextLine().toLowerCase(); //Invocamos un método sobre un objeto Scanner
    }
}
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class HackerLanguage {

    public static void hackerLanguage(){
        Map leetTable = getLeetTable();

        Scanner userInput = new Scanner(System.in);
        System.out.println("Ingresa una Frase: ");

        String alphabeticPhrase = userInput.nextLine().toUpperCase();

        for (int i = 0; i< alphabeticPhrase.toCharArray().length; i++){
            System.out.print(leetTable.get(alphabeticPhrase.toCharArray()[i]));
        }
    }

    private static Map getLeetTable() {

        Map table = new HashMap();

        table.put('A',"4");
        table.put('B',"|3");
        table.put('C',"{");
        table.put('D',"|}");
        table.put('E',"3");
        table.put('F',"|=");
        table.put('G',"[");
        table.put('H',"#");
        table.put('I',"|");
        table.put('J',"_|");
        table.put('K',"1<");
        table.put('L',"1");
        table.put('M',"|V|");
        table.put('N',"/V");
        table.put('O',"()");
        table.put('P',"|O");
        table.put('Q',"9");
        table.put('R',"12");
        table.put('S',"$");
        table.put('T',"7");
        table.put('U',"|_|");
        table.put('V',"\\/");
        table.put('W',"(/\\)");
        table.put('X',"%");
        table.put('Y'," ¥");
        table.put('Z',"7_");
        table.put('0', "C");
        table.put('1', "L");
        table.put('2', "Z");
        table.put('3', "E");
        table.put('4', "h");
        table.put('5', "S");
        table.put('6', "b");
        table.put('7', "T");
        table.put('8', "B");
        table.put('9', "g");
        table.put(' ', " ");

        return table;
    }
}

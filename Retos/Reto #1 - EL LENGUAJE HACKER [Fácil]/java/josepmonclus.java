import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class josepmonclus {
    public static final Map<Character, String> hackerMap = new HashMap<Character, String>();

    static {
      hackerMap.put('a', "4");
      hackerMap.put('b', "I3");
      hackerMap.put('c', "[");
      hackerMap.put('d', ")");
      hackerMap.put('e', "3");
      hackerMap.put('f', "|=");
      hackerMap.put('g', "&");
      hackerMap.put('h', "#");
      hackerMap.put('i', "1");
      hackerMap.put('j', ",_|");
      hackerMap.put('k', ">|");
      hackerMap.put('l', "1");
      hackerMap.put('m', "/\\/\\");
      hackerMap.put('n', "^/");
      hackerMap.put('o', "0");
      hackerMap.put('p', "|*");
      hackerMap.put('q', "(_,)");
      hackerMap.put('r', "I2");
      hackerMap.put('s', "5");
      hackerMap.put('t', "7");
      hackerMap.put('u', "(_)");
      hackerMap.put('v', "\\/");
      hackerMap.put('w', "\\/\\/");
      hackerMap.put('x', "><");
      hackerMap.put('y', "j");
      hackerMap.put('1', "L");
      hackerMap.put('2', "R");
      hackerMap.put('3', "E");
      hackerMap.put('4', "A");
      hackerMap.put('5', "S");
      hackerMap.put('6', "b");
      hackerMap.put('7', "T");
      hackerMap.put('8', "B");
      hackerMap.put('9', "g");
      hackerMap.put('0', "o");
  
    }

    private static String traslate(String toTranslate) {
        StringBuilder leetText = new StringBuilder("");

        for(int i = 0; i < toTranslate.length(); i++){
            if(hackerMap.containsKey(toTranslate.charAt(i))) {
                leetText.append(hackerMap.get(toTranslate.charAt(i)));
            } else {
                leetText.append(toTranslate.charAt(i));
            }
            
        }
        
        return leetText.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter text: ");
        String toTranslate = sc.nextLine();

        System.out.printf("Leet: %s", traslate(toTranslate));

        sc.close();
    }
}
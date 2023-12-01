/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

import java.util.HashMap;// Importing "Hashmap" pack.
import java.util.Scanner;

public class Adrian01cst {
   public static void main(String[] args) {
      Scanner input = new Scanner(System.in);

      String text;
      String new_text = "";

      System.out.print("Type any text: ");
      text = input.nextLine();

      // Original text to character array.
      char[] array_of_text;
      array_of_text = text.toCharArray();

      HashMap<Character, String> my_hash_map = new HashMap<>();
      // Adding items to "HashMap".
      my_hash_map.put('A', "4"); my_hash_map.put('B', "I3"); my_hash_map.put('C',"["); my_hash_map.put('D', ")");
      my_hash_map.put('E', "3"); my_hash_map.put('F', "|="); my_hash_map.put('G', "&"); my_hash_map.put('H', "#");
      my_hash_map.put('I', "1"); my_hash_map.put('J', ",_|"); my_hash_map.put('K', ">|"); my_hash_map.put('L', "1");
      my_hash_map.put('M', "/\\/\\"); my_hash_map.put('N', "^/"); my_hash_map.put('O', "0"); my_hash_map.put('P', "|*");
      my_hash_map.put('Q', "(_,)"); my_hash_map.put('R', "I2"); my_hash_map.put('S', "5"); my_hash_map.put('T', "7");
      my_hash_map.put('U', "(_)"); my_hash_map.put('V', "\\/"); my_hash_map.put('W', "\\/\\/"); my_hash_map.put('X', "><");
      my_hash_map.put('Y', "j"); my_hash_map.put('Z', "2"); my_hash_map.put('0', "o"); my_hash_map.put('1', "L");
      my_hash_map.put('2', "R"); my_hash_map.put('3', "E"); my_hash_map.put('4', "A"); my_hash_map.put('5', "S");
      my_hash_map.put('6', "b"); my_hash_map.put('7', "T"); my_hash_map.put('8', "B"); my_hash_map.put('9', "g");

      for(char i : array_of_text) {
         char upper_char = Character.toUpperCase(i);
         if(my_hash_map.containsKey(upper_char)) {
            new_text += my_hash_map.get(upper_char);
         } else {
            new_text += i;
         }
      }
      System.out.println("\n" + "The converted text is: " + new_text);
   }
}
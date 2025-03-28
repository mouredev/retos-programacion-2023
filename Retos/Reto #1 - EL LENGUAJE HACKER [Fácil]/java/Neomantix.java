/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

import java.util.HashMap;

import javax.swing.JOptionPane;

public class Neomantix {

	public static void main(String[] args) {

		String myText = JOptionPane.showInputDialog(null, "Introduce una cadena de texto: ").toUpperCase().trim();
		
		HashMap<Character, String> leetDictionary = new HashMap<Character, String>(26);
		leetDictionary.put('A',"4");
		leetDictionary.put('B',"I3");
		leetDictionary.put('C',"[");
		leetDictionary.put('D',")");
		leetDictionary.put('E',"3");
		leetDictionary.put('F',"|=");
		leetDictionary.put('G',"&");
		leetDictionary.put('H',"#");
		leetDictionary.put('I',"1");
		leetDictionary.put('J',",_|");
		leetDictionary.put('K',">|");
		leetDictionary.put('L',"1");
		leetDictionary.put('M',"^/");
		leetDictionary.put('O',"0");
		leetDictionary.put('P',"|*");
		leetDictionary.put('Q',"(_,)");
		leetDictionary.put('R',"|2");
		leetDictionary.put('S',"5");
		leetDictionary.put('T',"7");
		leetDictionary.put('U',"(_)");
		leetDictionary.put('V',"\\/");
		leetDictionary.put('W',"\\/\\/");
		leetDictionary.put('X',"><");
		leetDictionary.put('Y',"j");
		leetDictionary.put('Z',"2");
		
		StringBuilder hackText = new StringBuilder();
		
		for (int i=0; i<myText.length(); i++) {
			if(leetDictionary.containsKey(myText.charAt(i))) {
				hackText.append(leetDictionary.get(myText.charAt(i)));
			} else {
				hackText.append(myText.charAt(i));
			}
		}
		
		JOptionPane.showMessageDialog(null, hackText.toString());
		
	}

}
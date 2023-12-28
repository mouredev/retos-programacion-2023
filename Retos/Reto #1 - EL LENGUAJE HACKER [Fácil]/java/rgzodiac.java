package retos;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.AbstractMap;
import java.util.Map;

/*
 * Reto #1: EL "LENGUAJE HACKER"
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class Reto1 {

	static Map<String, String> leetAlphabet = Map.ofEntries(
			new AbstractMap.SimpleEntry<String, String>("A", "4"),
			new AbstractMap.SimpleEntry<String, String>("B", "I3"),
			new AbstractMap.SimpleEntry<String, String>("C", "["),
			new AbstractMap.SimpleEntry<String, String>("D", ")"),
			new AbstractMap.SimpleEntry<String, String>("E", "3"),
			new AbstractMap.SimpleEntry<String, String>("F", "|="),
			new AbstractMap.SimpleEntry<String, String>("G", "&"),
			new AbstractMap.SimpleEntry<String, String>("H", "#"),
			new AbstractMap.SimpleEntry<String, String>("I", "1"),
			new AbstractMap.SimpleEntry<String, String>("J", ",_|"),
			new AbstractMap.SimpleEntry<String, String>("K", ">|"),
			new AbstractMap.SimpleEntry<String, String>("L", "1"),
			new AbstractMap.SimpleEntry<String, String>("M", "/\\/\\"),
			new AbstractMap.SimpleEntry<String, String>("N", "^/"),
			new AbstractMap.SimpleEntry<String, String>("O", "0"),
			new AbstractMap.SimpleEntry<String, String>("P", "|*"),
			new AbstractMap.SimpleEntry<String, String>("Q", "(_,)"),
			new AbstractMap.SimpleEntry<String, String>("R", "I2"),
			new AbstractMap.SimpleEntry<String, String>("S", "5"),
			new AbstractMap.SimpleEntry<String, String>("T", "7"),
			new AbstractMap.SimpleEntry<String, String>("U", "(_)"),
			new AbstractMap.SimpleEntry<String, String>("V", "\\/"),
			new AbstractMap.SimpleEntry<String, String>("W", "\\/\\/"),
			new AbstractMap.SimpleEntry<String, String>("X", "><"),
			new AbstractMap.SimpleEntry<String, String>("Y", "j"),
			new AbstractMap.SimpleEntry<String, String>("Z", "2"),
			new AbstractMap.SimpleEntry<String, String>("1", "L"),
			new AbstractMap.SimpleEntry<String, String>("2", "R"),
			new AbstractMap.SimpleEntry<String, String>("3", "E"),
			new AbstractMap.SimpleEntry<String, String>("4", "A"),
			new AbstractMap.SimpleEntry<String, String>("5", "S"),
			new AbstractMap.SimpleEntry<String, String>("6", "b"),
			new AbstractMap.SimpleEntry<String, String>("7", "T"),
			new AbstractMap.SimpleEntry<String, String>("8", "B"),
			new AbstractMap.SimpleEntry<String, String>("9", "g"),
			new AbstractMap.SimpleEntry<String, String>("0", "o"));

	public static void main(String[] args) throws IOException {

		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		String naturalText = reader.readLine();
		System.out.println(toHackerText(naturalText));
	}

	private static String toHackerText(String naturalText) {

		StringBuilder sb = new StringBuilder();
		for (char naturalWord : naturalText.toCharArray()) {
			String naturalWordStr = String.valueOf(naturalWord);
			String leetWord = leetAlphabet.get(naturalWordStr.toUpperCase());
			sb.append(leetWord != null ? leetWord : naturalWordStr);
		}

		return sb.toString();
	}

}

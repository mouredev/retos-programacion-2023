/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

class Main {
	// Getting all the cahracters for use
	public static List<String> characterSet = new ArrayList<>(Arrays.asList( "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"));
	static List<String> mayus = Arrays.asList("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z");
	static List<String> numbers = Arrays.asList("0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
	static List<String> simbols = Arrays.asList("|", "!", "\"", "#", "$", "%", "&", "/", "(", ")", "=", "?", "'", "\\", "+", "-", "*", "{", "}", "[", "]", ";", ":", "_", "^");

	public static void main(String[] args) {
		// Asking the user for the selected information
		Scanner sc = new Scanner(System.in);
		System.out.print("Ingresar la longuitud: ");
		int passLength = Integer.parseInt(sc.nextLine());
		System.out.print("Tiene mayusculas?(y/n) ");
		String hasMayus = sc.nextLine();
		System.out.print("Tiene números?(y/n) ");
		String hasNumbers = sc.nextLine();
		System.out.print("tiene símbolos?(y/n) ");
		String hasSimbols = sc.nextLine();
		sc.close();
		// Cheking the different flags for character use
		if (hasMayus.equals("y")) {
			concatenate(mayus);
		}
		if (hasNumbers.equals("y")) {
			concatenate(numbers);
		}
		if (hasSimbols.equals("y")) {
			concatenate(simbols);
		}
		//System.out.println(characterSet);
		passLength = checkLength(passLength);
		String password = "";
		for (int i = 0; i < passLength; i++) {
			// Looping through to obtain the password
			int index = (int) (Math.random() * 1000) % characterSet.size();
			password += characterSet.get(index);
		}
		System.out.println(password);
    }

	// Function to concatenate the new set of chracters with the actual
	static void concatenate(List<String> lista) {
		for (String character : lista) {
			characterSet.add(character);
		}
	}

	// Function to determine the size of the password, keeping the restrictions in check
	static int checkLength(int passwordLength) {
		if (passwordLength < 8) {
			return 8;
		} else if (passwordLength > 16) {
			return 16;
		} else {
		return passwordLength;
		}
	}
}
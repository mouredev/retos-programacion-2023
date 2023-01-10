import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class carSneider99 {

	private static String translate (String text, Map<String, String> diccionario) {

		StringBuilder translateText = new StringBuilder();

		for (int n = 0; n < text.length (); n ++) {
			String letter = String.valueOf(text.charAt(n));
			String letterTranslate = diccionario.get(letter.toLowerCase());

			if (letterTranslate == null)
				letterTranslate = letter;

			translateText.append(letterTranslate);
		}

		return String.valueOf(translateText);
	}

	public static void main (String[] args){

		Map<String,String> alphabetLeet = new HashMap<>();

		alphabetLeet.put("a","4");
		alphabetLeet.put("b","I3");
		alphabetLeet.put("c","[");
		alphabetLeet.put("d",")");
		alphabetLeet.put("e","3");
		alphabetLeet.put("f","|=");
		alphabetLeet.put("g","&");
		alphabetLeet.put("h","#");
		alphabetLeet.put("i","1");
		alphabetLeet.put("j",",_|");
		alphabetLeet.put("k",">|");
		alphabetLeet.put("l","1");
		alphabetLeet.put("m","/\\/\\");
		alphabetLeet.put("n","^/");
		alphabetLeet.put("o","0");
		alphabetLeet.put("p","|*");
		alphabetLeet.put("q","(_,)");
		alphabetLeet.put("r","|2");
		alphabetLeet.put("s","5");
		alphabetLeet.put("t","7");
		alphabetLeet.put("u","(_)");
		alphabetLeet.put("v","\\/");
		alphabetLeet.put("w","\\/\\/");
		alphabetLeet.put("x","><");
		alphabetLeet.put("y","j");
		alphabetLeet.put("z","2");

		Scanner userInput = new Scanner(System.in);
		System.out.println("Frase a traducir: \n");

		System.out.println("Frase traducida: " + translate(userInput.nextLine(), alphabetLeet));
	}
}
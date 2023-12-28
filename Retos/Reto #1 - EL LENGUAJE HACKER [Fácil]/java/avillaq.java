import java.util.*;

public class avillaq {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String line = scan.nextLine();
		
		ArrayList<String> arrayLine = new ArrayList<String>();
		for (int i = 0; i < line.length(); i++) 
			arrayLine.add(""+line.charAt(i));

		HashMap<String, String> alphabet = new HashMap<String, String>();
		alphabet.put("a", "4");
		alphabet.put("b", "I3");
		alphabet.put("c", "[");
		alphabet.put("d", ")");
		alphabet.put("e", "3");
		alphabet.put("f", "|=");
		alphabet.put("g", "&");
		alphabet.put("h", "#");
		alphabet.put("i", "1");
		alphabet.put("j", ",_|");
		alphabet.put("k", ">|");
		alphabet.put("l", "1");
		alphabet.put("m", "/\\/\\");
		alphabet.put("n", "^/");
		alphabet.put("o", "0");
		alphabet.put("p", "|*");
		alphabet.put("q", "(_,)");
		alphabet.put("r", "I2");
		alphabet.put("s", "5");
		alphabet.put("t", "7");
		alphabet.put("u", "(_)");
		alphabet.put("v", "\\/");
		alphabet.put("w", "\\/\\/");
		alphabet.put("x", "><");
		alphabet.put("y", "j");
		alphabet.put("z", "2");

		alphabet.put("1", "L");
		alphabet.put("2", "R");
		alphabet.put("3", "E");
		alphabet.put("4", "A");
		alphabet.put("5", "S");
		alphabet.put("6", "b");
		alphabet.put("7", "T");
		alphabet.put("8", "B");
		alphabet.put("9", "g");
		alphabet.put("0", "o");
		
		for (int i = 0; i < arrayLine.size(); i++) {
			arrayLine.set(i, alphabet.get(arrayLine.get(i)));
			System.out.print(arrayLine.get(i));
		}
	}
}

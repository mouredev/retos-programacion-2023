/**
 * 
 */
package ec.com.vijes.retos;

import ec.com.vijes.retos.common.HackerUtil;

/**
 * @author vijes
 *
 */
public class VictorJaramillo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
        hackerTextReto1();
	}
	
	/**
	 * 
	 */
	public static void hackerTextReto1() {
		String textTest = "Hola mundo 1987";
		String textHacked = "";
		for (int i = 0; i < textTest.length(); i++) {
			System.out.println(textTest.substring(i, i+1));
			textHacked = textHacked.concat(HackerUtil.getLetterHacked(textTest.substring(i, i+1)));
		}
		System.out.println("Texto hackeado:");
		System.out.println(textHacked);
	}

    /**
     * Metodo para obtener la letra hackeada.
     */
    public static String getLetterHacked(String letter){
		switch (letter.toUpperCase()) {
		case "A":
			return "4";
		case "B":
			return "I3";
		case "C":
			return "[";
		case "D":
			return ")";
		case "E":
			return "3";
		case "F":
			return "|=";
		case "G":
			return "&";
		case "H":
			return "#";
		case "I":
			return "1";
		case "J":
			return ",_|";
		case "K":
			return ">|";
		case "L":
			return "£";// porque el 1 ya se encuentra con la I para no causar confusion.
		case "M":
			return "[V]";
		case "N":
			return "^/";
		case "O":
			return "0";
		case "P":
			return "|*";
		case "Q":
			return "(_,)";
		case "R":
			return "I2";
		case "S":
			return "5";
		case "T":
			return "7";
		case "U":
			return "(_)";
		case "V":
			return "|/";
		case "W":
			return "VV";
		case "X":
			return "><";
		case "Y":
			return "j";
		case "Z":
			return "7_";	
		case "1":
			return "L";	
		case "2":
			return "R";	
		case "3":
			return "E";	
		case "4":
			return "A";	
		case "5":
			return "S";	
		case "6":
			return "b";	
		case "7":
			return "T";	
		case "8":
			return "B";	
		case "9":
			return "g";	
		case "0":
			return "o";
		default:
			return ".-.";
		}
	}
}

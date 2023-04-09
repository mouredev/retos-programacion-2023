import java.util.*;

public class LaijieJi {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String octal = "";
		String hex = "";
		System.out.println("Please, write the decimal number");
		int decimal = sc.nextInt();
		octal = decToOctal(decimal);
		hex = decimalToHexadecimal(decimal);
		System.out.println(decimal + " in Octal is: " + octal + ", and in Hex it is : " + hex);
		sc.close();
	}

	public static String decToOctal(int decimal){
		int over;
		String res = "";
		char[] octals = {'0', '1', '2', '3', '4', '5', '6', '7'};
		while (decimal > 0){
			over = decimal % 8;
			char character = octals[over];
			res = character + res;
			decimal = decimal / 8;
		} 
		return res;
	}

	public static String decimalToHexadecimal(int decimal) {
		int over;
		String hexadecimal = "";
		char[] HexChars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
		while (decimal > 0) {
			over = decimal % 16;
			char caracterHexadecimal = HexChars[over];
			hexadecimal = caracterHexadecimal + hexadecimal;
			decimal = decimal / 16;
		}
		return hexadecimal;
	}
}

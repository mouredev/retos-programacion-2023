import java.util.Scanner;

public class LenguajeHacker {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner entrada = new Scanner (System.in);
		
		System.out.println("Escribe una frase para transformarla a lenguaje Hacker");
		
		String frase = entrada.nextLine().toUpperCase();
		
		for(int i = 0; i < frase.length(); i++) {
			
			switch (frase.charAt(i)) {
			
			case 'A':
				
				System.out.print("4");
				break;
				
			case 'B':
				
				System.out.print("13");
				break;
				
			case 'C':
				
				System.out.print("[");
				break;
				
			case 'D':
				
				System.out.print(")");
				break;
				
			case 'E':
				
				System.out.print("3");
				break;
				
			case 'F':
				
				System.out.print("|=");
				break;
				
			case 'G':
				
				System.out.print("&");
				break;
				
			case 'H':
				
				System.out.print("#");
				break;
				
			case 'I':
				
				System.out.print("1");
				break;
				
			case 'J':
				
				System.out.print(",_|");
				break;
				
			case 'K':
				
				System.out.print(">|");
				break;
				
			case 'L':
				
				System.out.print("1");
				break;
				
			case 'M':
				
				System.out.print("[V]");
				break;
				
			case 'N':
				
				System.out.print("^/");
				break;
				
			case 'O':
				
				System.out.print("0");
				break;
				
			case 'P':
				
				System.out.print("|*");
				break;
				
			case 'Q':
				
				System.out.print("(_,)");
				break;
				
			case 'R':
				
				System.out.print("12");
				break;
				
			case 'S':
				
				System.out.print("5");
				break;
				
			case 'T':
				
				System.out.print("7");
				break;
				
			case 'U':
				
				System.out.print("(_)");
				break;
				
			case 'V':
				
				System.out.print("|/");
				break;
				
			case 'W':
				
				System.out.print("'//");
				break;
				
			case 'X':
				
				System.out.print("><");
				break;
				
			case 'Y':
				
				System.out.print("j");
				break;
				
			case 'Z':
				
				System.out.print("2");
				break;
				
			case '1':
				
				System.out.print("L");
				break;
				
			case '2':
				
				System.out.print("R");
				break;
				
			case '3':
				
				System.out.print("E");
				break;
				
			case '4':
				
				System.out.print("A");
				break;
				
			case '5':
				
				System.out.print("S");
				break;
				
			case '6':
				
				System.out.print("b");
				break;
				
			case '7':
				
				System.out.print("T");
				break;
				
			case '8':
				
				System.out.print("B");
				break;
				
			case '9':
				
				System.out.print("g");
				break;
				
			case '0':
				
				System.out.print("o");
				break;
				
			default:
				
				System.out.print(frase.charAt(i));
				break;

				
				
				
			}
			
		}
		
		entrada.close();

	}

}

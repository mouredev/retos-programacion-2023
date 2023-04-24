import java.util.Scanner;
public class Principal {
	public static void main(String[] args) {
		Scanner lector = new Scanner(System.in);
		String text;
		
		text=lector.nextLine();
		
		String dic[] = new String[]{"4", "I3", "[", ")", "3", "|=", "&", "#", "1",",_|", ">|", "1", "^^", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "|/", "2u","><", "j", "2"};
		for(int i=0;i<text.length();i++){
			switch((text.toUpperCase()).charAt(i)){
			case ' ':System.out.print(" ");break;
			case 'A':System.out.print(dic[0]);break;
			case 'B':System.out.print(dic[1]);break;
			case 'C':System.out.print(dic[2]);break;
			case 'D':System.out.print(dic[3]);break;
			case 'E':System.out.print(dic[4]);break;
			case 'F':System.out.print(dic[5]);break;
			case 'G':System.out.print(dic[6]);break;
			case 'H':System.out.print(dic[7]);break;
			case 'I':System.out.print(dic[8]);break;
			case 'J':System.out.print(dic[9]);break;
			case 'K':System.out.print(dic[10]);break;
			case 'L':System.out.print(dic[11]);break;
			case 'M':System.out.print(dic[12]);break;
			case 'N':System.out.print(dic[13]);break;
			case 'O':System.out.print(dic[14]);break;
			case 'P':System.out.print(dic[15]);break;
			case 'Q':System.out.print(dic[16]);break;
			case 'R':System.out.print(dic[17]);break;
			case 'S':System.out.print(dic[18]);break;
			case 'T':System.out.print(dic[19]);break;
			case 'U':System.out.print(dic[20]);break;
			case 'V':System.out.print(dic[21]);break;
			case 'W':System.out.print(dic[22]);break;
			case 'X':System.out.print(dic[23]);break;
			case 'Y':System.out.print(dic[24]);break;
			case 'Z':System.out.print(dic[25]);break;
			}
		}
	}
}

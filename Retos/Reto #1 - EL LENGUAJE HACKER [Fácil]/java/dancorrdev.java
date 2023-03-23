import java.util.Scanner;

public class dancorrdev {
    public static void main(String[] args) {
         String message;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingresa tu mensaje aqui");
        message = scanner.nextLine();

        changeLetters(message);


    }
    public static void changeLetters(String message) {
        for (int i = 0; i < message.length(); i++) {
            char letter = message.charAt(i);
            hackerLenguageTranslator(letter);
        }
    }

    public static void hackerLenguageTranslator(char letter){
        switch (letter){
            case 'a':
                System.out.print("4");
                break;
            case 'b' :
                System.out.print("I3");
                break;
            case 'c':
                System.out.print("[");
                break;
            case 'd':
                System.out.print(")");
                break;
            case 'e':
                System.out.print("3");
                break;
            case 'f':
                System.out.print("|=");
                break;
            case 'g':
                System.out.print("&");
                break;
            case 'h':
                System.out.print("#");
                break;
            case 'i':
                System.out.print("1");
                break;
            case 'j':
                System.out.print("._|");
                break;
            case 'k':
                System.out.print(">|");
                break;
            case 'l':
                System.out.print("£");
                break;
            case 'm':
                System.out.print("/\\/\\");
                break;
            case 'n':
                System.out.print("^/");
                break;
            case 'o':
                System.out.print("0");
                break;
            case 'p':
                System.out.print("|*");
                break;
            case 'q':
                System.out.print("(_,)");
                break;
            case 'r':
                System.out.print("I2");
                break;
            case 's':
                System.out.print("5");
                break;
            case 't':
                System.out.print("7");
                break;
            case 'u':
                System.out.print("(_)");
                break;
            case 'v':
                System.out.print("\\/");
                break;
            case 'w':
                System.out.print("\\/\\/");
                break;
            case 'x':
                System.out.print("><");
                break;
            case 'y':
                System.out.print("`/");
                break;
            case 'z':
                System.out.print("2");
                break;
            default:
                System.out.print(letter);
                break;
        }
    }

}

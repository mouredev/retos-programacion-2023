import java.util.Scanner;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
public class erosiim {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        var sb = new StringBuffer();
        var textIn = sc.next().toUpperCase();
        for (int i = 0; i < textIn.length(); i++) {
                switch (textIn.charAt(i)){
                    case 'A':
                        sb.append('4');
                        break;
                    case 'B':
                        sb.append("I3");
                        break;
                    case 'C':
                        sb.append('[');
                        break;
                    case 'D':
                        sb.append(')');
                        break;
                    case 'E':
                        sb.append('3');
                        break;
                    case 'F':
                        sb.append("|=");
                        break;
                    case 'G':
                        sb.append('&');
                        break;
                    case 'H':
                        sb.append('#');
                        break;
                    case 'I':
                        sb.append('1');
                        break;
                    case 'J':
                        sb.append("_|");
                        break;
                    case 'K':
                        sb.append(">|");
                        break;
                    case 'L':
                        sb.append('1');
                        break;
                    case 'M':
                        sb.append("/\\/\\");
                        break;
                    case 'N':
                        sb.append("^/");
                        break;
                    case 'O':
                        sb.append('0');
                        break;
                    case 'P':
                        sb.append("|*");
                        break;
                    case 'Q':
                        sb.append("(_,)");
                        break;
                    case 'R':
                        sb.append("I2");
                        break;
                    case 'S':
                        sb.append('5');
                        break;
                    case 'T':
                        sb.append('7');
                        break;
                    case 'U':
                        sb.append("(_)");
                        break;
                    case 'V':
                        sb.append("\\/");
                        break;
                    case 'W':
                        sb.append(')');
                        break;
                    case 'X':
                        sb.append("><");
                        break;
                    case 'Y':
                        sb.append('j');
                        break;
                    case 'Z':
                        sb.append('2');
                        break;
                    default:
                        break;
                }
        }
        System.out.println(sb);
    }
}

import java.io.BufferedReader;
import java.io.InputStreamReader;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class sntxDev {
    public static void main(String[] args) {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        String txt = "";
        try {
            System.out.print("Ingrese el texto: ");
            txt = String.valueOf(entrada.readLine()).toLowerCase();
            for (int i = 0; i < txt.length(); i++) {
                switch (txt.charAt(i)) {
                    case 'a':
                        System.out.print("4");
                        break;
                    case 'b':
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
                        System.out.print(",_|");
                        break;
                    case 'k':
                        System.out.print(">|");
                        break;
                    case 'l':
                        System.out.print("1");
                        break;
                    case 'm':
                        System.out.print("JVI");
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
                        System.out.print("|/");
                        break;
                    case 'w':
                        System.out.print("VV");
                        break;
                    case 'x':
                        System.out.print("><");
                        break;
                    case 'y':
                        System.out.print("j");
                        break;
                    case 'z':
                        System.out.print("2");
                        break;
                    case ' ':
                        System.out.print(" ");
                }
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}

/*
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/
public class Reto01 {
    public static void main(String[] args) throws Exception {
        String texto = "leet";
        traductor(texto);
    }

    public static void traductor(String texto) {
        for (int i = 0; i < texto.length(); i++) {
            char letra = texto.toUpperCase().charAt(i);
            diccionario(letra);
        }
    }

    public static void diccionario(char letra) {
        switch (letra) {
            case 'A':
                System.out.print("4");
                break;
            case 'B':
                System.out.print("|3");
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
                System.out.print("/\\/\\");
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
                System.out.print("I2");
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
                System.out.print("\\/");
                break;
            case 'W':
                System.out.print("\\/\\/");
                break;
            case 'X':
                System.out.print("><");
                break;
            case 'Y':
                System.out.print("j");
                break;
            case 'Z':
                System.out.print("|3");
                break;
            default:
                System.out.print(letra);
            break;
        }
    }
}

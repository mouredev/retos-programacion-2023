import java.util.Scanner;

public class JuanMA0190 {
    /*
    * Escribe un programa que reciba un texto y transforme lenguaje natural a
    * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
    *  se caracteriza por sustituir caracteres alfanuméricos.
    * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
    *   con el alfabeto y los números en "leet".
    *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
    */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese Texto:");
        String texto = sc.nextLine().toLowerCase();
        StringBuilder textEncriptado = new StringBuilder();

        for (int i = 0; i < texto.length(); i++) {
            textEncriptado.append(encriptado(texto.charAt(i)));    
        }

        System.out.println(textEncriptado.toString());
        sc.close();
    }

    public static String encriptado(char caracter){
        switch (caracter) {
            case 'á':
            case 'a':
                return "4";
            case 'b':
                return "I3";
            case 'c':
                return "[";
            case 'd':
                return ")";
            case 'e':
            case 'é':
                return "3";
            case 'f':
                return "|=";
            case 'g':
                return "&";
            case 'h':
                return "#";
            case 'i':
            case 'í':
                return "1";
            case 'j':
                return ",_|";
            case 'k':
                return ">|";
            case 'l':
                return "£";
            case 'm':
                return "/\\/\\";
            case 'n':
            case 'ñ':
                return "^/";
            case 'o':
            case 'ó':
                return "0";
            case 'p':
                return "|*";
            case 'q':
                return "(_,)";
            case 'r':
                return "I2";
            case 's':
                return "5";
            case 't':
                return "7";
            case 'u':
            case 'ú':
            case 'ü':
                return "(_)";
            case 'v':
                return "\\/";
            case 'w':
                return "\\/\\/";
            case 'x':
                return "><";
            case 'y':
                return "j";
            case 'z':
                return "2";
            case '1':
                return "L";
            case '2':
                return "R";
            case '3':
                return "E";
            case '4':
                return "A";
            case '5':
                return "S";
            case '6':
                return "b";
            case '7':
                return "T";
            case '8':
                return "B";
            case '9':
                return "g";
            case '0':
                return "o";
            default:
                return String.valueOf(caracter);
        }
    }
}
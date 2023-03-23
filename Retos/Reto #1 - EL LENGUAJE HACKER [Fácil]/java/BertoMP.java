import java.util.Scanner;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
public class reto01_ElLenguajeHacker {
    static String cambiaCaracter(char chrCaracter) {
        int intIndiceBusqueda = 0;
        boolean blnEncontrado = false;

        char[] chrArrAlfanumerico = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
        String[] strLenguajeLeet = {"4", "|3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/\\", "^/",
                "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2", "o", "L", "R", "E", "A",
                "S", "b", "T", "B", "g"};

        for (int intCont = 0; intCont < chrArrAlfanumerico.length && !blnEncontrado; intCont++) {
            if (chrArrAlfanumerico[intCont] == chrCaracter) {
                blnEncontrado = true;
                intIndiceBusqueda = intCont;
            }
        }

        return strLenguajeLeet[intIndiceBusqueda];
    }
    static String traduceALeet(String strTexto) {
        StringBuilder strTextoReturn = new StringBuilder();
        String strTextoCambiado;

        for (int intCont = 0; intCont < strTexto.length(); intCont++) {
            if (strTexto.charAt(intCont) == 'ñ') {
                strTextoReturn.append("ñ");
            } else if (Character.isLetterOrDigit(strTexto.charAt(intCont))) {
                strTextoCambiado = cambiaCaracter(strTexto.charAt(intCont));
                strTextoReturn.append(strTextoCambiado);
            } else {
                strTextoReturn.append(strTexto.charAt(intCont));
            }
        }
        return strTextoReturn.toString();
    }
    private static void inicio() {
        Scanner scEntrada = new Scanner(System.in);
        String strTextoUsuario;
        String strTextoLeet;

        System.out.print("Introduce un texto a traducir: ");
        strTextoUsuario = scEntrada.nextLine().toLowerCase();
        scEntrada.close();

        strTextoLeet = traduceALeet(strTextoUsuario);

        System.out.println("El texto en lenguaje hacker es: " + strTextoLeet);

    }

    public static void main(String[] args) {
        inicio();
    }
}

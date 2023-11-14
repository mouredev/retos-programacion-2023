import java.io.BufferedReader;
import java.io.InputStreamReader;
/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

public class sntxDev {
    public static String alfabeto = "abcdefghijklmnopqrstuvwxyz";
    public static String numeros = "0123456789";
    public static String simbolos = "!\"#$%&'()*+,-./:;<=>?@[]\\^_`{|}~";

    public static void main(String[] args) {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        char cM, cN, cS;
        int lon;
        try {
            System.out.print("Longitud contraseña(8-16): ");
            lon = Integer.valueOf(entrada.readLine());
            System.out.print("¿Con mayuscula?(y/n): ");
            cM = entrada.readLine().charAt(0);
            System.out.print("¿Con números?(y/n): ");
            cN = entrada.readLine().charAt(0);
            System.out.print("¿Con simbolos?(y/n): ");
            cS = entrada.readLine().charAt(0);

            String showRes = returnPassword(cM, cN, cS, lon, alfabeto, numeros, simbolos);
            System.out.println(showRes);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public static boolean respuesta(char cm, char cn, char cs, int lon) {
        if ((cm == 'y' || cm == 'n') && (cn == 'y' || cn == 'n') && (cs == 'y' || cs == 'n')
                && (lon >= 8 && lon <= 16)) {
            return true;
        }
        return false;
    }

    public static String returnPassword(char cM, char cN, char cS, int lon, String alfabeto,
            String numeros, String simbolos) {
        String res = "";
        if (respuesta(cM, cN, cS, lon)) {
            if (cM == 'y') {
                alfabeto += alfabeto.toUpperCase();
            }
            if (cN == 'y') {
                alfabeto += numeros;
            }
            if (cS == 'y') {
                alfabeto += simbolos;
            }
            char[] chars = alfabeto.toCharArray();
            for (int i = 0; i < lon; i++) {
                int n = (int) (Math.random() * chars.length);
                for (int j = chars.length; j >= n; j--) {
                    if (j == n) {
                        res += chars[j];
                    }
                }
            }
        }
        return res;
    }
}

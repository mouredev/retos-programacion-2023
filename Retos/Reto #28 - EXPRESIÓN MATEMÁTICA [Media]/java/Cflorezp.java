package reto28ExpresionMatematica;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / %
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */
public class Cflorezp {

    private static String x;

    public static void main(String[] args) throws IOException {

        System.out.println(x);
        System.out.println("REGLA: Para numeros negativos escribir el menos junto al numero, ejemplo: -2\n" +
                "Digite la expresión a evaluar: ");
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        String cadena = input.readLine();
        if(verificarCadena(cadena)){
            System.out.println("La expresion: " + cadena + " es una expresion matematica");
        }else{
            System.out.println("La expresion: " + cadena + " NO es una expresion matematica");
        }

        input.close();
    }

    public static boolean verificarCadena(String chainToValidate){
        StringBuilder expresion = new StringBuilder();
        expresion.append("^-?\\d+(\\.\\d+)?\\s[+\\-*/]\\s-?\\d+(\\.\\d+)?$");

        int count = 1;
        for(int i = 0; i < chainToValidate.length(); i ++){
            if(chainToValidate.charAt(i) == '+' || chainToValidate.charAt(i) == '-' || chainToValidate.charAt(i) == '*' || chainToValidate.charAt(i) == '/'){
                count++;
                if(Character.isDigit(chainToValidate.charAt(i + 1))){
                    count--;
                }
            }
        }
        for(int i  = 2; i < count; i++){
            expresion.append("?\\s[+\\-*/]\\s-?\\d+(\\.\\d+)?$");
        }

        String regex = expresion.toString();
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(chainToValidate);
        if (matcher.matches()) {
            return true;
        }
         return false;
    }
}





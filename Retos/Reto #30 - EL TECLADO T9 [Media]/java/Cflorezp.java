package reto30TecladoT9;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */
public class Cflorezp {


    public static void main(String[] args) throws IOException {
        
        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("\n ********* INTERPRETE TECLADO T9 ********* ");
        System.out.print("Digite la cadena: ");
        String secuencia = input.readLine().replaceAll("\\s", "");
        if(validarNumerosYGuiones(secuencia)){
            System.out.println(representacionLetras(secuencia));
        }else{
            System.out.println("No ha ingresado una cadena valida");
        }
        
        input.close();
    }

    public static String representacionLetras(String input){
        Map<Integer, String[]> tecladoT9 = new HashMap<>();
        tecladoT9.put(1, new String[]{",", ".", "?", "!"});
        tecladoT9.put(2, new String[]{"A", "B", "C"});
        tecladoT9.put(3, new String[]{"D", "E", "F"});
        tecladoT9.put(4, new String[]{"G", "H", "I"});
        tecladoT9.put(5, new String[]{"J", "K", "L"});
        tecladoT9.put(6, new String[]{"M", "N", "O"});
        tecladoT9.put(7, new String[]{"P", "Q", "R", "S"});
        tecladoT9.put(8, new String[]{"T", "U", "V"});
        tecladoT9.put(9, new String[]{"W", "X", "Y", "Z"});
        tecladoT9.put(0, new String[]{" "});
        
        String[] elementos = input.split("-");
        StringBuilder resultado = new StringBuilder();
        for(String e: elementos){
            if(validarNumerosIguales(e)){
                String[] letra = tecladoT9.get(teclaPulsada(e));
                resultado.append(letra[e.length() - 1]);
            }else{
                resultado.setLength(0);
                resultado.append("Cadena invalida");
                break;
            }
        }
        return resultado.toString();
    }

    public static boolean validarNumerosYGuiones(String cadena){
        for(int i = 0; i < cadena.length(); i++){
            if(!Character.isDigit(cadena.charAt(i)) && cadena.charAt(i) != '-'){
                return false;
            }
        }
        return true;
    }

    public static boolean validarNumerosIguales(String cadena){
        char valor = cadena.charAt(0);
        for(int i = 1; i < cadena.length(); i++){
            if(cadena.charAt(i) != valor){
                return false;
            }
        }
        return true;
    }

    public static int teclaPulsada(String cadena){
        return Character.getNumericValue(cadena.charAt(0));
    }
}

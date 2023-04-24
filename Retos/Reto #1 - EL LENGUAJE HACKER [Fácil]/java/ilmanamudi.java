package Retos;

import java.util.HashMap;
import java.util.Scanner;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
public class Lenguajehacker {
    public static void main(String[] args) {
        
        Scanner read = new Scanner(System.in).useDelimiter("\n");
        System.out.println("Ingrese un texto a codificar: ");
        String texto = read.next().toLowerCase();
       
        System.out.println("El texto encriptado es: " + encriptar(codigo(), texto));
        
    }
    
    public static HashMap codigo() {
        HashMap<String, String> codigo = new HashMap();

        codigo.put("a", "4");
        codigo.put("b", "I3");
        codigo.put("c", "[");
        codigo.put("d", ")");
        codigo.put("e", "3");
        codigo.put("f", "|=");
        codigo.put("g", "&");
        codigo.put("h", "#");
        codigo.put("i", "1");
        codigo.put("j", ",_|");
        codigo.put("k", ">|");
        codigo.put("l", "1");
        codigo.put("m", "/\\/\\");
        codigo.put("n", "^/");
        codigo.put("o", "0");
        codigo.put("p", "|*");
        codigo.put("q", "(_,)");
        codigo.put("r", "I2");
        codigo.put("s", "5");
        codigo.put("t", "7");
        codigo.put("u", "(_)");
        codigo.put("v", "\\/");
        codigo.put("w", "\\/\\/");
        codigo.put("x", "><");
        codigo.put("y", "j");
        codigo.put("z", "2");
        codigo.put("1", "L");
        codigo.put("2", "R");
        codigo.put("3", "E");
        codigo.put("4", "A");
        codigo.put("5", "S");
        codigo.put("6", "b");
        codigo.put("7", "T");
        codigo.put("8", "B");
        codigo.put("9", "g");
        codigo.put("0", "o");
        return codigo;
    }
    
   
    public static String encriptar(HashMap codigo, String texto){
        String encriptado = "";
        
        for (int i = 0; i < texto.length(); i++) {
            String letra = texto.substring(i, i+1);
            encriptado += codigo.containsKey(letra) ? codigo.get(letra): letra;
        }
        return encriptado;
    }
}


import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */


public class RoyMartinez3103{

    private static final Map<String,String> leetMap = new HashMap<>();

    public static void crearLeet(){
        leetMap.put("A", "4");
        leetMap.put("B", "I3");
        leetMap.put("C", "[");
        leetMap.put("D", ")");
        leetMap.put("E", "3");
        leetMap.put("F", "|=");
        leetMap.put("G", "&");
        leetMap.put("H", "#");
        leetMap.put("I", "1");
        leetMap.put("J", ",_|");
        leetMap.put("K", ">|");
        leetMap.put("L", "1");
        leetMap.put("M", "/\\/\\");
        leetMap.put("N", "^/");
        leetMap.put("O", "0");
        leetMap.put("P", "|*");
        leetMap.put("Q", "(_,)");
        leetMap.put("R", "I2");
        leetMap.put("S", "5");
        leetMap.put("T", "7");
        leetMap.put("U", "(_)");
        leetMap.put("V", "\\/");
        leetMap.put("W", "\\/\\/");
        leetMap.put("X", "><");
        leetMap.put("Y", "j");
        leetMap.put("Z", "2");
        leetMap.put("1", "L");
        leetMap.put("2", "R");
        leetMap.put("3", "E");
        leetMap.put("4", "A");
        leetMap.put("5", "S");
        leetMap.put("6", "b");
        leetMap.put("7", "T");
        leetMap.put("8", "B");
        leetMap.put("9", "g");
        leetMap.put("0", "o");
        leetMap.put(" ", " ");
    }

    public static String traducir(String texto){
        
        crearLeet();
        texto = texto.toUpperCase();
        Integer tamano = texto.length();
        String textoT = "";

        for(int i = 0; i < tamano; i++){
            String caracter = String.valueOf(texto.charAt(i));
            textoT += leetMap.getOrDefault(caracter, caracter);
        }
        return textoT;
    }

    public static String pedirTexto(){
        Scanner scan = new Scanner(System.in);
        String texto = "";
        System.out.println("Ingresa el texto: ");
        texto = scan.nextLine();
        return texto;
    }


    public static void main(String[] args) {
        String texto,textoTraducido;
        texto=pedirTexto();
        textoTraducido= traducir(texto);

        System.out.println("Texto en leet: "+textoTraducido);
    }
}
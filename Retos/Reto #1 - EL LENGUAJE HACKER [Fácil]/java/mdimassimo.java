/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package pkg1.el.lenguaje.hacker;
import java.util.HashMap;
import java.util.stream.Collectors;
import static java.util.Map.entry;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class ElLenguajeHacker {
    /*Método que recibe un char y lo convierte en String*/
    public static String conversorString(char ch){
        return String.valueOf(ch);
        }
        
    public static void main(String[] args) {  
        /*Input de prueba*/
        String input = "MoureDev eres un grande!!";  
        /*Creamos el hashmap y le insertamos todas las letras del abecedario 
        hacker
        */
        HashMap<String, String>alfabetoHacker = new HashMap<>();
        alfabetoHacker.put("A","4");
        alfabetoHacker.put("B","|3");
        alfabetoHacker.put("C","{");
        alfabetoHacker.put("D","|}");
        alfabetoHacker.put("E","£");
        alfabetoHacker.put("F","|=");
        alfabetoHacker.put("G","[");
        alfabetoHacker.put("H","#");
        alfabetoHacker.put("I","|");
        alfabetoHacker.put("J","_|");
        alfabetoHacker.put("K","1<");
        alfabetoHacker.put("L","|_");
        alfabetoHacker.put("M","|V|");
        alfabetoHacker.put("N","/V");
        alfabetoHacker.put("O","()");
        alfabetoHacker.put("P","|O");
        alfabetoHacker.put("Q","9");
        alfabetoHacker.put("R","12");
        alfabetoHacker.put("S","$");
        alfabetoHacker.put("T","+");
        alfabetoHacker.put("U","|_|");
        alfabetoHacker.put("V","\\/");
        alfabetoHacker.put("W","(/\\)");
        alfabetoHacker.put("X","%");
        alfabetoHacker.put("Y"," ¥");
        alfabetoHacker.put("Z","7_");
        alfabetoHacker.put("0", "C");
        alfabetoHacker.put("1", "L");
        alfabetoHacker.put("2", "Z");
        alfabetoHacker.put("3", "E");
        alfabetoHacker.put("4", "h");
        alfabetoHacker.put("5", "S");
        alfabetoHacker.put("6", "b");
        alfabetoHacker.put("7", "T");
        alfabetoHacker.put("8", "B");
        alfabetoHacker.put("9", "g");
        alfabetoHacker.put(" ", " ");
        String output = "";
        /* Recorremos la cadena de prueba*/
        for (int i = 0; i < input.length(); i++){   
            /* Almacenamos en String cada caracter obtenido*/
            String caracterConvertido = conversorString(input.charAt(i));
            /* Si el hashmap contiene una clave que coincida con el String
            obtiene su valor y va formando la cadena resultante. Si el hashmap
            no contiene clave, entonces deja el caracter tal como está
            */
            if(alfabetoHacker.containsKey(caracterConvertido.toUpperCase())){
                String value = alfabetoHacker.get(caracterConvertido.toUpperCase());
                output += value;
            }  else {
                output += caracterConvertido;
            }
        }      
        System.out.println(output);     
    }
}

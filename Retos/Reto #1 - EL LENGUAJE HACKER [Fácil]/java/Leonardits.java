/**
 *
 *  * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 * 
 * @author Leonardo Méndez
 * 
 * Respuesta: Para hacerlo un poco más complejo voy a suponer que debo sacar los caracteres para leet de un txt primero. Luego interactuar con el usuario con ventanas y cuadroas de dialogo.
 * No utilizo la primera line del leet como solicitan. Da muchos números en la traducción. Hice algunos cambios con la segunda linea. Se ve más hacker ;)
 */

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import javax.swing.*;
public class Reto_1_lenguaje_hacker {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);  // instancio un objeto de la clase Scanner para recibir la frase del usuario
        String frase="";
        String fraseleet="";
        char abc[]= new char[]{'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};  // creo un array con las letras del abcedario para poder ir comparando, letra a letra, la frase 
        String abcvacio[]=new String[26];  // creo un array para guardar los caracteres por los cuales cambiar los de la frase del usuario. Está vacio para poder llenarlo con los caracteres leet quye tengo en un archivo txt que bajé de internet
        String texto="";   // creo una variable de tipo String llamada texto en la cual guardaré lo que hay en el archivo con los caracteris leet.
        
        // con este try catch leo el txt y lo introduzco en la variable texto
        try {
            BufferedReader bf=new BufferedReader(new FileReader("C:\\Users\\LEONARDO\\Desktop\\leet.txt"));
            String temp="";
            String bfRead;
            while ((bfRead=bf.readLine())!=null) { 
                temp=temp+bfRead;                
            }
            texto=temp;
        } catch (Exception e) {
            System.out.println("No se encontró el archivo");
        }
        // relleno el array abcvacio, con los caracteres hasta la primera coma, para así tener un arrray traductor de leet
        for(int i=0; i<26; i++){
             abcvacio[i]=texto.substring(((texto.indexOf((abc[i])+"\t"))+((abc[i])+"\t").length()), texto.indexOf(",", texto.indexOf((abc[i])+"\t")));                
            }
        // Utilizo un cuadro de dialogo para explicarle al usuario lo que hace el programa y pedirle la frase con la cual trabajar.
        frase=(JOptionPane.showInputDialog("Esta es una herramienta para transcribir al abcedario leet.\n Introduce la frase a traducir sin utilizar acentos:")).toUpperCase();
        //Recorro la frase caracter por caracter. Busco ese caracter el array con el abcedario para encontrar su indice. Busco el valor de ese indice en el array con los caracteres leet y lo sumo a la variable String fraseleet
        for(int i=0; i<frase.length();i++){
            if((frase.charAt(i))==(' ')){   // si el caracter es un espacio se lo sumo a la fraseleet y sigo con el siguiente
                fraseleet=fraseleet+" ";
            }else{
            fraseleet=fraseleet+abcvacio[Arrays.binarySearch(abc, frase.charAt(i))];
            }
        }
        JOptionPane.showInternalMessageDialog(null, fraseleet);  // Muestro el resultado
        System.exit(0);
    }
}

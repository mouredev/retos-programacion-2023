import java.util.Scanner;

public class jacj14 {
    
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public static void main(String[] args) {
        
    String alfNormal[] = {"A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", 
    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", 
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};


    String alfLeet[] = {"4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", 
    "/\\/\\", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2", " ", 
    "o", "L","R", "E", "A", "S", "b", "T", "B", "g"};

    Scanner teclado = new Scanner(System.in);

    System.out.println("Por favor ingrese el texto que desea convertir: ");

    String texto = teclado.nextLine().toUpperCase();

    char porLetras[] = texto.toCharArray();

    // Se tiene que hacer el recorrido del arreglo porLetras y almacenar la letra en una variable que se pueda 
    //comparar cuando se haga el recorrido del arreglo alfNormal
    
    

    mostrarDatos(porLetras);
    convertir(porLetras, alfNormal, alfLeet);
}


public static void mostrarDatos(char lista[]){
    for (int i = 0; i < lista.length; i++) {
        System.out.print(lista[i]);
    }
}

public static void convertir(char lista[], String lista2[], String lista3[]){
    String conversion = "";
    for (int i = 0; i < lista.length; i++) {
        char letra = lista[i];
        String letraPalabra = String.valueOf(letra);
        for (int j = 0; j < lista2.length; j++) {
            String letraAbecedario = lista2[j];
            if(letraAbecedario.equals(letraPalabra)){
                conversion += lista3[j];
                break;//Tener pendiente si aca esta bien ubicado este break
            }
        }
    }System.out.print("\nEl texto ingresado convertido a lenguaje leet quedaria asi: " + conversion);

}


}


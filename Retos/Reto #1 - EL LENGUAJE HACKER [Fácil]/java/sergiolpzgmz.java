import java.util.Scanner;
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
public class sergiolpzgmz {
    // Funcion que convierte la palabra introducida en lenguaje natural a lenguaje hacker
    public static void palabraNaturalAHacker(String[]arrayHacker, char[] arrayLetrasNaturales, char[] arrayPalabra){
        for (int i = 0; i < arrayPalabra.length ; i++) {
            for (int j = 0; j < arrayLetrasNaturales.length; j++) {
                if(arrayPalabra[i]==arrayLetrasNaturales[j]){
                    System.out.print(arrayHacker[j]);
                }
            }
        }
    }
    public static void main(String[] args) {
        String[]arrayHacker ={"4","I3","[",")","3","|=","&","#","1",",_|",">|","1",
                              "/\\/\\","^/","0","|*","(_,)","I2","5","7","(_)",
                              "\\/","\\/\\/","><","j","2"};
        char[] arrayLetrasNaturales = {'a','b','c','d','e','f','g','h','i','j','k','l',
                                       'm','n','o','p','q','r','s','t','u','v','w','x','y','z'};


        Scanner sc = new Scanner(System.in);
        System.out.print("Introduzca una palabra a convertir en lenguaje hacker: ");
        String palabra = sc.nextLine().toLowerCase();
        char[] arrayPalabra = palabra.toCharArray();

        System.out.print(palabra+" -> ");
        palabraNaturalAHacker(arrayHacker,arrayLetrasNaturales,arrayPalabra);

        sc.close();
    }
}
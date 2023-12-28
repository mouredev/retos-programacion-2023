import java.util.Scanner;

public class Genetrium {
    private static String text;
    private static final String[] abc = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"};
    private static final String[] leek = {"4","I3","[",")","3","|=","&","#","1",",_|",">|","1","/\\/\\","^/","0","|*","(_,)","I2","5","7","(_)","\\/","\\/\\/","><","j","2","L","R","E","A","S","b","T","B","g","o"};
    public static void main(String[] args) {
        graphicInterface();
        System.out.println(leetConverter());
    }

    public static void graphicInterface(){
        Scanner sc = new Scanner(System.in);

        System.out.println("=====================================================================");
        System.out.println("I313^/\\/3^/1)0 41 [0^/\\/3I271)0I2 )3 73><70 4 1337");
        System.out.println("=====================================================================");
        System.out.println("Inserta el texto que quieres convertir a leet:");
        text = sc.nextLine();
        System.out.println("=====================================================================");

    }

    public static String leetConverter() {

        String result = "";
        text.toLowerCase();
        char letter = '0';

        for(int x = 0; x < text.length(); x++){
            letter = text.charAt (x);

            for(int y = 0; y < leek.length; y++){
                if(letter == 32){
                    result += String.valueOf(letter);
                    break;
                }else if(String.valueOf(letter).toLowerCase().equals(abc[y].toLowerCase())){
                    result += leek[y];
                    break;
                }
            }
        }
        return result;
    }
}

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
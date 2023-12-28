import java.util.Hashtable;
import java.util.Scanner;

import static jdk.nashorn.internal.objects.NativeString.toUpperCase;

public class Main {
    public static void main(String[]  args) {
        Hashtable<String,String> alfabeto = new Hashtable<String,String>();
        alfabeto.put("A","4");
        alfabeto.put("B","I3");
        alfabeto.put("C","[");
        alfabeto.put("D",")");
        alfabeto.put("E","3");
        alfabeto.put("F","|=");
        alfabeto.put("G","&");
        alfabeto.put("H","#");
        alfabeto.put("I","1");
        alfabeto.put("J","_|");
        alfabeto.put("K",">|");
        alfabeto.put("L","1");
        alfabeto.put("M","/\\/\\");
        alfabeto.put("N","^/");
        alfabeto.put("O","0");
        alfabeto.put("P","|*");
        alfabeto.put("Q","(_,)");
        alfabeto.put("R","I2");
        alfabeto.put("S","5");
        alfabeto.put("T","7");
        alfabeto.put("U","(_)");
        alfabeto.put("V","\\/");
        alfabeto.put("W","\\/\\/");
        alfabeto.put("X","><");
        alfabeto.put("Y","J");
        alfabeto.put("Z","2");
        alfabeto.put(" "," ");

        Scanner reader = new Scanner(System.in);
        System.out.println("Introduce una frase");
        String frase = reader.nextLine();
        frase = toUpperCase(frase);
        String fraseHacker = "";
        for (int i = 0 ; i < frase.length() ; i++){
            fraseHacker = fraseHacker+alfabeto.get(frase.substring(i,i+1));
        }
        System.out.println(fraseHacker);
    }
}

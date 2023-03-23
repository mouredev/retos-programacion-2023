import java.util.HashMap;
import java.util.Map;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class lenguaje_hacker
{
    public static void main (String[] args)
    {
        String name = "El lenguaje Hacker";
        System.out.println(name);
        contenido(name);
    }

    static void contenido (String palabra)
    {
        palabra = palabra.toLowerCase();
        String [] partes = palabra.split("");
        //System.out.print(Arrays.toString(partes));

        for (int i=0 ; i<partes.length; i++)
        {
            //System.out.print(partes[i].toString());
            diccionario(partes[i].toString());
        }

    }

    static void diccionario(String elemnt){
        
        Map<String, String> dicc = new HashMap<String, String>();

        dicc.put("a", "4"); dicc.put("b","I3"); dicc.put("C", "["); 
        
        dicc.put("a", "4"); dicc.put("b","I3"); dicc.put("c", "["); dicc.put("d",")");
        dicc.put("e", "3"); dicc.put("f","|="); dicc.put("g", "&"); dicc.put("h","#"); 
        dicc.put("i", "1"); dicc.put("j",",_|");  dicc.put("k", ">|"); dicc.put("l","1");
        dicc.put("m", "/\\/\\"); dicc.put("n","^/"); dicc.put("o", "0"); dicc.put("p","|*");
        dicc.put("q", "(_,)"); dicc.put("r","I2"); dicc.put("s", "5"); dicc.put("t","7"); 
        dicc.put("u", "(_)"); dicc.put("v","\\/");  dicc.put("w", "\\/\\/"); dicc.put("x","><");
        dicc.put("y", "j"); dicc.put("z","2"); dicc.put(" ", " ");
        dicc.put("1", "L"); dicc.put("2","R"); dicc.put("3", "E"); dicc.put("4","A");
        dicc.put("5", "S"); dicc.put("6","b"); dicc.put("7", "T"); dicc.put("8","B"); 
        dicc.put("9", "g"); dicc.put("0","o");

        System.out.print(dicc.get(elemnt));
    }

}
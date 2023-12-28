import java.util.HashMap;
import java.util.Map;

class iago1905 {
    private static Map<String, String> miDiccionario = new HashMap<>();

    public static void main(String[] args) {
        miDiccionario.put("A","4");
        miDiccionario.put("B","I3");
        miDiccionario.put("C","[");
        miDiccionario.put("D",")");
        miDiccionario.put("E","3");
        miDiccionario.put("F","|=");
        miDiccionario.put("G","&");
        miDiccionario.put("H","#");
        miDiccionario.put("I","1");
        miDiccionario.put("J",",_|");
        miDiccionario.put("K",">|");
        miDiccionario.put("L","1");
        miDiccionario.put("M","/\\/\\");
        miDiccionario.put("N","^/");
        miDiccionario.put("O","0");
        miDiccionario.put("P","|*");
        miDiccionario.put("Q","(_,)");
        miDiccionario.put("R","I2");
        miDiccionario.put("S","5");
        miDiccionario.put("T","7");
        miDiccionario.put("U","(_)");
        miDiccionario.put("V","\\/");
        miDiccionario.put("W","\\/\\/");
        miDiccionario.put("X","><");
        miDiccionario.put("Y","j");
        miDiccionario.put("Z","2");

        if (args.length == 0) {
            System.out.println("No has introducido ningún argumento");
        } else {
            for (String arg : args) {
                String palabra = arg.toUpperCase();
                for (int i = 0; i < palabra.length(); i++) {
                    String letra = palabra.substring(i, i + 1);
                    if (miDiccionario.containsKey(letra)) {
                        System.out.print(miDiccionario.get(letra));
                    } else {
                        System.out.print(letra);
                    }
                }
                System.out.println();
            }
        }
         
    }
    
}

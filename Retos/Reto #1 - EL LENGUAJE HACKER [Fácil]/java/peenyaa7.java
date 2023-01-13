import java.util.HashMap;
import java.util.Map;

public class peenyaa7 {

    /*
     * Escribe un programa que reciba un texto y transforme lenguaje natural a
     * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
     * se caracteriza por sustituir caracteres alfanuméricos.
     * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
     * con el alfabeto y los números en "leet".
     * (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
     */
    public static void main(String[] args) {
        
        // Init mapper
        Map<Character,String> leetMapper = new HashMap<>();
        leetMapper.put('A', "4");
        leetMapper.put('B', "I3");
        leetMapper.put('C', "[");
        leetMapper.put('D', ")");
        leetMapper.put('E', "3");
        leetMapper.put('F', "|=");
        leetMapper.put('G', "&");
        leetMapper.put('H', "#");
        leetMapper.put('I', "1");
        leetMapper.put('J', ",_|");
        leetMapper.put('K', ">|");
        leetMapper.put('L', "1");
        leetMapper.put('M', "/\\/\\");
        leetMapper.put('N', "^/");
        leetMapper.put('O', "0");
        leetMapper.put('P', "|*");
        leetMapper.put('Q', "(_,)");
        leetMapper.put('R', "I2");
        leetMapper.put('S', "5");
        leetMapper.put('T', "7");
        leetMapper.put('U', "(_)");
        leetMapper.put('V', "\\/");
        leetMapper.put('W', "\\/\\/");
        leetMapper.put('X', "><");
        leetMapper.put('Y', "j");
        leetMapper.put('Z', "2");

        // Input
        String input = "Hola que tal";
        String output = "";

        // Process
        String uppercaseInput = input.toUpperCase();
        for (int i = 0; i < uppercaseInput.length(); i++) {
            char c = uppercaseInput.charAt(i);
            output += leetMapper.containsKey(c) ? leetMapper.get(c) : c;
        }

        // Print output
        System.out.println(output);


    }
}

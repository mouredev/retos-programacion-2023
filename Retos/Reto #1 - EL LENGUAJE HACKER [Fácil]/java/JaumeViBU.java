/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class JaumeViBU {

    public static void main(String[] args) {
        System.out.println(leetTranslate("Hello World"));
    }

    public static String leetTranslate(String str) {
        String[] input = str.toLowerCase().split("");
        HashMap<String, String> leetDictionary = new HashMap<>();
        leetDictionary.put("a", "/\\");
        leetDictionary.put("b", "/3");
        leetDictionary.put("c", "<");
        leetDictionary.put("d", "|)");
        leetDictionary.put("e", "[-");
        leetDictionary.put("f", "|=");
        leetDictionary.put("g", "9");
        leetDictionary.put("h", "!-!");
        leetDictionary.put("i", "!");
        leetDictionary.put("j", ",_]");
        leetDictionary.put("k", "|<");
        leetDictionary.put("l", "7");
        leetDictionary.put("m", "/\\/\\");
        leetDictionary.put("n", "[\\]");
        leetDictionary.put("o", "0");
        leetDictionary.put("p", "|º");
        leetDictionary.put("q", "<|");
        leetDictionary.put("r", "|2");
        leetDictionary.put("s", "$");
        leetDictionary.put("t", "†");
        leetDictionary.put("u", "µ");
        leetDictionary.put("v", "\\/");
        leetDictionary.put("w", "\\/\\/");
        leetDictionary.put("x", "Ж");
        leetDictionary.put("y", "¥");
        leetDictionary.put("z", "7_");
        leetDictionary.put("0", "o");
        leetDictionary.put("1", "|");
        leetDictionary.put("2", "Z");
        leetDictionary.put("3", "E");
        leetDictionary.put("4", "A");
        leetDictionary.put("5", "S");
        leetDictionary.put("6", "G");
        leetDictionary.put("7", "T");
        leetDictionary.put("8", "B");
        leetDictionary.put("9", "g");

        StringBuilder sb = new StringBuilder();
        for (String s : input) {
            String check = leetDictionary.get(s);
            if (check == null) check = " ";
            sb.append(check);
        }

        return sb.toString();
    }
}
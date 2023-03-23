import java.util.AbstractMap;
import java.util.Map;
import java.util.Optional;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class mariabarrilero {

    /*
     * Escribe un programa que reciba un texto y transforme lenguaje natural a
     * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
     *  se caracteriza por sustituir caracteres alfanuméricos.
     * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
     *   con el alfabeto y los números en "leet".
     *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
     */

    private static final Map<String, String> TRANSLATION_TABLE = Stream.of(
                    new AbstractMap.SimpleImmutableEntry<>("1", "L"),
                    new AbstractMap.SimpleImmutableEntry<>("2", "R"),
                    new AbstractMap.SimpleImmutableEntry<>("3", "E"),
                    new AbstractMap.SimpleImmutableEntry<>("4", "A"),
                    new AbstractMap.SimpleImmutableEntry<>("5", "S"),
                    new AbstractMap.SimpleImmutableEntry<>("6", "b"),
                    new AbstractMap.SimpleImmutableEntry<>("7", "T"),
                    new AbstractMap.SimpleImmutableEntry<>("8", "B"),
                    new AbstractMap.SimpleImmutableEntry<>("9", "g"),
                    new AbstractMap.SimpleImmutableEntry<>("0", "o"),
                    new AbstractMap.SimpleImmutableEntry<>("a", "4"),
                    new AbstractMap.SimpleImmutableEntry<>("b", "|3"),
                    new AbstractMap.SimpleImmutableEntry<>("c", "["),
                    new AbstractMap.SimpleImmutableEntry<>("d", ")"),
                    new AbstractMap.SimpleImmutableEntry<>("e", "3"),
                    new AbstractMap.SimpleImmutableEntry<>("f", "|="),
                    new AbstractMap.SimpleImmutableEntry<>("g", "&"),
                    new AbstractMap.SimpleImmutableEntry<>("h", "#"),
                    new AbstractMap.SimpleImmutableEntry<>("i", "1"),
                    new AbstractMap.SimpleImmutableEntry<>("j", ",_|"),
                    new AbstractMap.SimpleImmutableEntry<>("k", ">|"),
                    new AbstractMap.SimpleImmutableEntry<>("l", "1"),
                    new AbstractMap.SimpleImmutableEntry<>("m", "/\\/\\"),
                    new AbstractMap.SimpleImmutableEntry<>("n", "^/"),
                    new AbstractMap.SimpleImmutableEntry<>("o", "0"),
                    new AbstractMap.SimpleImmutableEntry<>("p", "|*"),
                    new AbstractMap.SimpleImmutableEntry<>("q", "(_,)"),
                    new AbstractMap.SimpleImmutableEntry<>("r", "I2"),
                    new AbstractMap.SimpleImmutableEntry<>("s", "5"),
                    new AbstractMap.SimpleImmutableEntry<>("t", "7"),
                    new AbstractMap.SimpleImmutableEntry<>("u", "(_)"),
                    new AbstractMap.SimpleImmutableEntry<>("v", "\\/"),
                    new AbstractMap.SimpleImmutableEntry<>("w", "\\/\\/"),
                    new AbstractMap.SimpleImmutableEntry<>("x", "><"),
                    new AbstractMap.SimpleImmutableEntry<>("y", "j"),
                    new AbstractMap.SimpleImmutableEntry<>("z", "2"))
            .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));

    private static final String GREETING = "\nIntroduce un texto a traducir [Enter para salir]:\t";
    private static final String EMPTY = "";
    private static final String RESULT = "Traducción: \t\t\t\t\t\t\t\t\t\t%s\n";

    public static void main(String[] args) {

        final Scanner input = new Scanner(System.in);
        String text;
        boolean exit;

        try {
            do {
                System.out.print(GREETING);
                text = input.nextLine();
                exit = EMPTY.equals(text);
                if (!exit) {
                    System.out.printf(RESULT, translate(text));
                }
            } while (!exit);
        } finally {
            input.close();
        }
    }

    private static String translate(String text) {

        StringBuilder result = null;

        if (text != null) {
            result = new StringBuilder();
            for (char character : text.toCharArray()) {
                result = result.append(getValueFromCode(character));
            }
        }

        return Optional.ofNullable(result).map(StringBuilder::toString).orElse(null);
    }

    private static String getValueFromCode(final char code) {
        return Optional
                .ofNullable(code)
                .map(String::valueOf)
                .map(String::toLowerCase)
                .map(TRANSLATION_TABLE::get)
                .orElse(String.valueOf(code));
    }
}

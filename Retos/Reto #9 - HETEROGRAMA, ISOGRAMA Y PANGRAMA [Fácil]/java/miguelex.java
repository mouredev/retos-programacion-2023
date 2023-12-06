import java.util.*;

public class miguelex {

    public static String removeDiacritics(String cadena) {

        Map<Character, Character> diacriticos = new HashMap<>();
        diacriticos.put('á', 'a');
        diacriticos.put('é', 'e');
        diacriticos.put('í', 'i');
        diacriticos.put('ó', 'o');
        diacriticos.put('ú', 'u');
        diacriticos.put('à', 'a');
        diacriticos.put('è', 'e');
        diacriticos.put('ì', 'i');
        diacriticos.put('ò', 'o');
        diacriticos.put('ù', 'u');
        diacriticos.put('ä', 'a');
        diacriticos.put('ë', 'e');
        diacriticos.put('ï', 'i');
        diacriticos.put('ö', 'o');
        diacriticos.put('ü', 'u');
        diacriticos.put('â', 'a');
        diacriticos.put('ê', 'e');
        diacriticos.put('î', 'i');
        diacriticos.put('ô', 'o');
        diacriticos.put('û', 'u');
        diacriticos.put('ã', 'a');
        diacriticos.put('ñ', 'n');
        diacriticos.put('õ', 'o');
        diacriticos.put('ç', 'c');

        StringBuilder cadenaSinDiacriticos = new StringBuilder();
        for (char caracter : cadena.toCharArray()) {
            if (diacriticos.containsKey(caracter)) {
                cadenaSinDiacriticos.append(diacriticos.get(caracter));
            } else {
                cadenaSinDiacriticos.append(caracter);
            }
        }
        return cadenaSinDiacriticos.toString();
    }

    public static boolean isHeterogram(String cadena) {
        return cadena.length() == removeDiacritics(cadena).chars().distinct().count();
    }

    public static boolean isIsogram(String cadena) {
        Set<Character> letrasVistas = new HashSet<>();
        for (char letra : removeDiacritics(cadena).toCharArray()) {
            if (letrasVistas.contains(letra)) {
                return false;
            }
            letrasVistas.add(letra);
        }
        return true;
    }

    public static boolean isPangram(String cadena) {
        Set<Character> alfabeto = new HashSet<>();
        for (char letra = 'a'; letra <= 'z'; letra++) {
            alfabeto.add(letra);
        }
        for (char letra : removeDiacritics(cadena.toLowerCase()).toCharArray()) {
            if (alfabeto.contains(letra)) {
                alfabeto.remove(letra);
            }
            if (alfabeto.isEmpty()) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {

        String string1 = "murcielago";
        String string2 = "esdrújula";
        String string3 = "El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja";

        System.out.println(isHeterogram(string1)); // true
        System.out.println(isHeterogram(string2)); // false
        System.out.println(isIsogram(string1)); // true
        System.out.println(isIsogram(string2)); // false
        System.out.println(isPangram(string3)); // true
    }
}
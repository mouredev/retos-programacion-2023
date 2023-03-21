import java.util.*;
public class LaijieJi {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in).useLocale(Locale.US);
        System.out.println("Introduce una cadena de texto");
        String input = sc.nextLine().toLowerCase();

        boolean isHeterogram = true;
        boolean isIsogram;
        Set<Character> characters = new HashSet<>();
        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (!Character.isLetter(c)) {
                continue;
            }
            if (characters.contains(c)) {
                isIsogram = false;
            }
            characters.add(c);
        }

        if (characters.size() == 26) {
            System.out.println("La cadena es un pangrama.");
        }
        if (isIsogram(input)) {
            System.out.println("La cadena es un isograma.");
        }

        for (int i = 0; i < input.length(); i++) {
            char letra = input.charAt(i);
            if (Character.isLetter(letra) && input.indexOf(letra, i + 1) != -1) { // si la letra es una letra del alfabeto y aparece más de una vez
                isHeterogram = false; // la cadena no es un heterograma
                break;
            }
        }
        if (isHeterogram) {
            System.out.println("La cadena es un heterograma.");
        }
        sc.close();
    }

    public static boolean isIsogram(String str) {
        Map<Character, Integer> frequencies = new HashMap<>();
    
        for (char c : str.toCharArray()) {
            int frequency = frequencies.getOrDefault(c, 0);
            frequencies.put(c, frequency + 1);
        }
    
        int initialFrequency = frequencies.get(str.charAt(0));
        for (int frequency : frequencies.values()) {
            if (frequency != initialFrequency) {
                return false;
            }
        }
    
        return true;
        }
}

// [EN] Program in charge of detecting if a text string is a heterogram, an isogram or a pangram.
// [ES] Programa encargado de detectar si una cadena de texto es un heterograma, un isograma o un pangrama.

// [EN] English - Inglés
// Pangram: Minimal phrase that uses all the letters of the alphabet of a certain language.
// Heterogram: Word or phrase that does not contain any repeated letter.
// Isogram: Word or phrase in which each letter occurs the same number of times.

// [ES] Español - Spanish
// Pangrama: Frase mínima que utiliza todas las letras del alfabeto de un determinado idioma.
// Heterograma:  Palabra o frase que no contiene ninguna letra repetida.
// Isograma: Palabra o frase que utiliza el mismo número de letrás el mismo número de veces.

import java.util.Arrays;

public class Main {

    private static final String ALPHABET = "abcdefghijklmnñopqrstuvwxyz";
    public static void main(String[] args) {
        StringBuilder word = new StringBuilder();
        if (args.length == 0) {
            word = new StringBuilder("hola halo");
        } else
            for (String s: args)
                word.append(" ").append(s);

        // This function can be used in every function, but is common for all of them
        String simplifiedWord = simplifyingWord(word.toString());

        if (simplifiedWord.length() > 0) {
            System.out.println(word);
            System.out.println(" - HETEROGRAM? " + (heterogram(simplifiedWord) ? "YES" : "NO"));
            System.out.println(" - ISOGRAM? " + (isogram(simplifiedWord) ? "YES" : "NO"));
            System.out.println(" - PANGRAM? " + (pangram(simplifiedWord) ? "YES" : "NO"));

        } else
            System.out.println("ERROR: There is not a word.");

    }


    // Simplifying a word or phrase in order to avoid problems with accents, spaces or similar.
    public static String simplifyingWord (String word) {
        String aWithAccent = "áàäÀÄ";
        String eWithAccent = "éèëÉÈË";
        String iWithAccent = "íìïÍÌÏ";
        String oWithAccent = "óòöÓÒÖ";
        String uWithAccent = "úùüÚÙÜ";

        word = word.toLowerCase();

        for (char ch: aWithAccent.toCharArray()) word = word.replace(ch, 'a');
        for (char ch: eWithAccent.toCharArray()) word = word.replace(ch, 'e');
        for (char ch: iWithAccent.toCharArray()) word = word.replace(ch, 'i');
        for (char ch: oWithAccent.toCharArray()) word = word.replace(ch, 'o');
        for (char ch: uWithAccent.toCharArray()) word = word.replace(ch, 'u');

        String newWord = word;
        for (char ch: word.toCharArray())
            if (!ALPHABET.contains(String.valueOf(ch)))
                newWord = word.replace(String.valueOf(ch), "");

        return newWord;
    }


    // Pangram: Minimal phrase that uses all the letters of the alphabet of a certain language.
    public static boolean pangram (String word) {
        for (int i= 0; i < ALPHABET.length(); i++)
            if (word.indexOf(ALPHABET.charAt(i)) == -1)
                return false;

        return true;
    }


    // Heterogram: Word or phrase that does not contain any repeated letter.
    // The strategy is to change the string to an array, order the array, and then loop the array.
    // If it is detected a repeated letter, it is not a heterogram (and return "false").
    public static boolean heterogram (String word) {
        char[] arrayWord = word.toCharArray();
        Arrays.sort(arrayWord);

        for (int i = 0; i < arrayWord.length - 1; i++)
            if (arrayWord[i] == arrayWord[i+1])
                return false;

        return true;
    }


    // Isogram: Word or phrase in which each letter occurs the same number of times.
    // The strategy is to change the string to an array, order the array, and then loop the array.
    // In first place, it gets the number of times that the first letter appear.
    // Later, the rest of letters are checked one by one in order to know if it is repeated the same number of times.
    public static boolean isogram (String word) {
        char[] arrayWord = word.toCharArray();
        Arrays.sort(arrayWord);

        int firstLetterCount = 0;
        int currentLetterCount = 1;

        for (int i = 1; i < arrayWord.length; i++) {
            if (arrayWord[i] == arrayWord[i-1]) {
                // No problem, the current letter is the same that the previous one.
                currentLetterCount += 1;

            } else if (firstLetterCount == currentLetterCount) {
                // No problem, it is a new letter and the previous one was OK.
                // The repetitions of the first letter was the same of the last one.
                // Now we start a new counter
                currentLetterCount = 1;

            } else if (firstLetterCount == 0) {
                // Now we are finished the first word. So, here it assign the counter for the first letter.
                // Also, restart the counter.
                firstLetterCount = currentLetterCount;
                currentLetterCount = 1;

            } else
                // Problem, the new letter is not the same and the number of repetitions are different.
                return false;

        }

        return true;
    }


}
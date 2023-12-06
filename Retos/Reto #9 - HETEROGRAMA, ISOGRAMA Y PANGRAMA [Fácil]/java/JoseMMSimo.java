import java.util.Arrays;

public class JoseMMSimo {
    private static final String ALPHABET = "abcdefghijklmnñopqrstuvwxyz";
    public static void main(String[] args) {
        StringBuilder word = new StringBuilder();
        if (args.length == 0)
            word = new StringBuilder("hola halo");
        else
            for (String s : args)
                word.append(" ").append(s);

        String simplifiedWord = simplifyingWord(word.toString());

        if (simplifiedWord.length() > 0) {
            System.out.println(word);
            System.out.println(" - HETEROGRAM? " + (heterogram(simplifiedWord) ? "YES" : "NO"));
            System.out.println(" - ISOGRAM? " + (isogram(simplifiedWord) ? "YES" : "NO"));
            System.out.println(" - PANGRAM? " + (pangram(simplifiedWord) ? "YES" : "NO"));
        } else
            System.out.println("ERROR: There is not a word.");
    }

    public static String simplifyingWord(String word) {
        String aWithAccent = "áàäÀÄ";
        String eWithAccent = "éèëÉÈË";
        String iWithAccent = "íìïÍÌÏ";
        String oWithAccent = "óòöÓÒÖ";
        String uWithAccent = "úùüÚÙÜ";

        word = word.toLowerCase();

        for (char ch : aWithAccent.toCharArray()) word = word.replace(ch, 'a');
        for (char ch : eWithAccent.toCharArray()) word = word.replace(ch, 'e');
        for (char ch : iWithAccent.toCharArray()) word = word.replace(ch, 'i');
        for (char ch : oWithAccent.toCharArray()) word = word.replace(ch, 'o');
        for (char ch : uWithAccent.toCharArray()) word = word.replace(ch, 'u');

        String newWord = word;
        for (char ch : word.toCharArray())
            if (!ALPHABET.contains(String.valueOf(ch)))
                newWord = word.replace(String.valueOf(ch), "");

        return newWord;
    }


    public static boolean pangram(String word) {
        for (int i = 0; i < ALPHABET.length(); i++)
            if (word.indexOf(ALPHABET.charAt(i)) == -1)
                return false;

        return true;
    }


    public static boolean heterogram(String word) {
        char[] arrayWord = word.toCharArray();
        Arrays.sort(arrayWord);

        for (int i = 0; i < arrayWord.length - 1; i++)
            if (arrayWord[i] == arrayWord[i + 1])
                return false;

        return true;
    }


    public static boolean isogram(String word) {
        char[] arrayWord = word.toCharArray();
        Arrays.sort(arrayWord);

        int firstLetterCount = 0, currentLetterCount = 1;
        for (int i = 1; i < arrayWord.length; i++) {
            if (arrayWord[i] == arrayWord[i - 1]) {
                currentLetterCount += 1;
            } else if (firstLetterCount == currentLetterCount) {
                currentLetterCount = 1;
            } else if (firstLetterCount == 0) {
                firstLetterCount = currentLetterCount;
                currentLetterCount = 1;
            } else {
                return false;
            }
        }
        return true;
    }
}

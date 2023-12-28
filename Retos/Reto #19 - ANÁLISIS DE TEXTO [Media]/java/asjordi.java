public class TextParser {

    public void parse(String text){

        text = text.replace("\n", " ");
        String[] textArray = text.split(" ");
        int numOfWords = 0;
        double meanWordsLength = 0;
        int numOfSentences = 0;
        String longestWord  = "";

        for (String word : textArray) {
            if (word.length() != 0) {
                numOfWords++;
                meanWordsLength += word.length();
                if (word.contains(".")) numOfSentences++;
                if (longestWord.length() < word.length()) longestWord = word;
            }
        }

        meanWordsLength /= numOfWords;

        System.out.println("Number of words: " + numOfWords);
        System.out.println("Mean: " + meanWordsLength);
        System.out.println("Number of sentences: " + numOfSentences);
        System.out.println("Longest word: " + longestWord);

    }

}

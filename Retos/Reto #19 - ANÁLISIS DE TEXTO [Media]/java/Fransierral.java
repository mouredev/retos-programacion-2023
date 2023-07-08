/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class Fransierral {

    public static void main(String[] args) {
        if (args.length == 0 || args[0].trim().equals("")) {
            throw new IllegalStateException("No text found");
        }
        TextAnalyzer textAnalyzer = new TextAnalyzer(args[0]);
        textAnalyzer.report();
    }

    static class TextAnalyzer {

        private final String text;
        private int totalWords = 0;
        private int totalCharacters = 0;
        private int totalSentences = 0;
        private String longestWord = "";

        public TextAnalyzer(String text) {
            this.text = fixTextEnd(cleanText(text));
            analyze();
        }

        public double wordAverageLength() {
            return (double) totalCharacters / (double) totalWords;
        }

        public void report() {
            String report = """
                Total words: %d
                Word average length: %.3f
                Total sentences: %d
                Longest word: %s
            """;
            System.out.println(String.format(report, totalWords, wordAverageLength(), totalSentences, longestWord));
        }

        private void analyze() {
            String[] words = cleanText(text).split(" ");
            for (String word : words) {
                processWord(word);
            }
        }

        private void processWord(String word) {
            String cleanWord = cleanWord(word);
            totalWords++;
            totalCharacters += cleanWord.length();
            totalSentences = word.endsWith(".") ? totalSentences + 1 : totalSentences;
            longestWord = cleanWord.length() > longestWord.length() ? cleanWord : longestWord;
        }

        private String cleanText(String text) {
            text = text.replaceAll("\\.", "\\. "); // fixes points not followed by a space
            return text == null ? "" : text.trim().replaceAll("\\s{2,}", " "); // remove duplicate spaces and beginning/end spaces
        }

        private String fixTextEnd(String text) {
            return text.endsWith(".") ? text : text + "."; // adds a point at the end if it does not exist
        }

        private String cleanWord(String word) {
            return word.replaceAll("\\p{Punct}", ""); // remove punctuation symbols
        }

    }

    @Test
    public void oneSentenceText() {
        TextAnalyzer textAnalyzer = new TextAnalyzer("Hola mundo.");
        assertEquals(2, textAnalyzer.totalWords);
        assertEquals(4.5, textAnalyzer.wordAverageLength(), 0.001);
        assertEquals(1, textAnalyzer.totalSentences);
        assertEquals("mundo", textAnalyzer.longestWord);
    }

    @Test
    public void twoSentencesText() {
        TextAnalyzer textAnalyzer = new TextAnalyzer("Vamos a jugar, tus problemas déjalos. Para disfrutar con los Fraggle Rock");
        assertEquals(12, textAnalyzer.totalWords);
        assertEquals(5.0, textAnalyzer.wordAverageLength(), 0.001);
        assertEquals(2, textAnalyzer.totalSentences);
        assertEquals("problemas", textAnalyzer.longestWord);
    }

}

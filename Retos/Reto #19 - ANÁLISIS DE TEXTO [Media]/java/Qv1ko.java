public class Qv1ko {

    public static void main(String[] args) {
        textAnalysis("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin quis turpis vestibulum, elementum mi ac, gravida est. Phasellus ut mattis mauris, a aliquet odio. Integer nec erat sed libero efficitur interdum. Curabitur vitae dolor ac ligula sollicitudin suscipit. Aenean suscipit, sapien id elementum lobortis, turpis orci hendrerit risus, ut fermentum arcu nisl fermentum velit. Fusce id condimentum mi. Aliquam luctus sollicitudin nunc, id suscipit nibh efficitur efficitur. Etiam lacus leo, ullamcorper scelerisque eleifend nec, varius non orci. Morbi est felis, sodales faucibus ligula ut, consequat finibus nisl.");
    }

    private static void textAnalysis(String text) {
        int totalWords = 0, sentences = 0, lettersLongestWord = 0;
        float totalWordLength = 0.0f;
        String longestWord = "";
        for (String word : text.split(" ")) {
            totalWords++;
            if (Character.isLetter(word.charAt(word.length() - 1))) {
                totalWordLength += word.length();
                if (word.length() > lettersLongestWord) {
                    longestWord = word;
                    lettersLongestWord = longestWord.length();
                }
            } else {
                totalWordLength += word.length() - 2;
                if (word.length() > lettersLongestWord) {
                    longestWord = word.substring(0, word.length() - 1);
                    lettersLongestWord = longestWord.length();
                }
                if(word.charAt(word.length() - 1) == '.') {
                    sentences++;
                }
            }
        }
        System.out.println("Total number of words: " + totalWords + "\nAverage word length: " + totalWordLength / totalWords+ "\nNumber of sentences: " + sentences + "\nLongest word: " + longestWord);
    }

}

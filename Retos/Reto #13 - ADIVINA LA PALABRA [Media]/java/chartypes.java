/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo
 * de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 * - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma
 * longitud que
 * la palabra a adivinar)
 * - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si
 * falla, se resta
 * uno al número de intentos
 * - Si escribe una resolución y acierta, finaliza el juego, en caso contrario,
 * se resta uno
 * al número de intentos
 * - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 * ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que
 * consideres
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Random;
import java.util.Scanner;
import java.util.logging.Logger;

public class chartypes {
    private static Random random = new Random();
    private static final Logger logger = Logger.getLogger(chartypes.class.getName());

    public static void main(String[] args) {
        game();

    }

    public static void game() {

        List<String> WORDS = List.of("consideres", "numero", "jugador", "comenzar", "contrario", "letra",
                "palabra", "0", "unicamente", "intentos", "consista", "consideres", "pierde", "a", "ocultando", "60%",
                "el");

        Scanner input = new Scanner(System.in);
        int randomIndex = random.nextInt(WORDS.size());
        String word = WORDS.get(randomIndex);
        ArrayList<String> updatedWord = new ArrayList<>(word.length());

        HashMap<String, Object> resultMap = hideLetters(word);
        int attempts = (int) resultMap.get("hidden");
        ArrayList<Integer> indexes = (ArrayList<Integer>) resultMap.get("indexes");
        String hiddenWord = (String) resultMap.get("word");
        boolean valid = false;
k
        for (Character letter : hiddenWord.toCharArray()) {
            updatedWord.add(letter.toString());
        }
        logger.info("Welcome to the --Guess the Word Game-- ");

        while (attempts > 0 && updatedWord.contains("_")) {

            logger.info("Guess the word: "
                    + updatedWord.toString().replace("[", "").replace("]", "").replace(",", "").replace(" ", "")
                    + "      ----->> Attempts:" + attempts);
            logger.info("Insert a one missing character or the whole word");
            String choice = input.next();

            if (choice.equals(word)) {
                logger.info("Good job!! you hit it !!! ");
                break;
            } else if (choice.length() == 1) {
                valid = false;
                for (Integer index : indexes) {
                    if (choice.toCharArray()[0] == word.charAt(index)
                            && updatedWord.get(index).equalsIgnoreCase("_")) {
                        updatedWord.set(index, choice);
                        valid = true;
                        if (!updatedWord.contains("_"))
                            logger.info("Excelent you did it!!");
                        else {
                            logger.info("Keep going !! You are doing great!!");

                        }

                    }
                }
            }
            if (!valid || choice.length() > 1) {
                attempts--;
                logger.info("Try one more time :( ");

            }
            if (attempts <= 0)
                logger.info("Game Over :( ");
        }
        logger.info("Game ended");
        input.close();
    }

    public static HashMap<String, Object> hideLetters(String word) {

        HashMap<String, Object> result = new HashMap<>();
        int maxLen = word.length();
        ArrayList<Character> wordList = new ArrayList<>();
        ArrayList<Character> hiddenLetters = new ArrayList<>();
        char[] wordArray = word.toCharArray();
        int maxPercent = 60;
        int minPercent = 30;
        int index = 0;
        float randomPercentage = (random.nextInt(maxPercent - minPercent) + minPercent) / 100f;
        int numberOfShadyLetter = Math.round(maxLen * randomPercentage);
        ArrayList<Integer> indexes = new ArrayList<>();

        int shadyCounter = 0;

        for (char letter : wordArray)
            wordList.add(letter);

        while (shadyCounter < numberOfShadyLetter) {
            index = random.nextInt(maxLen);
            if (!wordList.get(index).equals('_')) {
                hiddenLetters.add(wordList.set(index, '_'));
                indexes.add(index);
                shadyCounter++;
            }
        }
        String strWord = wordList.toString()
                .replace("[", "")
                .replace("]", "")
                .replace(",", "")
                .replace(" ", "");

        result.put("word", strWord);
        result.put("hidden", shadyCounter);
        result.put("indexes", indexes);

        return result;

    }
}
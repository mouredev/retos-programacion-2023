import java.util.Scanner;

public class reto13 {

    /*
     * Reto #13
     * 
     * @autor gonzsanz
     * 
     * @description
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

    public static void main(String[] args) {

        guessWord();

    }

    public static void guessWord() {

        int player_tries = 3;
        String[] words = { "murcielago", "pelicula", "pantalla", "teclado", "raton", "programacion",
                "ordenador", "videojuego", "consola" };

        String randomWord = words[(int) (Math.random() * words.length)];

        int maxCharsHidden = (int) Math.floor(randomWord.length() * 0.6);
        String guessWord = randomWord;

        for (int i = 0; i < maxCharsHidden; i++) {
            int randomIndex = (int) (Math.random() * guessWord.length());
            guessWord = guessWord.substring(0, randomIndex) + "_" + guessWord.substring(randomIndex + 1);
        }

        Scanner sc = new Scanner(System.in);
        boolean guessed = false;
        do {
            System.out.println(">> Adivina la palabra: " + guessWord);
            String playerGuess = sc.next();

            if (playerGuess.equals(randomWord))
                guessed = true;

            if (playerGuess.length() == 1) {
                if (randomWord.contains(playerGuess)) {
                    System.out.println("La palabra contiene la letra " + playerGuess);
                    for (int i = 0; i < randomWord.length(); i++) {
                        if (randomWord.charAt(i) == playerGuess.charAt(0)) {
                            guessWord = guessWord.substring(0, i) + playerGuess + guessWord.substring(i + 1);
                        }
                    }
                    System.out.println(guessWord);
                } else {
                    System.out.println("La palabra no contiene la letra " + playerGuess);
                    player_tries--;
                    System.out.println("Te quedan " + player_tries + " intentos");
                }
            }

            if (guessWord.equals(randomWord))
                guessed = true;

        } while (!guessed && player_tries > 0 && !guessWord.equals(randomWord));
        sc.close();

        if (guessed)
            System.out.println("Has ganado!");
        else
            System.out.println("Has perdido, la palabra era: " + randomWord + "!");
    }

}
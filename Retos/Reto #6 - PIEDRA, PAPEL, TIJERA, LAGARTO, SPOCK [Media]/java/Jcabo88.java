import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Jcabo88 {
    enum Token {
        PIEDRA,
        PAPEL,
        TIJERA,
        LAGARTO,
        SPOCK;
        public static Token getToken(String token) {
            return Token.valueOf(token.toUpperCase());
        }
    }

    public static class GameLogic {
        private static final Map<Token, List<Token>> gameToken;

        static {
            gameToken = new EnumMap<>(Token.class);
            gameToken.put(Token.PIEDRA, addToList(Token.TIJERA, Token.LAGARTO));
            gameToken.put(Token.PAPEL, addToList(Token.PIEDRA, Token.SPOCK));
            gameToken.put(Token.TIJERA, addToList(Token.PAPEL, Token.LAGARTO));
            gameToken.put(Token.LAGARTO, addToList(Token.PAPEL, Token.SPOCK));
            gameToken.put(Token.SPOCK, addToList(Token.PIEDRA, Token.SPOCK));
        }
        private boolean isTokenWinner(Token input1, Token input2) {
            return gameToken.get(input1).contains(input2);
        }

        private static List<Token> addToList(Token... token1) {
            return Stream.of(token1).collect(Collectors.toList());
        }

    }

    public static class Player {
        private Integer score;
        private String name;
        private Map<String, Token> tokens;

        Player() {
            this.score = 0;
            this.tokens = new HashMap<>();
        }

        public void setName(String name) {
            this.name = name;
        }

        @Override
        public String toString() {
            return "Name: " + this.name + ", Score:" + score;
        }
    }


    public static class Game {
        int numberOfRounds = 3;
        Player player1 = new Player();
        Player player2 = new Player();
        GameLogic gameLogic = new GameLogic();
        Scanner scanner = new Scanner(System.in);

        public void end(){
            scanner.close();
        }
        public void start() {

            initPlayers();
            int index = 0;
            while (index < numberOfRounds) {

                String currentRound = "round" + index;

                playerInput(currentRound);

                evaluatePlayerInputs(currentRound);

                System.out.println("The result is as following:");
                System.out.println(player1.name + ": " + player1.score);
                System.out.println(player2.name + ": " + player2.score);

                index++;
            }

            if (player1.score > player2.score) {
                System.out.println("The winner is: " + player1.name);
            } else if (player1.score < player2.score) {
                System.out.println("The winner is: " + player2.name);
            } else {
                System.out.println("The result is a tie.");
            }
        }

        /**
         * This function evaluates the input for both players for a given round.
         * @param currentRound
         */
        private void evaluatePlayerInputs(String currentRound) {
            try {
                boolean isTokenPlayer1Winner = gameLogic.isTokenWinner(
                        player1.tokens.get(currentRound),
                        player2.tokens.get(currentRound));

                boolean isTokenPlayer2Winner = gameLogic.isTokenWinner(
                        player2.tokens.get(currentRound),
                        player1.tokens.get(currentRound));

                if (isTokenPlayer1Winner) {
                    player1.score++;
                } else if (isTokenPlayer2Winner){
                    player2.score++;
                }
            } catch (Exception e) {
                System.out.println(e.getMessage());
            }
        }

        private void playerInput(String currentRound) {
            try {
                System.out.println(player1.name + ": Introduce one value");
                String token = scanner.nextLine();
                player1.tokens.put(currentRound, Token.getToken(token));

                System.out.println(player2.name + ": Introduce one value");
                token = scanner.nextLine();
                player2.tokens.put(currentRound, Token.getToken(token));
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }

        private void initPlayers() {
            System.out.println("Input name of the Player1: ");
            String name1 = scanner.nextLine();
            player1.setName(name1.isEmpty() ? "Player1" : name1);

            System.out.println("Input name of the Player2: ");
            String name2 = scanner.nextLine();
            player2.setName(name2.isEmpty() ? "Player2" : name2);
        }
    }

    public static void main(String[] args) {
        Game game = new Game();
        game.start();
        game.end();
    }
}
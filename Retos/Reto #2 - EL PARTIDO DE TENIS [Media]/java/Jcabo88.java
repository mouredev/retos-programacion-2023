import java.util.*;
import java.util.stream.Collectors;

public class Jcabo88 {

    public enum POINTSYSTEM {
        LOVE("0"),
        FIFTEEN("15"),
        THIRTY("30"),
        FORTYFIVE("45"),
        DEUCE("Deuce"),
        ADVANTAGE("Advantage"),
        WIN("Win");

        String value;
        POINTSYSTEM(String value){
            this.value = value;
        }
    }


    public static class Player {
        private String name;
        private POINTSYSTEM point;

        public Player(String name) {
            this.name = name;
            point = POINTSYSTEM.LOVE;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public POINTSYSTEM getPoint() {
            return point;
        }

        public void setPoint(POINTSYSTEM point) {
            this.point = point;
        }
    }

    public static class Tennis {
        private Player player1;
        private Player player2;
        private List<String> args;

        public Tennis(Player player1, Player player2, List<String> str) {
            this.player1 = player1;
            this.player2 = player2;
            this.args = str;
        }
        public void start () {

            for (String arg: args) {

                if (arg.equals(player1.name)) {
                    evaluatePoint(player1);
                }

                if (arg.equals(player2.name)) {
                    evaluatePoint(player2);
                }

                boolean isDeuce = (player1.getPoint() == POINTSYSTEM.FORTYFIVE && player2.getPoint() == POINTSYSTEM.FORTYFIVE)
                || (player1.getPoint() == POINTSYSTEM.ADVANTAGE && player2.getPoint() == POINTSYSTEM.ADVANTAGE);

                if (isDeuce) {
                    player1.setPoint(POINTSYSTEM.DEUCE);
                    player2.setPoint(POINTSYSTEM.DEUCE);
                }

                if (player1.getPoint() == POINTSYSTEM.WIN || player2.getPoint() == POINTSYSTEM.WIN) {
                    break;
                }
            }
            prepareResult();
        }

        private void prepareResult() {
            if (player1.getPoint() == POINTSYSTEM.WIN) {
                System.out.println("The winner is: " + player1.getName());
            } else if (player2.getPoint() == POINTSYSTEM.WIN) {
                System.out.println("The winner is: " + player2.getName());
            } else if (player1.getPoint() == POINTSYSTEM.DEUCE && player2.getPoint() == POINTSYSTEM.DEUCE) {
                System.out.println("The result is: DEUCE");
            } else {
                System.out.println("The result is:");
                System.out.println(player1.getName() + ": "+ player1.getPoint().value);
                System.out.println(player2.getName() + ": "+ player2.getPoint().value);
            }
        }

        private void evaluatePoint(Player player) {
            boolean isWinner = player.getPoint() == POINTSYSTEM.FORTYFIVE || player.getPoint() == POINTSYSTEM.ADVANTAGE;
            if (isWinner) {
                player.setPoint(POINTSYSTEM.WIN);
            } else {
                player.setPoint(POINTSYSTEM.values()[player.getPoint().ordinal() + 1]);
            }
        }
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduce player1 name:");
        String name = scanner.nextLine();

        System.out.println("Introduce player2 name:");
        String name2 = scanner.nextLine();

        System.out.println("Introduce a string with player's names separated by commas:");
        List<String> str = Arrays.stream(scanner.nextLine().split(","))
                .map(String::trim)
                .collect(Collectors.toList());


        scanner.close();

        Tennis tennis = new Tennis(new Player(name), new Player(name2), str);
        tennis.start();
    }
}
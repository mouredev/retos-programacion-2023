import java.util.Random;
import java.util.Scanner;

public class Qv1ko {

    public static void main(String[] args) {

        char[][] house = createHouse();
        int[] door = findDoor(house);

        int[] position = door;
        System.out.println("Starting position: [" + position[0] + ", " + position[1] + "]\n");

        System.out.println("If you want to find the candy in the haunted house you will have to search through its rooms.");
        System.out.println("But remember, you won't be able to move if you don't answer their riddle correctly first.\n");

        Scanner scanner = new Scanner(System.in);

        while (true) {

            position = move(position, house);
            System.out.println("Position: [" + position[0] + ", " + position[1] + "]\n");

            char houseRoom = house[position[0]][position[1]];

            if (houseRoom == 'R') {

                System.out.println("Answer this question correctly.");
                riddle();

                boolean ghost = new Random().nextInt(10) == 1;

                if (ghost) {
                    System.out.println("Boo! To get out of this room you will have to answer one more question.");
                    riddle();
                }

            } else if (houseRoom == 'C') {
                System.out.println("You have found the candy and escaped from the haunted house.");
                break;
            }

        }

        scanner.close();

    }

    private static char[][] createHouse() {

        char[][] house = new char[4][4];

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                house[i][j] = 'R';
            }
        }

        boolean isColumn = new Random().nextBoolean();
        int[] door;

        if (isColumn) {
            door = new int[] { new Random().nextInt(4), new Random().nextInt(2) * 3 };
        } else {
            door = new int[] { new Random().nextInt(2) * 3, new Random().nextInt(4) };
        }

        house[door[0]][door[1]] = 'D';

        int[] candy = generateCandy(door);
        house[candy[0]][candy[1]] = 'C';

        for (int i = 0; i < 4; i++) {
            System.out.println(new String(house[i]));
        }

        return house;

    }

    private static int[] generateCandy(int[] door) {

        int[] candy;

        do {
            candy = new int[] { new Random().nextInt(4), new Random().nextInt(4) };
        } while (candy[0] == door[0] && candy[1] == door[1]);

        return candy;

    }

    private static int[] findDoor(char[][] house) {

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (house[i][j] == 'D') {
                    return new int[] { i, j };
                }
            }
        }

        return new int[] { -1, -1 };

    }

    private static int[] move(int[] position, char[][] house) {

        int row = position[0];
        int column = position[1];

        String movements = "N S E W ";

        if (row == 0) {
            movements = movements.replace("N ", "");
        }
        if (row == 3) {
            movements = movements.replace("S ", "");
        }
        if (column == 0) {
            movements = movements.replace("W ", "");
        }
        if (column == 3) {
            movements = movements.replace("E ", "");
        }

        try (Scanner scanner = new Scanner(System.in)) {

            String movement;

            do {
                System.out.print("Where do you want to move [ " + movements + "]?: ");
                movement = scanner.next().toUpperCase();
            } while (!movements.contains(movement));

            if (movement.equals("N")) {
                position = new int[] { row - 1, column };
            } else if (movement.equals("S")) {
                position = new int[] { row + 1, column };
            } else if (movement.equals("E")) {
                position = new int[] { row, column + 1 };
            } else if (movement.equals("W")) {
                position = new int[] { row, column - 1 };
            }

        }

        return position;

    }

    private static void riddle() {

        int randomNumber1 = (int) (Math.random() * 51);
        int randomNumber2 = (int) (Math.random() * 51);

        String[][] riddles = {
            { Integer.toString(randomNumber1) + " + " + Integer.toString(randomNumber2), Integer.toString(randomNumber1 + randomNumber2) },
            { Integer.toString(randomNumber1) + " - " + Integer.toString(randomNumber2), Integer.toString(randomNumber1 - randomNumber2) },
            { Integer.toString(randomNumber1) + " * " + Integer.toString(randomNumber2), Integer.toString(randomNumber1 * randomNumber2) },
        };

        String[] riddle = riddles[new Random().nextInt(riddles.length)];

        try (Scanner scanner = new Scanner(System.in)) {

            System.out.print(riddle[0] + ": ");

            String answer = scanner.nextLine();

            if (answer.equalsIgnoreCase(riddle[1])) {
                System.out.println("Correct answer!\n");
            } else {
                System.out.println("Incorrect answer!\n");
            }

        }

    }

}

import java.util.Arrays;
import java.util.Objects;
import java.util.Random;
import java.util.Scanner;

public class HauntedHouse {

    public static void main(String[] args) {
        String[][] house;
        int[] door;

        HouseCreationResult result = createHouse();
        house = result.house;
        door = result.door;

        int[] position = Arrays.copyOf(door, door.length);
        System.out.println("Posición inicial: " + Arrays.toString(position));

        System.out.println("""
                👻 BoooOOOoOoo!
                Si quieres encontrar los dulces 🍭 de la casa encantada 🏰
                tendrás que buscarlos a través de sus habitaciones.
                Pero recuerda, no podrás moverte si antes no respondes
                correctamente a su enigma.
                """);

        Scanner scanner = new Scanner(System.in);

        while (true) {
            position = move(position, scanner);
            System.out.println("Posición: " + Arrays.toString(position));

            String houseRoom = house[position[0]][position[1]];

            if (Objects.equals(houseRoom, "⬜")) {
                System.out.println("Responde correctamente a esta pregunta.");
                riddle(scanner);

                boolean ghost = new Random().nextInt(10) == 0;
                if (ghost) {
                    System.out.println("👻 BoooOOOoOoo! Para salir de esta habitación deberás responder otra pregunta más.");
                    riddle(scanner);
                }

            } else if (Objects.equals(houseRoom, "🍭")) {
                System.out.println("""
                        👻 BoooOOOoOoo!
                        Has encontrado los dulces 🍭 y escapado de la casa encantada 🏰
                        Feliz Halloween! 🎃
                        """);
                break;
            }
        }
    }

    static class HouseCreationResult {
        String[][] house;
        int[] door;

        public HouseCreationResult(String[][] house, int[] door) {
            this.house = house;
            this.door = door;
        }
    }

    static HouseCreationResult createHouse() {
        String[][] house = new String[4][4];

        for (String[] row : house) {
            Arrays.fill(row, "⬜");
        }

        int[] door;
        if (new Random().nextBoolean()) {
            door = new int[]{new Random().nextInt(4), new Random().nextInt(2) * 3};
        } else {
            door = new int[]{new Random().nextInt(2) * 3, new Random().nextInt(4)};
        }

        house[door[0]][door[1]] = "🚪";

        int[] candy = generateCandy(door);

        house[candy[0]][candy[1]] = "🍭";

        for (String[] row : house) {
            System.out.println(Arrays.toString(row));
        }

        return new HouseCreationResult(house, door);
    }

    static int[] generateCandy(int[] door) {
        int[] candy = {new Random().nextInt(4), new Random().nextInt(4)};

        if (candy[0] == door[0] && candy[1] == door[1]) {
            return generateCandy(door);
        }

        return candy;
    }

    static int[] move(int[] position, Scanner scanner) {
        int row = position[0];
        int col = position[1];

        String movements = "N S E O ";

        if (row == 0) movements = movements.replace("N ", "");
        if (row == 3) movements = movements.replace("S ", "");
        if (col == 0) movements = movements.replace("O ", "");
        if (col == 3) movements = movements.replace("E ", "");

        System.out.print("¿Hacia dónde te quieres desplazar [ " + movements + "]?: ");
        String movement = scanner.nextLine().toUpperCase();

        if (movements.contains(movement)) {
            switch (movement) {
                case "N":
                    position = new int[]{row - 1, col};
                    break;
                case "S":
                    position = new int[]{row + 1, col};
                    break;
                case "E":
                    position = new int[]{row, col + 1};
                    break;
                case "O":
                    position = new int[]{row, col - 1};
                    break;
            }
            return position;
        } else {
            System.out.println("Desplazamiento incorrecto. Selecciona una de las opciones válidas.");
            return move(position, scanner);
        }
    }

    static void riddle(Scanner scanner) {
        String[][] riddles = {
                {"¿Qué lenguaje de programación fue creado por Guido van Rossum?", "Python"},
                {"¿Cuál es el sistema operativo de código abierto más popular?", "Linux"},
                {"¿Qué compañía desarrolló el sistema operativo Windows?", "Microsoft"},
                {"¿Qué lenguaje de programación se utiliza principalmente para el desarrollo web del lado del cliente?", "JavaScript"},
                {"¿Cuál es el protocolo estándar para enviar correos electrónicos?", "SMTP"},
                {"¿Qué significa HTML?", "HyperText Markup Language"},
                {"¿Cuál es la base de datos relacional de código abierto más popular?", "MySQL"},
                {"¿Qué significa URL?", "Uniform Resource Locator"},
                {"¿Qué compañía desarrolló el lenguaje de programación Java?", "Sun"},
                {"¿Qué estructura de datos es LIFO?", "Pila"},
                {"¿Qué lenguaje de programación fue diseñado por Bjarne Stroustrup?", "C++"},
                {"¿Qué significa HTTP?", "HyperText Transfer Protocol"},
                {"¿Qué significa SQL?", "Structured Query Language"},
                {"¿Cuál es el lenguaje de hojas de estilo utilizado en la web?", "CSS"},
                {"¿Qué significa API?", "Application Programming Interface"},
                {"¿Qué estructura de datos es FIFO?", "Cola"},
                {"¿Cuál es el lenguaje de programación más antiguo aún en uso?", "Fortran"},
                {"¿Qué significa IDE?", "Integrated Development Environment"},
                {"¿Qué compañía es la creadora del sistema operativo macOS?", "Apple"},
                {"¿Qué lenguaje se utiliza comúnmente para el desarrollo de aplicaciones Android?", "Kotlin"}
        };

        String[] currentRiddle = riddles[new Random().nextInt(riddles.length)];

        while (true) {
            System.out.print(currentRiddle[0] + ": ");
            String answer = scanner.nextLine();

            if (answer.equalsIgnoreCase(currentRiddle[1])) {
                System.out.println("Respuesta correcta!\n");
                return;
            } else {
                System.out.println("Respuesta incorrecta!\n");
            }
        }
    }
}

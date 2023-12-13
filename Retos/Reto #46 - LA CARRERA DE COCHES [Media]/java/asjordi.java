import java.util.Arrays;
import java.util.Random;

public class Race {

    public static void main(String[] args) {
        race(20);
    }

    public static void race(int trackLength) {
        String[] track1, track2;
        track1 = new String[trackLength];
        track2 = new String[trackLength];

        createTracks(track1, track2);

        printRace(track1, track2);

        int position1 = track1.length - 1;
        int position2 = track2.length - 1;
        boolean crash1 = false, crash2 = false;

        while (position1 > 0 && position2 > 0) {
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            track1[position1] = "_";
            track2[position2] = "_";

            position1 -= (crash1) ? 0 : new Random().nextInt(3) + 1;
            position2 -= (crash2) ? 0 : new Random().nextInt(3) + 1;

            crash1 = false;
            crash2 = false;

            position1 = (position1 < 0) ? 0 : position1;
            position2 = (position2 < 0) ? 0 : position2;

            if (track1[position1].equals("🌲")) {
                crash1 = true;
            }
            if (track2[position2].equals("🌲")) {
                crash2 = true;
            }

            track1[position1] = (crash1) ? "💥" : "🚙";
            track2[position2] = (crash2) ? "💥" : "🚗";

            printRace(track1, track2);

            checkRace(position1, position2);
        }
    }

    public static void createTracks(String[] track1, String[] track2) {
        Arrays.fill(track1, "_");
        Arrays.fill(track2, "_");

        addTrees(track1);
        addTrees(track2);

        track1[0] = "🏁";
        track1[track1.length - 1] = "🚙";
        track2[0] = "🏁";
        track2[track2.length - 1] = "🚗";
    }

    public static void addTrees(String[] track) {
        Random random = new Random();
        int trees = random.nextInt(3) + 1;

        for (int i = 0; i < trees; i++) {
            int position = random.nextInt(track.length);
            track[position] = "🌲";
        }
    }

    public static void printRace(String[] track1, String[] track2) {
        System.out.print("\033[H\033[2J"); // Clear console (Unix-based systems)
        // System.out.print("\f"); // Clear console (Windows)

        System.out.println(String.join("", track1));
        System.out.println(String.join("", track2));
        System.out.println();
    }

    public static void checkRace(int position1, int position2) {
        if (position1 == 0 && position2 == 0) {
            System.out.println("Empate");
        } else if (position1 == 0) {
            System.out.println("Ha ganado el coche 🚙");
        } else if (position2 == 0) {
            System.out.println("Ha ganado el coche 🚗");
        }
    }
}


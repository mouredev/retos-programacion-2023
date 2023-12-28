public class Qv1ko {

    private static char END = '#';
    private static char ROAD = '_';
    private static char TREE = 'T';
    private static char CAR = '<';
    private static char SHOCK = 'x';
    
    public static void main(String[] args) {
        race();
    }

    private static void race() {

        int turn = 1;
        boolean shockCar1 = false, shockCar2 = false;

        String track1 = trackGenerator();
        String track2 = trackGenerator();

        System.out.println("\nSTART\n");

        System.out.println(track1);
        System.out.println(track2);

        while (track1.toCharArray()[0] != CAR && track2.toCharArray()[0] != CAR) {

            try {
                Thread.sleep(1000);
            } catch (InterruptedException exc) {
                exc.printStackTrace();
            }

            System.out.println("\nTurn " + turn + "\n");

            if (!shockCar1) {

                track1 = advance(track1, (int)(Math.random() * 3) + 1);

                for (char element : track1.toCharArray()) {
                    if (element == SHOCK) {
                        shockCar1 = true;
                        break;
                    }
                }

            } else {
                shockCar1 = false;
            }

            if (!shockCar2) {

                track2 = advance(track2, (int)(Math.random() * 3) + 1);

                for (char element : track2.toCharArray()) {
                    if (element == SHOCK) {
                        shockCar2 = true;
                        break;
                    }
                }

            } else {
                shockCar2 = false;
            }

            System.out.println(track1);
            System.out.println(track2);

            turn++;

        }

        if (track1.toCharArray()[0] == track2.toCharArray()[0]) {
            System.out.println("\nThe race ended in a tie");
        } else {
            System.out.println("\nThe race winner is " + ((track1.toCharArray()[0] == CAR) ? "car 1" : "car 2"));
        }

    }

    private static String trackGenerator() {

        String road = "";
        int trees = 0;

        for (int i = 0; i < 10; i++) {
            if (trees < 3 && (int)(Math.random() * 10) < 3) {
                road += TREE;
                trees++;
            } else {
                road += ROAD;
            }
        }

        return END + road + CAR;

    }

    private static String advance(String track, int positions) {

        String clearTrack = "", newTrack = "";
        int newPosition = 0;

        for (int i = 0; i < track.length(); i++) {
            if (track.toCharArray()[i] == CAR || track.toCharArray()[i] == SHOCK) {
                newPosition = (i - positions < 0) ? 0 : i - positions;
                clearTrack += '_';
            } else {
                clearTrack += track.toCharArray()[i];
            }
        }

        for (int i = 0; i < clearTrack.length(); i++) {
            if (i == newPosition) {
                newTrack += (clearTrack.toCharArray()[newPosition] == TREE) ? SHOCK : CAR;
            } else {
                newTrack += clearTrack.toCharArray()[i];
            }
        }

        return newTrack;

    }

}

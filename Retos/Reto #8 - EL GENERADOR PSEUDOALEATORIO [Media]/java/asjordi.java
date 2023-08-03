import java.time.LocalTime;

public class PseudoRandomGenerator {

    private final LocalTime lt = LocalTime.now();
    private int seed = (int) System.currentTimeMillis();

    private int generateRandomNumber() {

        seed = (seed * 1103515245 + 12345) & Integer.MAX_VALUE;

        return seed % 101;

    }

    public int generateWithNano() {

        return (lt.getNano() + 1) / 10000000;

    }

}

import java.util.concurrent.TimeUnit;

public class Fhera {

    public static void main(String[] args) {
        countDown(5, 2);
    }

    private static void countDown(Integer startNumber, Integer intervalSeconds) {
        if (startNumber < 0 || intervalSeconds < 0) {
            System.out.println("No se aceptan números negativos.");
        } else {
            while (startNumber != 0) {
                System.out.println(startNumber);
                try {
                    Thread.sleep(TimeUnit.SECONDS.toMillis(intervalSeconds));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                startNumber--;
            }
            System.out.println(startNumber);
        }
    }
}
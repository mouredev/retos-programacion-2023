import java.util.concurrent.TimeUnit;

public class Qv1ko {

    public static void main(String[] args) {
        countdown(9, 3);
    }

    private static void countdown(int startNumber, int waitingTime) {
        if (startNumber >= 0) {
            for (int i = startNumber; i >= 0; i--) {
                System.out.println(i);
                try {
                    TimeUnit.SECONDS.sleep((i != 0) ? waitingTime : 0);
                } catch (InterruptedException exc) {
                    System.out.println("Waiting time has failed");
                }
            }
        }
    }

}

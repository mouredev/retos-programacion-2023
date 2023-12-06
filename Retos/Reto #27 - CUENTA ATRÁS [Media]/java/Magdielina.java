public class Magdielina {
    public static void main(String[] args) {
        try {
            countdown(10,5);
        } catch (InterruptedException e) {
            System.out.println("Sorry!, there was an error during countdown.");
        }
    }

    private static void countdown(int start, int interval) throws InterruptedException{
        if (start > 0 && interval > 0) {
            for (; start >= 0; start--) {
                System.out.println("Count..." + start);
                Thread.sleep(interval * 1000);
            }
        } else {
            System.out.println("Please, provide only positive numbers.");
        }
    }
}
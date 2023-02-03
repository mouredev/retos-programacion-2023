
public class Allin {

    /**
     * @param args
     */
    public static void main(String[] args) {
        //FIZZBUZZ
        boolean multiple3 = false;
        boolean multiple5 = false;
        for (int i = 1; i <= 100; i++) {
            multiple3 = false;
            multiple5 = false;
            if (i%3 == 0) {
                multiple3 = true;
            }
            if (i%5 == 0) {
                multiple5 = true;
            }
            if (multiple3 && multiple5) {
                System.out.println("fizzbuzz");
            } else if (multiple3) {
                    System.out.println("fizz");
            } else if (multiple5) {
                System.out.println("fizz");
            } else {
                System.out.println(i);
            }
            System.out.println("");
        }
    }
}


/**
 * The type Sebastian 09173.
 */
public class Sebastian09173 {

    /**
     * Game fizz buzz.
     *
     * @param range the range
     */
    public void gameFizzBuzz(int range) {
        for (int i = 1; i <= range; i++) {
            if (i % 3 == 0 && i % 5 == 0) { // Si es multiplo de 3 y de 5
                System.out.println("fizzbuzz");
            } else if (i % 3 == 0) { // Si es multiplo de 3
                System.out.println("fizz");
            } else if (i % 5 == 0) { // Si es multiplo de 5
                System.out.println("buzz");
            }
            System.out.println(i);
        }
    }

    /**
     * The entry point of application.
     *
     * @param args the input arguments
     */
    public static void main(String[] args) {
        Sebastian09173 sebastian09173 = new Sebastian09173();
        sebastian09173.gameFizzBuzz(100);
    }
}

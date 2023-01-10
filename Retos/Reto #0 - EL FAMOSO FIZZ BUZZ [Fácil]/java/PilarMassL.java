public class PilarMassL {

    public static void main(String args[]) {

        for (int i = 0; i < 99; i++) {
            extractDivisor(i, "fizz", 5, "buzz", 3, "fizzbuzz");

        }

    }

    public static void extractDivisor(int i, String fizz, int i2, String buzz, int i3, String fizzbuzz) {
        if (i%3 == 0 && i%5 == 0) {
            System.out.println(fizz);
        } else if (i% i2 == 0) {
            System.out.println(buzz);
        } else if (i% i3 == 0) {
            System.out.println(fizzbuzz);
        } else {
            System.out.println(i);
        }
    }

}

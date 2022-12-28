public class FizzBuzz {
    public static void main(String[] args) {
        String fizz = "fizz";
        String buzz = "buzz";
        for (int i = 1; i <= 100; i++) {
            if (i % 3 == 0 && i % 5 == 0) System.out.println(fizz + buzz);
            else if (i % 3 == 0) System.out.println(fizz);
            else if (i % 5 == 0) System.out.println(buzz);
            else System.out.println(i);
        }
    }
}

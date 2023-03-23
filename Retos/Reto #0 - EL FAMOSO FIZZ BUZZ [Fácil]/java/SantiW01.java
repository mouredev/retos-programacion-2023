public class santiw01 {
    public static void main(String[] args) {
        int i;
        for(i = 0; i <= 100; i++) {
            if(i % 3 == 0 && i % 5 == 0) {
                System.out.println("fizzBuzz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else {
                continue;
            }
        }
    }
}
class Main {
    public static void main(String[] args) {
        fizzBuzz();
    }

    public static void fizzBuzz() {
        for (int x = 1; x <= 100; x ++) {
            if (x % 15 == 0) {
                System.out.printf("fizzbuzz\n");
            } else if (x % 3 == 0) {
                System.out.printf("fizz\n");
            } else if (x % 5 == 0) {
                System.out.printf("buzz\n");
            } else {
                System.out.printf("%d\n", x);
            }
        }
    }
}
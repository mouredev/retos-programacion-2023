public class miguelex {
    public static void main(String[] args) {
        System.out.println(CheckNumber(1));
        System.out.println(CheckNumber(2));
        System.out.println(CheckNumber(3));
        System.out.println(CheckNumber(4));
        System.out.println(CheckNumber(5));
        System.out.println(CheckNumber(6));
        System.out.println(CheckNumber(7));
        System.out.println(CheckNumber(8));
        System.out.println(CheckNumber(9));
        System.out.println(CheckNumber(10));
        System.out.println(CheckNumber(1024));
        System.out.println(CheckNumber(1358742586));
    }

    private static String CheckNumber(int number) {
        String isPrime = isPrimeNumber(number) ? "es primo, " : "no es primo, ";
        String isEven = isEvenNumber(number) ? "es par y " : "no es par y ";
        String isFibonacci = isFibonacciNumber(number) ? "es un numero de Fibonacci" : "no es numero de Fibonacci";

        return "El numero " + Integer.toString(number) + " " + isPrime + isEven + isFibonacci;
    }

    private static boolean isPrimeNumber(int number) {
        if (number == 1) {
            return false;
        }
        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }

    private static boolean isEvenNumber(int number) {
        return number % 2 == 0;
    }

    private static boolean isFibonacciNumber(int number) {
        int a = 0;
        int b = 1;
        int c = 0;
        while (c < number) {
            c = a + b;
            a = b;
            b = c;
        }
        return c == number;
    }

}
public class PrimeFibonacciEven {

    public static void main(String[] args) {

        PrimeFibonacciEven p = new PrimeFibonacciEven();

        System.out.println(p.checkNumber(2));
        System.out.println(p.checkNumber(7));
        System.out.println(p.checkNumber(0));

    }

    public String checkNumber(int n) {

        StringBuilder msg = new StringBuilder();

        msg.append(n);

        if (isPrime(n)) msg.append(" es primo,");
        else msg.append(" no es primo,");

        if (isFibonacci(n)) msg.append(" es fibonacci");
        else msg.append(" no es fibonacci");

        if (isEven(n)) msg.append(" y es par");
        else msg.append(" y es impar");

        return msg.toString();
    }

    public boolean isEven(int n) {

        return n % 2 == 0;

    }

    public boolean isPrime(int n) {

        if (n <= 1) return false;

        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }

        return true;

    }

    public boolean isFibonacci(int n) {

        if (n == 0) return false;

        return isPerfectSquare(5 * n * n + 4) || isPerfectSquare(5 * n * n - 4);

    }

    public boolean isPerfectSquare(int n) {

        int sqrt = (int) Math.sqrt(n);

        return sqrt * sqrt == n;

    }

    public boolean isFibonacciNumber(int n) {

        if (n == 0) return false;

        int prev = 0;
        int current = 1;

        while (current <= n) {
            int temp = current;
            current = prev + current;
            prev = temp;

            if (current == n) {
                return true;
            }
        }

        return false;

    }

}

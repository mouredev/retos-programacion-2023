import java.util.ArrayList;

public class Qv1ko {

    public static void main(String[] args) {
        twinPrimes(21);
    }

    private static void twinPrimes(int maxNumber) {
        if(maxNumber>=0) {
            String result = "";
            ArrayList<Integer> primes = new ArrayList<Integer>();
            boolean isPrime = true;
            for (int i = 2; i <= maxNumber; i++) {
                isPrime = true;
                for (int j = 2; j < i; j++) {
                    if (i % j == 0 && i != j) {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime) {
                    primes.add(i);
                }
            }
            for (int k = 0; k < primes.size() - 1; k++) {
                if (primes.get(k) + 2 == primes.get(k + 1)) {
                    result += (result.equals("")) ? "(" + primes.get(k) + ", " + primes.get(k + 1) + ")" : ", (" + primes.get(k) + ", " + primes.get(k + 1) + ")";
                }
            }
            System.out.println("Range " + maxNumber + "\n" + result);
        } else {
            System.out.println("Maximum range must be a positive integer");
        }
    }

}

import java.util.stream.IntStream;

public class TwinPrimeNumbers {

    public static String calculate(int range){

        StringBuilder res = new StringBuilder();
        int[] rangeOfNumbers = IntStream.rangeClosed(0, range).toArray();


        for (int num : rangeOfNumbers){
            int currentPlusTwo = num + 2;
            if (isPrime(num) && isPrime(currentPlusTwo)) res.append("(").append(num).append(", ").append(currentPlusTwo).append(")\n");
        }

        return res.toString();

    }

    public static boolean isPrime(int num) {

        if (num <= 1) return false;

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }

        return true;

    }



}

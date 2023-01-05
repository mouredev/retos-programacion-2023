public class Kirenai {

    public static void main(String[] args) {
        for (int i = 1; i <= 100; i++) {
            boolean isMultipleOfThreeAndFive = i % 3 == 0 && i % 5 == 0;
            if (isMultipleOfThreeAndFive) {
                System.out.println("fizzbuzz");
                continue;
            }
            boolean isMultipleOfThree = i % 3 == 0;
            if (isMultipleOfThree) {
                System.out.println("fizz");
                continue;
            }
            boolean isMultipleOfFive = i % 5 == 0;
            if (isMultipleOfFive) {
                System.out.println("buzz");
                continue;
            }
            System.out.println(i);
        }
    }

}

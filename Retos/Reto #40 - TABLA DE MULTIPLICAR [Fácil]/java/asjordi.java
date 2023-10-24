public class MultiplicationTable {

    public void calculate(int n){

        for (int i = 1; i <= 10; i++) {
            System.out.printf("%d x %d = %d%n", n, i, n * i);
        }
    }

}

public class Qv1ko {

    public static void main(String[] args) {
        findPythagoreanTriple(10);
    }

    public static void findPythagoreanTriple(int max) {

        for (int a = 1; a <= max; a++) {
            for (int b = a; b <= max; b++) {
                for (int c = b; c <= max; c++) {
                    if (a * a + b * b == c * c) {
                        System.out.println("(" + a + ", " + b + ", " + c + ")");
                    }
                }
            }
        }

    }

}

public class fizz_buzz {
    public static void main(String[] args) {

        for (int i = 1; i <= 100; i++) {

                int resultado = i;

                if (resultado % 3 == 0 && resultado % 5 ==0) {
                    System.out.println("fizzbuzz");
                }else {
                if(resultado % 3 == 0) {
                    System.out.println("fizz");
                } else
                if (resultado % 5 == 0) {
                    System.out.println("buzz");
                }else {
                    System.out.println(resultado);
                }
            }
        }
    }
}

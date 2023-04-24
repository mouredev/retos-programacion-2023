public class camilaspt {

    public static void main(String[] args) {
        fizzBuzz();
    }

    public static void fizzBuzz(){
        for (int i = 1; i <= 100; i ++ ){
            if(multiplo3(i) && !multiplo5(i)){
                System.out.println("fizz");
            }
            if(multiplo5(i) && !multiplo3(i)){
                System.out.println("buzz");
            }
            if (multiplo3y5(i)) {
                System.out.println("fizzbuzz");
            }
        }
    }

    private static boolean multiplo3(int i) {
        return i%3 == 0;
    }

    private static boolean multiplo5(int i){
        return i%5 == 0;
    }

    private static boolean multiplo3y5(int i){
        return multiplo3(i) && multiplo5(i);
    }

}

public class Qv1ko {

    public static void main(String[] args) {
        for(int i=1;i<=100;i++) {
            fizzbuzz(i);
        }
    }//main

    private static void fizzbuzz(int number) {
        if(number%3==0&&number%5==0) {
            System.out.println("fizzbuzz");
        } else if(number%3==0) {
            System.out.println("fizz");
        } else if(number%5==0) {
            System.out.println("buzz");
        } else {
            System.out.println(number);
        }
    }//fizzbuzz

}//class

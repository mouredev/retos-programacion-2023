public class Qv1ko {

    public static void main(String[] args) {
        checker(21);
    }//main

    private static void checker(int number) {
        String primeResult=" ",fibonacciResult=" ",evenResult=" ";
        int fib1=0,fib2=1;
        for(int i=number;i>0;i--) {
            if(number%i==0&&number!=i&&number!=1) {
                primeResult=number+" is prime,";
                break;
            } else {
                primeResult=number+" is not prime,";
            }
        }
        while((fib1+fib2)<=number) {
            if(number==(fib1+fib2)) {
                fibonacciResult=" fibonacci and";
                break;
            } else {
                fibonacciResult=" is not fibonacci and";
                if(fib1<fib2) {
                    fib1+=fib2;
                } else {
                    fib2+=fib1;
                }
            }
        }
        if(number%2==0) {
            evenResult=" is even";
        } else {
            evenResult=" is odd";
        }
        System.out.println(primeResult+fibonacciResult+evenResult);
    }//checker

}//class
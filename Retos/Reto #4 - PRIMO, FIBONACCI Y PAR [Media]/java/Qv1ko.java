public class Qv1ko {

    public static void main(String[] args) {
        checker(21);
    }//main

    private static void checker(int number) {
        String result=number+" ";
        boolean prime=true;
        if(number>1) {
            for(int i=2;i<number;i++) {
                if(number%i==0) {
                    prime=false;
                    break;
                }
            }
            result+=(prime)? "is prime, ":"is not prime, ";
        } else {
            result+="is not prime, ";
        }
        result+=(number>0&&(fibonacciEquation(5*number*number+4)||fibonacciEquation(5*number*number-4)))? "fibonacci and ":"is not fibonacci and ";
        result+=(number%2==0)? "is even":"is odd";
        System.out.println(result);
    }//checker

    private static boolean fibonacciEquation(int number) {
        int sqrt=(int)Math.sqrt(number);
        return sqrt*sqrt==number;
    }//fibonnaciEquation

}//class
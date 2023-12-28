public class AnzurezDev {
    public static void main( String args[] ) {
        fizzBuzz();
    }

    public static void fizzBuzz() {
        for ( int index=1; index<=100; index++ ) {
            String output = ( index % 3==0 ? "fizz" : "" ) + ( index % 5==0 ? "buzz" : "" );
            System.out.println( output.isEmpty() ? index : output );
        }
    }
}
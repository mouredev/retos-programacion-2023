import java.util.ArrayList;

public class AnzurezDev {
    public static void main( String args[] ) {
        getTwinPrimeNumbers( 14 );
    }

    public static boolean isPrime( int number ) {
        if ( number<2 )
            return false;

        for ( int i=2; i<number; i++ ) {
            if ( number%i == 0 )
                return false;
        }

        return true;
    }

    public static void getTwinPrimeNumbers( int limit ) {
        int currentPrime = 0;
        int lastPrime = 2;
        ArrayList<String> twinPrimeNumbers = new ArrayList<String>();

        for ( int index=2; index<=limit; index++ ) {
            if ( isPrime(index) ) {
                currentPrime = index;

                if ( (currentPrime-lastPrime)==2 ) {
                    twinPrimeNumbers.add( "(" + lastPrime + ","+ currentPrime + ")" );
                }

                lastPrime = currentPrime;
            }
        }

        printArrayList(twinPrimeNumbers);
    }

    public static void printArrayList( ArrayList<String> elementos) {
        for ( int index=0; index<elementos.size(); index++ ) {
            System.out.println( elementos.get(index) );
        }
    }
}
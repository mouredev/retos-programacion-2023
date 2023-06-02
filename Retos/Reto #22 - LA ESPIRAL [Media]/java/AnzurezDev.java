import java.util.Scanner;

public class AnzurezDev {
    public static void main( String args[] ) {
        int option      = 1;
        Scanner reader  = new Scanner( System.in );

        while ( option>0 ) {
            System.out.println( "Enter a number greater than one to set the spiral size or (0) to exit:" );
            option = reader.nextInt();

            if ( option>1 )
                printSpiral( option );
        }
    }

    public static void printSpiral( int size ) {
        char spiral[][] = new char[size][size];
        int iterations  = size/2 + 1;
        int indexLeft   = 0;
        int indexRight  = 0;
        int from        = 0;
        int to          = size;
        char horizontal = '\u2550'; // ═
        char vertical   = '\u2551'; // ║
        char topLeft    = '\u2554'; // ╔
        char topRight   = '\u2557'; // ╗
        char downLeft   = '\u255A'; // ╚
        char downRight  = '\u255D'; // ╝
        char value      = '\u0020'; // Blank Space

        if ( size%2 == 0 )
            iterations = size/2;

        // Traverse array by rows
        for ( int iteration=0; iteration<iterations; iteration++ ) {
            // Fill data to right (→)
            for ( int indexR=from; indexR<to; indexR++ )  {
                value       = horizontal;
                indexLeft   = from;
                indexRight  = indexR;

                if ( indexR==(to-1))
                    value = topRight;

                spiral[indexLeft][indexRight] = value;
            }

            // Fill data to down (↓)
            for ( int indexD=(from+1); indexD<to; indexD++ )  {
                value       = vertical;
                indexLeft   = indexD;
                indexRight  = to-1;

                if ( indexD==(to-1) )
                    value = downRight;

                spiral[indexLeft][indexRight] = value;
            }

            // Fill data to left (←)
            for ( int indexL=to-2; indexL>=from; indexL-- )  {
                value       = horizontal;
                indexLeft   = to-1;
                indexRight  = indexL;

                if ( indexL==from )
                    value = downLeft;

                spiral[indexLeft][indexRight] = value;
            }

            // Fill data to up (↑)
            for ( int indexU=to-2; indexU>from; indexU-- )  {
                value       = vertical;
                indexLeft   = indexU;
                indexRight  = from;

                if ( indexU==(from+1) )
                    value = topLeft;

                spiral[indexLeft][indexRight] = value;
            }

            from++;
            to--;
        }

        // Print full array
        for ( int i=0; i<size; i++ ) {
            for ( int j=0; j<size; j++ )  {
                    System.out.print( spiral[i][j] );
                }
            System.out.print( "\n" );
        }
    }
}
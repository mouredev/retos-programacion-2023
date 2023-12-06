/*
 Retos Semanales ‘23
 Reto #21: NÚMEROS PRIMOS GEMELOS
 MEDIA | Publicación: 22/05/23 | Resolución: 29/05/23

 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 *
*/

// Autor: Clark - @ClarkCodes
// Fecha de Resolución: 29/05/2023
// Lenguaje: Java

package retos_2023_mauredev_java_project;

// Imports
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import javax.swing.JOptionPane;

public class PrimosGemelos
{
    public record PrimeTwinsPair( int leftPrime, int rightPrime ){}    

    private boolean isPrime( int n )
    {
        for ( int i = 2; i < n; i++ )
            if( ( n % i ) == 0 )
                return false;
        
        return true;
    }

    private void primeTwinsEngine( int maxRange )
    {
        ArrayList<PrimeTwinsPair> primeTwins = new ArrayList<>();
        int leftPrime = 0, rightPrime = 0;

        for ( int n = 1; n <= maxRange; n++ ) // Prime Twins Engine
        {
            if( isPrime( n ) )
            {
                if( leftPrime == 0 ) // En la primera iteración simplemente se asigna el primer valor primo a left_prime, se necesitan dos primos para realizar la resta y verificar si son gemelos
                {    
                    leftPrime = n;
                }
                else // En las siguientes iteraciones en que se hallen números primos se asignará su valor a right_prime y se realizará la resta, si la diferencia es exactamente 2, se agregará left_prime y right_prime como una tupla par de valores a la lista prime_twins, ahí se iran recolectando los primos gemelos que se encuentren
                {
                    rightPrime = n;

                    if( ( rightPrime - leftPrime ) == 2 )
                        primeTwins.add( new PrimeTwinsPair( leftPrime, rightPrime ) );

                    leftPrime = rightPrime; // Al final de la iteración nos aseguramos que left_prime tenga ahora el valor de right_prime para que la próxima vez que se halle un primo y se asigne su valor a right_prime se pueda realizar la resta correctamente ahora entre el último primo que se tenia con el siguiente
                }
            }
        }

        if( primeTwins.size() > 0 )
        {
            System.out.println( "\nLos Números Primos Gemelos en el rango entre 1 y " + maxRange + " son los siguientes:\n" );
            AtomicInteger listIndex = new AtomicInteger( 1 );

            primeTwins.forEach( pair -> 
            {
                int index = listIndex.getAndIncrement();
                System.out.print( pair.leftPrime() + " y " + pair.rightPrime() );
            
                if( index < primeTwins.size() )
                    System.out.print( ", " );
            } );
        }
        else
        {
            System.out.println( "\nNo existen Números Primeros Gemelos entre 1 y " + maxRange );
        }

        System.out.println( " " );
    }

    public static void main( String[] args )
    {
        PrimosGemelos primeTwins = new PrimosGemelos();
        boolean welcomePending = true;
        boolean keepRunning = true;

        do
        {
            if( welcomePending )
            {
                System.out.println( "\n*** Reto #21: NÚMEROS PRIMOS GEMELOS - By @ClarkCodes ***" );
                welcomePending = false;
            }
            else
                System.out.println( "\n¿Qué tal, está cool no?, ¿quieres ingresar otro rango?" );

            try
            {  
                String userAnswer = JOptionPane.showInputDialog( null, 
                    "Ingrese el rango máximo para calcular los Números Primos Gemelos, debe ser un número entero positivo, o ingresa 'q' si deseas salir.\nRango máximo: ",
                    "Rango", 
                    JOptionPane.QUESTION_MESSAGE );

                if( userAnswer.trim().equalsIgnoreCase( "q" ) ) // Condición de Salida
                {
                    System.out.println( "\nEsto ha sido todo por hoy.\nMuchas gracias por ejecutar este Script, hasta la próxima...Happy Coding!, bye :D\nClark." );
                    keepRunning = false;
                }
                else
                {
                    int maxRange = Integer.parseInt( userAnswer.trim() ); // Se convierte la opcion ingresada por el usuario de texto a entero
            
                    if( maxRange >= 1 )
                    {
                        primeTwins.primeTwinsEngine( maxRange );
                    }
                    else
                        System.out.println( "\nSolo se admiten números enteros positivos mayores o iguales a 1, o la letra 'q' si deseas salir, verifique nuevamente." );
                }
            }
            catch( NumberFormatException nfex )
            {
                System.out.println( "\nOpción ingresada no disponible, solo se admiten números enteros positivos mayores o iguales a 2, o la letra 'q' si deseas salir, verifique nuevamente." );
                System.out.println( "Error: " + nfex.getMessage() );
            }
            catch( Exception ex )
            {
                System.out.println( "\nOops... algo no ha salido bien, revise nuevamente por favor." );
                System.out.println( "Error: " + ex.getMessage() );
            }

        } while( keepRunning );
    }
}

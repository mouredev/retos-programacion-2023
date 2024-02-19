/**
 * Escribe un programa que muestre por consola (con un print) los números de 1 a
 * 100 (ambos incluidos y con un salto de línea entre cada impresión),
 * sustituyendo los siguientes: - Múltiplos de 3 por la palabra "fizz". -
 * Múltiplos de 5 por la palabra "buzz". - Múltiplos de 3 y de 5 a la vez por la
 * palabra "fizzbuzz".
 *
 * @author abel
 */
public class AbelADEJava {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        for (int i = 1; i <= 100; i++) {
            
            //Si es múltiplo de 15
            if (i % 3 == 0 && i % 5 == 0) {
                //Imprimo la palabra "fizzbuzz"
                System.out.println("fizzbuzz");
                //Sinó compruebo si es mútliplo de 5
            } else if (i % 5 == 0) {
                //Imprimo la palabra "buzz"
                System.out.println("buzz");
                //Sinó compruebo si es mútliplo de 3
            } else if (i % 3 == 0) {
                //Imprimo la palabra "fizz"
                System.out.println("fizz");
                //Si no es múltiplo de los anteriores
            } else {
                //Imprimo el número
                System.out.println(i);
            }
            
        }
        
    }

}

class josema294 {

    /*
 * Reto #0: EL FAMOSO "FIZZ BUZZ"* 
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

    public static void main(String[] args) {

       int n=1; 
       recursivo(n);
          
    }

    /*
     * Solucionaremos el ejercicio mediante recursividad y utilizando el operador ternario. La funcion
     * recursivo() hara las operaciones, es void y no devulve nada sino que lo imprime directamente.
     *  
    */
    
    static void recursivo (int n) {
        
        if (n<=100) {

            System.out.println((n%3==0 && n%5==0 ) ? "\033[31mfizzbuzz": (n%3==0)?"\033[32mfizz" : (n%5==0)? "\033[34mbuzz" : "\033[30m" + n );
            n++;
            recursivo(n);

        }

        
    }

   

    
}

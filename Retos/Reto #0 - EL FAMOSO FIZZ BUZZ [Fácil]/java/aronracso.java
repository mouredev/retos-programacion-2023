/**
 * Reto #0: EL FAMOSO "FIZZ BUZZ"
 * Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23
 * 
 * Enunciado
 * 
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
public class aronracso
{
    public static void main(String[] args)
    {
        for(int i = 1; i <= 100; ++i)
        {
            boolean fizz = (i % 3 == 0);
            boolean buzz = (i % 5 == 0);

            if(fizz)
                System.out.print("fizz");

            if(buzz)
                System.out.print("buzz");

            if(!fizz && !buzz)
                System.out.print(i);

            System.out.println();
        }
    }
}
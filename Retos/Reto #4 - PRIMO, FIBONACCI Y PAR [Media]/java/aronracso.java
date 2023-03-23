/**
 * Reto #4: PRIMO, FIBONACCI Y PAR
 * 
 * Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23
 * 
 * Enunciado:
 * 
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
public class aronracso
{
    public static void main(String[] args)
    {
        //Probando
        for(int i = 0; i <= 100; i++)
            comprobarNumero(i);
    }
    
    public static void comprobarNumero(int numero)
    {
        System.out.print(numero);

        if(!esPrimo(numero)) {
            System.out.print(" no");
        }
        System.out.print(" es primo,");

        if(!esFibonacci(numero)) {
            System.out.print(" no");
        }
        System.out.print(" es fibonacci y");

        if(!esPar(numero)) {
            System.out.print(" no");
        }
        System.out.println(" es par");
    }

    /**
     * De: https://www.geeksforgeeks.org/prime-numbers/
     * 
     * @param numero
     * @return
     */
    protected static boolean esPrimo(int numero)
    {
        if (numero <= 1)
            return false;
        else if (numero == 2)
            return true;
        else if (numero % 2 == 0)
            return false;

        for (int i = 3; i <= Math.sqrt(numero); i += 2) {
            if (numero % i == 0)
                return false;
        }
        return true;
    }

    /**
     * De: https://www.ritambhara.in/checking-if-a-number-is-fibonacci/
     * 
     * @param numero
     * @return
     */
    protected static boolean esFibonacci(int numero)
    {
        int a = 0;
        int b = 1;

        if (numero == a || numero == b)
            return true;

        int c = a + b;
        while(c <= numero)
        {
            if(c == numero)
                return true;

            a = b;
            b = c;
            c = a + b;
        }
        return false;
    }

    protected static boolean esPar(int numero)
    {
        return (numero % 2 == 0);
    }
}

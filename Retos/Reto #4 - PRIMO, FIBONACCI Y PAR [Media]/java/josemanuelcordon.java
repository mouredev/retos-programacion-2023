/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
*/

public class Main {
    public static void main(String[] args) {
        solucion(0);
        solucion(13);
        solucion(21);
        solucion(144);
        solucion(-2);
    }

    public static boolean esPar(int n) {
        boolean resultado = (n%2 == 0) ;
        return resultado;
    }
    public static boolean esPrimo(int n) {
        int divisor = 2;
        boolean resultado = !(n<=0);
        while(divisor < n/2) {
            if(n%divisor == 0) {
                resultado = false;
                break;
            } else {
                divisor++;
            }
        }


        return resultado;
    }

    public static boolean esFibonacci(int n) {
        int numero1 = 0;
        int numero2 = 1;
        int variable_de_paso;
        boolean resultado = (n==0);
        for(int i = 0; i<n; i++) {
            if (numero1 + numero2 > n) {
                break;
            }
            if (numero1 + numero2 == n) {
                resultado = true;
            } else {
                variable_de_paso = numero1;
                numero1 = numero2;
                numero2 = numero1 + variable_de_paso;
            }
        }
        return resultado;
    }

    public static void solucion(int n) {
        String esPar = " es par,";
        String esPrimo = " es primo y";
        String esFibonacci = " es fibonaci.";
        if (!esPar(n)) {
            esPar = " no" + esPar;
        }
        if(!esPrimo(n)) {
            esPrimo = " no" + esPrimo;
        }
        if(!esFibonacci(n)) {
            esFibonacci = " no" + esFibonacci;
        }
        System.out.println("El número: " + n + esPar + esPrimo + esFibonacci);
    }
}
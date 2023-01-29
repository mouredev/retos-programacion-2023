
public class mario_16 {

    /*
     * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
     * Ejemplos:
     * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
     * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
     */

    public static void main(String[] args) {

        verificarNumero(0);
        verificarNumero(1);
        verificarNumero(2);
        verificarNumero(3);
        verificarNumero(4);
        verificarNumero(5);
        verificarNumero(6);
        verificarNumero(7);
        verificarNumero(8);
        verificarNumero(9);

    }

    public static void verificarNumero(int numero){

        String esPrimo = esPrimo(numero) ? "es primo, " : "no es primo, ";
        String esFibonacci = esFibonacci(numero) ? "es Fibonacci" : "no es Fibonacci";
        String esPar = numero % 2 == 0 ? "es par" : "es impar";

        System.out.println(numero + " " + esPrimo + esFibonacci + " y " + esPar);

    }

    private static boolean esPrimo(int numero) {
        int cantDivisores = 0;
        for (int i = 1; i <= numero; i++){
            if (numero % i == 0){
                cantDivisores += 1;
            }
        }
        return cantDivisores == 2;
    }

    private static boolean esFibonacci(int n) {

        int calculo = (int) (5 * Math.pow(n, 2) + 4);
        int calculo1 = (int) (5 * Math.pow(n, 2) - 4);
        return esPotenciaAlCuadradoPerfecta(calculo) || esPotenciaAlCuadradoPerfecta(calculo1);
    }

    private static boolean esPotenciaAlCuadradoPerfecta(int calculo) {
        int resultado = (int) Math.sqrt(calculo);
        return calculo == resultado * resultado;
    }


}

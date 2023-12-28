public class Alvarogtz {
    /*
     * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
     * Ejemplos:
     * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
     * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
     */
    public static void main(String[] args){
        System.out.println(evaluateNumber(2));
        System.out.println(evaluateNumber(7));
    }

    private static String evaluateNumber(int number) {
        int fibonacci;
        int first = 0;
        int previous = 1;

        boolean isFibonacci = false;
        boolean isPrimo = true;

        for(int i = 1; i <= number; i++){
            fibonacci = first + previous;
            if(fibonacci == number){
                isFibonacci = true;
                break;
            }
                first = previous;
                previous = fibonacci;
        }

        for(int i = 2; i < number; i++){
            if(number%i == 0){
                isPrimo = false;
                break;
            }
        }

        String texto = "El numero " + number;
        texto += isPrimo?" es primo,":" no es primo,";
        texto += isFibonacci?" es fibonacci":" no es fibonacci";
        texto += number%2 == 0? " y es par": " y es impar";

        return texto;
    }
}

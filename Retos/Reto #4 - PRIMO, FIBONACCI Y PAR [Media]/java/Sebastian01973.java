/**
 * The type Sebastian 01973.
 */
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
public class Sebastian01973 {

    private int number;

    /**
     * Instantiates a new Sebastian 01973.
     *
     * @param number the number
     */
    public Sebastian01973(int number) {
        this.number = number;
    }


    /**
     * Is par boolean.
     *
     * @return the boolean
     */
    public boolean isPar(){
        return number%2==0;
    }

    /**
     * Is prime boolean.
     *
     * @return the boolean
     */
    public  boolean isPrime() {
        // El 0, 1 y 4 no son primos
        if (number == 0 || number == 1 || number == 4) {
            return false;
        }
        for (int x = 2; x < number / 2; x++) {
            // Si es divisible por cualquiera de estos números, no es primo
            if (number % x == 0)
                return false;
        }
        // Si no se pudo dividir por ninguno de los de arriba, sí es primo
        return true;
    }

    /**
     * Is fibonacci boolean.
     *
     * @return the boolean
     */
    public boolean isFibonacci(){
        int fibonacci = 0;
        int fibonacciAnt = 1;
        int suma = 1;
        while(number >= fibonacci){
            suma = fibonacci + fibonacciAnt;
            fibonacci = fibonacciAnt;
            fibonacciAnt = suma;
            if(fibonacci == number){
                return true;
            }
        }
        return false;
    }

    /**
     * Result string.
     *
     * @return the string
     */
    /*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
    public String result(){
        if(isFibonacci() && isPrime() && isPar()){
            return  "Numero " + number + " es primo, fibonacci y es par";
        } else if (isFibonacci() && isPar()) {
            return  "Numero " + number + " es fibonacci y es par, pero no es primo";
        } else if (isPrime() && isFibonacci()) {
            return  "Numero " + number + " es primo, es fibonacci y es impar";
        } else if (isPrime() && isPar()) {
            return  "Numero " + number + " es primo, no es fibonacci y es par";
        }else if (isPrime()){
            return  "Numero " + number + " es primo, no es fibonacci y es impar";
        } else if (isFibonacci()) {
            return  "Numero " + number + " es fibonacci, no es primo y es impar";
        } else if (isPar()) {
            return  "Numero " + number + " es par, no es fibonacci y no es primo";
        }else {
            return "El Numero no cumple con los criterios anteriores";
        }
    }

    /**
     * The entry point of application.
     *
     * @param args the input arguments
     */
    public static void main(String[] args) {
        Sebastian01973 test = new Sebastian01973(2);
        System.out.println(test.result());

        Sebastian01973 test1 = new Sebastian01973(5);
        System.out.println(test1.result());

        Sebastian01973 test2 = new Sebastian01973(21);
        System.out.println(test2.result());

        Sebastian01973 test3 = new Sebastian01973(17);
        System.out.println(test3.result());
    }
}

/**
 * Listar los números del 1 al 100 ambos incluidos
 * Si el número es múltiplo de 3 sustituir por la palabra 'fizz'
 * Si el número es múltiplo de 5 sustituir por la palabra 'buzz'
 * Si el número es múltiplo de 3 y 5 sustituir por la palabra 'fizzbuzz'
 */
public class vandresca {
    public static void main(String[] args) {
        for(int i = 0; i<100; i++){
            if(i%15==0) System.out.println("fizzbuzz");
            else if(i%3==0) System.out.println("fizz");
            else if(i%5==0) System.out.println("buzz");
            else System.out.println(i);
        }
    }
}
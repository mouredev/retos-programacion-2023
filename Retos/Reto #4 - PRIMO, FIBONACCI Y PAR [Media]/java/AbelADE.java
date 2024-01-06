import java.util.HashMap;
import java.util.Scanner;

/**
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 *
 * @author abel
 */
public class NumbersClasificator {

    /**
     * Número a clasificar.
     */
    private int number;

    /**
     * Devuelve el número a clasificar.
     *
     * @return el número a clasificar.
     */
    public int getNumber() {
        return number;
    }

    /**
     * Sobrescribe el número a clasificar.
     *
     * @param number el número a clasificar.
     */
    public void setNumber(int number) {
        this.number = number;
    }

    /**
     * Pide un número al usuario y lo almacena en el atributo 'number'.
     */
    public void giveNumber() {
        Scanner scan = new Scanner(System.in);

        System.out.println();
        System.out.print("Dame un número: ");
        number = scan.nextInt();
    }

    /**
     * Devuelve un texto indicando si el atributo 'number' es primo o no.
     *
     * @return un texto indicando si el atributo 'number' es primo o no.
     */
    private String primeNumber() {
        boolean isPrime = true;

        if (number > 1) {
            for (int i = 2; i < number; i++) {
                if (number % i == 0) {
                    isPrime = false;
                }
            }
        } else {
            isPrime = false;
        }

        if (isPrime) {
            return "es primo, ";
        } else {
            return "no es primo, ";
        }
    }

    /**
     * Devuelve un texto indicando si el atributo 'number' es fibonacci o no.
     *
     * @return un texto indicando si el atributo 'number' es fibonacci o no.
     */
    private String fibonacciNumber() {

        HashMap<Integer, Integer> fibonacci = new HashMap<>();

        fibonacci.put(1, 1);
        fibonacci.put(2, 1);

        for (int i = 3; i <= number + 10; i++) {
            int fi = fibonacci.get(i - 1) + fibonacci.get(i - 2);
            fibonacci.put(i, fi);
        }

        boolean isfibonacci = fibonacci.containsValue(number);

        if (isfibonacci) {
            return "fibonacci ";
        } else {
            return "no es fibonacci ";
        }
    }

    /**
     * Devuelve un texto indicando si el atributo 'number' es par o impar.
     *
     * @return un texto indicando si el atributo 'number' es par o impar.
     */
    private String parNumber() {

        if (number % 2 == 0) {
            return "y es par.";
        } else {
            return "y es impar.";
        }
    }

    /**
     * Devuelve un texto con toda la clasificación del atributo 'number'.
     *
     * @return un texto con toda la clasificación del atributo 'number'.
     */
    public String NumberClasificator() {
        String text = number + " ";
        text += primeNumber();
        text += fibonacciNumber();
        text += parNumber();
        return text;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        NumbersClasificator clasificator = new NumbersClasificator();
        Scanner scan = new Scanner(System.in);
        boolean exit = false;

        System.out.println("Bienvenido al programa clasificador de números");
        
        do {
            int option;
            do {
                System.out.println();
                System.out.println("--------------------------");
                System.out.println("¿Qué quieres hacer?");
                System.out.println("1 - Clasificar un número");
                System.out.println("2 - Salir");
                System.out.println("--------------------------");
                option = scan.nextInt();

                if (option < 1 || option > 2) {
                    System.err.println("Opción incorrecta.");
                }

            } while (option < 1 || option > 2);

            switch (option) {
                case 1:
                    clasificator.giveNumber();
                    System.out.println(clasificator.NumberClasificator());
                    break;
                case 2:
                    exit = true;
                    break;
            }
        } while (!exit);
    }

}

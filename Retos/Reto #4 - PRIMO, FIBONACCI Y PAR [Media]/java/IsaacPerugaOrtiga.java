import java.util.Scanner;

public class Main {


    public static void main(String[] args) {

        int num, result, firstTerm = 0, secondTerm = 1, thirdTerm = 0;
        boolean esPrimo = true;
        String texto = "";

        Scanner teclado = new Scanner(System.in);

        System.out.println("Que número quieres comprobar: ");
        num = teclado.nextInt();

        //Primo
        if(num <= 1){
            esPrimo = false;
        }
        for (int i = 2; i < num; i++) {
            result = num % i;
            if (result == 0) {
                esPrimo = false;
            }

        }
        if (esPrimo) {
            texto += num + " es primo";
        } else {
            texto += num + " no es primo";
        }


        while (thirdTerm < num) {
            thirdTerm = firstTerm + secondTerm;

            firstTerm = secondTerm;

            secondTerm = thirdTerm;
        }

        if (thirdTerm == num) {
            texto += ",es Fibonacci";
        } else {
            texto += ",no es Fibonacci";
        }

        //Par
        texto += (num % 2 == 0) ? " y es par." : "y es impar.";

        System.out.println(texto);
    }
}

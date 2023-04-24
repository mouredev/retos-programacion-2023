import java.util.Scanner;

import org.omg.CORBA.NO_MEMORY;

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        boolean correct;
        int number = 0;

        do{
            correct = true;
            System.out.println("Introduce un número para analizar: ");
            
            try{
                number = Integer.parseInt(josepmonclus.entrada.nextLine());
            } catch(Exception e){
                System.out.println("Número incorrecto!");
                correct = false;
            }
        } while(!correct);

        josepmonclus.analizeNumber(number);
    }

    private void analizeNumber(int number) {

        boolean primo = true, fibonacci = true, par = true;

        // PRIMO
        for(int i = 2; i < number; i++) {
            if(number%i == 0) {
                primo = false;
                break;
            }
        }

        // FIBONACCI
        int f1 = 1, f2 = 1;
        while (f2 < number) {
            int aux = f1 + f2;
            f1 = f2;
            f2 = aux;
        }

        if(f2 == number) fibonacci = true;
        else fibonacci = false;

        // PAR - IMPAR
        par = number % 2 == 0;

        System.out.println(number + " " + (primo ? "es primo" : "no es primo") + ", " + (fibonacci ? "es fibonacci" : "no es fibonacci") + " y " + (par ? "es par" : "es impar"));
    }
}

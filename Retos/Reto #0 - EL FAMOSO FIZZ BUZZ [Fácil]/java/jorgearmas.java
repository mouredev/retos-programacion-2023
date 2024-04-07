import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        System.out.print("--- Fizz Buzz ---");
        System.out.print("\nIngrese un rango de números");
        Scanner scanner = new Scanner(System.in);
        System.out.println("\nIngrese Inicio -> ");
        int inicio = scanner.nextInt();
        System.out.println("Ingrese Fin -> ");
        int fin = scanner.nextInt();
        System.out.println("-----------------");
        fizzBuzz(inicio, fin);
    }

    public static void fizzBuzz(int inic, int fn){
        for(int i=inic; i<=fn; i++){
            if(i%3==0 && i%5!=0){
                System.out.println(i+" Fizz");
            } else if (i%3!=0 && i%5==0) {
                System.out.println(i+" Buzz");
            } else if (i%3==0 && i%5==0){
                System.out.println(i+" Fizz-Buzz");
            }
            else {
                System.out.println(i+" - Rule does not apply ---");
            }
        }
    }
}
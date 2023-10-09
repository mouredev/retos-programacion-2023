package reto_04;
import java.util.InputMismatchException;
import java.util.Scanner;

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
public class JesusWay69 {

  public static void main(String[] args) {
try{
    Scanner sc = new Scanner(System.in);
    String re = "[0-9]+";
    System.out.println("Introduzca número a evaluar: ");
    String num = sc.nextLine();
   if(num.matches(re)) {
    if (esprimo(Integer.parseInt(num))) {
      System.out.print("El número " + num + " es primo ");
    } else {
      System.out.print("El número " + num + " no es primo");
    }
    if (espar(Integer.parseInt(num))) {
      System.out.print(", es par");
    } else {
      System.out.print(", es impar");
    }
    if (esfibonacci(Integer.parseInt(num))) {
      System.out.println(" y es fibonacci");
    } else {
      System.out.println(" y no es fibonacci");
    }
   }
}catch (InputMismatchException ex){
  System.out.println("Error: " + ex);
}
  }

  private static boolean esprimo(int num) {
    boolean primo = true;
    for (int i = 2; i < num; i++) {
      if (num % i == 0) {
        primo = false;
        break;
      }
    }
    return primo;
  }

  private static boolean espar(int num) {

      return num % 2 == 0;

  }

  private static boolean esfibonacci(int num){
      int a = 1;
      int b = 1;
      for (int i = 2; i <= num; i++) {
        if(num == b){
          break;
        }else if(i < num){
          b=a+b;
          a=b-a;
        }else{
          return false;
        }
    }
  return true;  
  }

}

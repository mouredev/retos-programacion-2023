/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 * Hecho por Albano Diez el 25/01/2023
 */

import java.util.Scanner;

public class reto4 {

    public static void main(String[] args) {
        Scanner sc=new Scanner (System.in);
        int num=0;
        
        System.out.println("Dime un numero positivo");
        num=sc.nextInt();
        System.out.print(num);
        if (isPrimo(num)) {
            System.out.print(" es primo,");
        }else{
             System.out.print("  no es primo,");
        }
        
        if (isFibonnacci(num)) {
            System.out.print(" fibonacci");
        }else{
             System.out.print("  no es fibonacci");
        }
        
        if (isPar(num)) {
            System.out.print(" y es par");
        }else{
             System.out.print("  y no es par");
        }
        

    }
   private static boolean isPrimo(int intNum) {
        if (intNum == 0 || intNum == 1) {
            return false;
        }
        for (int i = 2; i < intNum / 2; i++) {
            if (intNum % i == 0)
                return false;
        }

        return true;
    }
    private static boolean isFibonnacci(int intNum) {
      int intFibo1 = 0;
      int intFibo2 = 1;
      int intAuxiliar;

      while (intFibo1 + intFibo2 <= intNum) {
          intAuxiliar = intFibo1;
          intFibo1 = intFibo2;
          intFibo2 = intAuxiliar + intFibo1;
          if (intNum == intFibo2) {
              return true;
          }
      }
      return false;
  }
    public static boolean isPar(int num){
        if (num%2==0) {
            return true;
            
        }else{
            return false;
        }
    }
    
}

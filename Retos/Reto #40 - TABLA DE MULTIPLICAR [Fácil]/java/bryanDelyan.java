/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

 import java.util.Scanner;



 public class bryanDelyan{
     int numero;
     Scanner entrada = new Scanner(System.in);
 
     public void printNumber() {
         //Try catch si mete un numero no entero o negativo o un caracter
         try {
         System.out.println("Ingrese un número:");
         numero =  entrada.nextInt();
         if(numero < 0){
             System.out.println("Ingrese un número positivo:");
         }
         else{
             printTable(numero);
         }
         } catch (Exception e) {
             System.out.println("Entrada inválida, por favor ingrese un número entero positivo");
         } 
         finally {
             entrada.close();
         }
     }
     public void printTable(int numero){
         System.out.println("Tabla de multiplicar para " + numero + ":");
         for(int i = 1 ; i<=10;i++){
             System.out.println(numero + " x " + i + " = " + numero*i);
         }
     }
     public static void main(String[] args) {
         bryanDelyan n = new bryanDelyan();
         n.printNumber();
     }
 }
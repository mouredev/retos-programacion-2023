/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/
public class Main{
  public static void main(String args[]){
   for(int i=1;i<=100;i++){
    //Compruebo si el numero es multiplo de 3 o 5 o si es de ambos, utilizando el operador ternario para realizarlo.
    //en el caso de que el numero no se ni multiplo de 3 ni 5 muestro el numero
    //pero como i es entero y la variable que almacena el resultado de la comparacion es String transformo i a string utilizando el
    //metodo String.valueOf().
    String fb = i%3==0 && i%5==0?"fizzbuzz":i%3==0?"fizz":i%5==0?"buzz":String.valueOf(i);
    //muestro el resultado de la comparacion previa
    System.out.println(fb);
  }
 }
}

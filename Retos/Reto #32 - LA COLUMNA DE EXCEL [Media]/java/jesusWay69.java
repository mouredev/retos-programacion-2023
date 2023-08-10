package reto_32;
import java.util.Scanner;
/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letters de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */
public class jesusWay69 {

  public static void main(String[] args) {
    String l;
    Scanner sc = new Scanner(System.in, "ISO-8859-1");
    System.out.print("Introduzca el código de columna: ");
    l = sc.next();
    if(l.matches("[a-zA-Z]+")) letters(l.toUpperCase());
    else System.out.println("Sólo se pueden calcular "
        + "secuencias de letras de la 'a' a la 'z' sin incluir la 'ñ'");
  }
  private static void letters(String l) {
    long num1 = 0;
    long num2 = 0;
    if (l.length() > 1) {
      for (int i = l.length() - 1; i >= 0; i--) {
        num2=num1+num2;
        num1 = (long) l.charAt(i) - 64;
        for (int j = l.length() - 1; j > i; j--) 
         num1 = num1*26;
      }
    } else num1 = (byte)l.charAt(0) -64;
    System.out.println("La columna equivalente al código "+ l +" es la número: " + (num1 + num2));
  }
}

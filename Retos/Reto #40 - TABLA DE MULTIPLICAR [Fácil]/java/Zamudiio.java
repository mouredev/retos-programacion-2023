
/**
 * Zamudiio
 */
import java.util.Scanner;

public class Zamudiio {

   public static void main(String[] args) {
      Scanner myScanner = new Scanner(System.in);
      System.out.println("🔢 Tabla de multiplicar 🔢");
      System.out.println("Ingresa algun numero entero");
      String number = myScanner.nextLine();
      
      if(!tryIntParse(number)){
         System.out.println("Porfavor ingresa un formato valido, debe ser un numero entero");
         main(args);
      }else{
         operation(Integer.parseInt(number));
      }

      myScanner.close();
   }

   public static void operation(int number) {
      for (int i = 1; i <= 10; i++) {
         System.out.println(number + " x " + i + " = " + i * number);
      }
   }

   public static Boolean tryIntParse(String number) {
      try {
         Integer.parseInt(number);
         return true;
      } catch (NumberFormatException e) {
         return false;
      }
   }

}
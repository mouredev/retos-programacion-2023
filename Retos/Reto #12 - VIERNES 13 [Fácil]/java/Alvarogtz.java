import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;

public class Alvarogtz {
    public static void main(String [] args){
        boolean correcto = false;
        int month = 0;
        int year = 0;
        Scanner sc = new Scanner(System.in);

        while(!correcto) {
            try {
                System.out.println("Introduce mes(numerico): ");
                month = sc.nextInt();
                System.out.println("Introduce año: ");
                year = sc.nextInt();

                if(month > 0 && month < 13 && year > 1000)
                    correcto = true;

            } catch (Exception e) {
                System.out.println("Fecha teclada incorrecta");
            }
        }

        if (checkFriday13(month, year))
            System.out.println("Este mes y año tiene un VIERNES 13 !!");
        else
            System.out.println("Este mes y año NO tiene un VIERNES 13... Prueba de nuevo.");
    }

    private static boolean checkFriday13(int month, int year) {
        Calendar cal = Calendar.getInstance();
        cal.set(year,month-1,13);
        int dia = cal.get(Calendar.DAY_OF_WEEK);

        if(dia == Calendar.FRIDAY)
            return true;

        return false;
    }
}

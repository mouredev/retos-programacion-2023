import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.Scanner;

/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        int month = josepmonclus.getMonth();
        int year = josepmonclus.getYear();

        boolean viernes13 = josepmonclus.haveViernes13(month, year);

        System.out.println(viernes13 ? "Si que existe viernes 13!" : "No existe viernes 13!");
    }

    private boolean haveViernes13(int month, int year) {
        Calendar cal = new GregorianCalendar(year, month - 1, 13);

        if(cal.get(Calendar.DAY_OF_WEEK) == Calendar.FRIDAY) {
            return true;
        } else {
            return false;
        }
    }

    private int getMonth() {
        int month = 0;

        boolean correctMonth = false;
        while (!correctMonth) {
            System.out.println("Introduce el mes [1-12]:");
            
            String sMonth = entrada.nextLine();

            try {
                month = Integer.parseInt(sMonth);

                if(month >= 1 && month <= 12) {                    
                    correctMonth = true;
                }
            } catch(Exception e) {
                correctMonth = false;
            }

            if(!correctMonth) System.out.println("Mes incorrecto!");
        }

        return month;
    }

    private int getYear() {
        int year = 0;

        boolean correctYear = false;
        while (!correctYear) {
            System.out.println("Introduce el año [yyyy]:");

            String sYear = entrada.nextLine();

            try{
                year = Integer.parseInt(sYear);

                correctYear = true;
            } catch(Exception e) {
                correctYear = false;
            }

            if(!correctYear) System.out.println("Año incorrecto!");
        }

        return year;
    }
}

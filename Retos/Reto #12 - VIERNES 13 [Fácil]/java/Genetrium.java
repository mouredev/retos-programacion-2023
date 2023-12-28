package retoprogramacion12;

import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.Scanner;

public class Genetrium {

    public static void main(String[] args) {
        String dateMonth, dateYear;

        dateMonth = validarMes();
        dateYear = validarAnio();

        String monthYear = dateMonth + "/" + dateYear;
        boolean isFriday13 = isFriday13(monthYear);

        if(isFriday13){
            System.out.println("El Mes: "+dateMonth+" del año: "+dateYear+" tiene un viernes 13");
        }else{
            System.out.println("El Mes: "+dateMonth+" del año: "+dateYear+" NO tiene un viernes 13");
        }
    }

    public static boolean isFriday13(String monthYear){

        try {
            // Dar formato a la fecha
            DateFormat formatter= new SimpleDateFormat("dd/MM/yyyy");
            // Crear calendario
            Calendar calendar = new GregorianCalendar();
            // Dar formato a la fecha
            Date date= formatter.parse("13/"+monthYear);
            // Establecer la fecha del calendario
            calendar.setTime(date);

            // Guardar número de día de la semana y día del mes en variables
            int dayOfWeek = calendar.get(Calendar.DAY_OF_WEEK);
            int dayOfMonth = calendar.get(Calendar.DAY_OF_MONTH);
            // Comparar si es viernes y el día del mes
            return dayOfWeek == 6 && dayOfMonth == 13;

        } catch (ParseException e) {
            throw new RuntimeException(e);
        }
    }

    public static String validarMes(){
        Scanner sc = new Scanner(System.in);
        int mes;
        do{
            System.out.println("Inserte mes [MM]:");
            mes = sc.nextInt();
        }while(mes < 1 || mes > 12);
        return String.valueOf(mes);
    }

    public static String validarAnio(){
        Scanner sc = new Scanner(System.in);
        int anio;
        do{
            System.out.println("Inserte año [MM]:");
            anio = sc.nextInt();
        }while(anio < 0);
        return String.valueOf(anio);
    }
}

/*
 * Crea una función que sea capaz de detectar si existe un viernes 13
 * en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

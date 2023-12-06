/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */

import java.util.GregorianCalendar;

public class JaumeViBU {
    public static void main(String[] args) {
        System.out.println(isThereFriday13InMonthYear(1,2023));
        System.out.println(isThereFriday13InMonthYear(2,2023));
        System.out.println(isThereFriday13InMonthYear(3,2023));
        System.out.println(isThereFriday13InMonthYear(4,2023));
        System.out.println(isThereFriday13InMonthYear(5,2023));
        System.out.println(isThereFriday13InMonthYear(6,2023));
        System.out.println(isThereFriday13InMonthYear(7,2023));
        System.out.println(isThereFriday13InMonthYear(8,2023));
        System.out.println(isThereFriday13InMonthYear(9,2023));
        System.out.println(isThereFriday13InMonthYear(10,2023));
        System.out.println(isThereFriday13InMonthYear(11,2023));
        System.out.println(isThereFriday13InMonthYear(12,2023));

    }

    public static boolean isThereFriday13InMonthYear(int month,int year){
        GregorianCalendar calendar=new GregorianCalendar(year,month-1,13 );

        int dayOfWeek=calendar.get(GregorianCalendar.DAY_OF_WEEK);
        boolean isFriday=dayOfWeek==6;

        return isFriday;
    }
}
import java.util.Map;

/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */
public class masdos {

    public static void main(String[] args) {
        System.out.println(hasFridayThirteenth(8, 1992));
        System.out.println(hasFridayThirteenth(8, 1993));

    }

    private static Boolean hasFridayThirteenth(int month, int year) {
        return calculateDayOfTheWeek(13, month, year).equals("Friday");
    }

    /**
     *  Based on Zeller’s Congruence
     *  (http://people.csail.mit.edu/ddeford/Crossroads_pdfs/Date_Methods.pdf)
     */
    private static String calculateDayOfTheWeek(int day, int month, int year) {
        Map<Integer, String> daysOfTheWeek =
                Map.of(
                        1, "Sunday",
                        2, "Monday",
                        3, "Tuesday",
                        4, "Wednesday",
                        5, "Thursday",
                        6, "Friday",
                        7, "Saturday"
                );
        int quotientYear = year / 100;
        int remainderYear = year % 100;
        int dayOfTheWeek =
                (day +
                        ((13 * (month + 1)) / 5) +
                        remainderYear +
                        (remainderYear / 4) +
                        (quotientYear / 4) -
                        (2 * quotientYear)) %
                        7;
        return daysOfTheWeek.get(dayOfTheWeek);
    }
}

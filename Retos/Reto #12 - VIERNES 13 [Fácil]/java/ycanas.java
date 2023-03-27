import java.time.LocalDate;
import java.time.DayOfWeek;

public class ycanas{
    public static Boolean hasFridayThirteenth(int month, int year){
        final int DAY = 13;

        LocalDate date = LocalDate.of(year, month, DAY);
        DayOfWeek day  = date.getDayOfWeek();

        return day == DayOfWeek.FRIDAY;
    }

    public static void main(String[] args){
        System.out.println(hasFridayThirteenth(10, 2023));
        System.out.println(hasFridayThirteenth(3, 2023));
    }
}
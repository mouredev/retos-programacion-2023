import java.time.DayOfWeek;
import java.time.LocalDate;

public class Friday13 {

    public static boolean check(int year, int month) {
        int day = 13;
        LocalDate date = LocalDate.of(year, month, day);
        return date.getDayOfWeek().compareTo(DayOfWeek.FRIDAY) == 0;
    }

}

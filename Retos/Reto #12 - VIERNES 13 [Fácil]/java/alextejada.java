import java.time.DayOfWeek;
import java.time.LocalDate;

public class alextejada {

    public static void main(String[] args) {

    }

    public static boolean isFridayThirteen(int month, int year) {
        return LocalDate.of(year, month, 13).getDayOfWeek().equals(DayOfWeek.FRIDAY);
    }
}

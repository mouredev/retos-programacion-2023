import org.junit.Test;
import static org.junit.Assert.*;

import java.time.DayOfWeek;
import java.time.LocalDate;

public class Qv1ko {

    @Test
    public void testing() {
        assertTrue(isFridayThirteenth(10, 2023));
        assertFalse(isFridayThirteenth(6, 2023));
        assertNotNull(isFridayThirteenth(8, 2023));
    }

    private static boolean isFridayThirteenth(int month,int year) {

        try {
            return LocalDate.of(year, month, 13).getDayOfWeek() == DayOfWeek.FRIDAY;
        } catch (Exception exc) {
            return false;
        }
        
    }

}

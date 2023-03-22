import java.time.DayOfWeek;
import java.time.LocalDate;

public class Qv1ko {

    public static void main(String[] args) {
        System.out.println(isFridayThirteenth(3,2023));
    }//main

    private static boolean isFridayThirteenth(int month,int year) {
        month=(month<1||month>12)? LocalDate.now().getMonthValue():month;  
        return LocalDate.of(year,month,13).getDayOfWeek()==DayOfWeek.FRIDAY;
    }//isFridayThirteenth

}//class
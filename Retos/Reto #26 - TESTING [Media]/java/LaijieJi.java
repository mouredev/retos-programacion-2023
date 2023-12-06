import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.*;

public class LaijieJi {
	public static void main(String[] args) {
        int year = 2023;
		int month = 1;//On 13, January of 2023 there is a Friday 13th, but in the next two months there is not.
        for(int i = 0; i < 3; i++){
            if(checkFriday(year, month) == true){
                System.out.println("Case #" + i + ": Passed");
            } else {
                System.out.println("Case #" + i + ": Wrong");
            }
            ++month;
        }
	}
    //Shortened version of the code for Checking if a date was Friday 13th. The input part was eliminated
    public static boolean checkFriday(int year, int month){
		LocalDate date = LocalDate.of(year, month, 13);
		if(date.getDayOfWeek() == DayOfWeek.FRIDAY) {
			return true;
		}else {
			return false;
		}
    }
}

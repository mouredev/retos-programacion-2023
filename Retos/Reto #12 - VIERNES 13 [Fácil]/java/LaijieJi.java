import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.*;

public class LaijieJi {
	public static void main(String[] args) {
			Scanner sc = new Scanner(System.in).useLocale(Locale.US);
			int year;
			int month;
			System.out.println("Write a year: ");
			year = sc.nextInt();
			System.out.println("Write a month: ");
			month = sc.nextInt();
			LocalDate date = LocalDate.of(year, month, 13);
			if(date.getDayOfWeek()== DayOfWeek.FRIDAY) {
				System.out.println("The specified data is a Friday 13th");
			}else {
				System.out.println("The specified data is not a Friday 13th");
			}
			sc.close();
	}
}

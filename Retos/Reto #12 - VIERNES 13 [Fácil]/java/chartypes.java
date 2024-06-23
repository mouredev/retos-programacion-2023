import java.time.LocalDate;
import java.time.DayOfWeek;

class chartypes {
  public static void main(String[] args) {
    System.out.println(friday13th(1, 2023));
    System.out.println(friday13th(2, 2023));
    System.out.println(friday13th(3, 2023));
    System.out.println(friday13th(4, 2023));
    System.out.println(friday13th(5, 2023));
    System.out.println(friday13th(6, 2023));
    System.out.println(friday13th(7, 2023));
    System.out.println(friday13th(8, 2023));
    System.out.println(friday13th(9, 2023));
    System.out.println(friday13th(10, 2023));
    System.out.println(friday13th(11, 2023));
    System.out.println(friday13th(12, 2023));

  }

  public static boolean friday13th(int month, int year) {
    LocalDate date = LocalDate.of(year, month, 13);
    return date.getDayOfWeek() == DayOfWeek.FRIDAY;

  }
}

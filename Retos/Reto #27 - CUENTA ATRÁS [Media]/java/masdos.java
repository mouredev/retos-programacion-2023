import java.time.LocalDateTime;

public class masdos {

  public static void main(String[] args) {
    countDown(10, 1);
  }

  private static void countDown(int startNumber, int secondsBetweenNumbers) {
    if (startNumber > 0 && secondsBetweenNumbers > 0) {
      LocalDateTime timeValid = LocalDateTime.now().plusSeconds(secondsBetweenNumbers);
      while (startNumber > 0) {
        if (LocalDateTime.now().isAfter(timeValid)) {
          System.out.println(--startNumber);
          timeValid = timeValid.plusSeconds(secondsBetweenNumbers);
        }
      }
    }
  }
}
import java.util.Arrays;
import java.util.Scanner;

public class chartypes {

  public static void main(String[] args) {
    SortingHat hat = new SortingHat();
    hat.choiceHouse("Harry");
  }
}

class SortingHat {

  private final String[] QUESTIONS = { "What trait do you admore most?", "How do you approach challenges?",
      "What kind of people do you enjoy being around?", "What friendship quality matters most to you?",
      "What drives you to succeed?" };
  private final String[] GRYFFINDOR_ANSWERS = { "Bravery", "Head-on", "Adventurous", "Loyalty", "Making a difference" };
  private final String[] RAVENCLAW_ANSWERS = { "Intelligence", "Strategically", "Intellectual", "Intellect",
      "Pursuit of knowledge" };
  private final String[] HUFFLEPUFF_ANSWERS = { "Loyalty", "Persistently", "Kind-hearted", "Trustworthiness",
      "Helping others" };
  private final String[] SLYTHERIN_ANSWERS = { "Ambition", "Resourcefully", "Ambitious", "Ambition",
      "Achieving recognition" };

  private int gryffindor = 0;
  private int slytherin = 0;
  private int hufflepuff = 0;
  private int ravenclaw = 0;

  public void choiceHouse(String name) {
    makeQuestions();
    int[] HOUSES_POINTS = { gryffindor, slytherin, hufflepuff, ravenclaw };
    int max = Arrays.stream(HOUSES_POINTS).max().getAsInt();

    if (max == 0)
      System.out.println("Something went wrong try again. :(");
    else if (max == gryffindor)
      System.out.println("Congrats " + name + " your house is Gryffindor");
    else if (max == slytherin)
      System.out.println("Congrats " + name + " your house is Slytherin");
    else if (max == hufflepuff)
      System.out.println("Congrats " + name + " your house is Hufflepuff");
    else if (max == ravenclaw)
      System.out.println("Congrats " + name + " your house is Ravenclaw");

  }

  public void makeQuestions() {
    Scanner choice = new Scanner(System.in);

    for (int i = 0; i < QUESTIONS.length; i++) {
      System.out.println("\nQUESTION: ");
      System.out.println(QUESTIONS[i]);
      System.out.println("\nANSWERS: ");
      System.out.println("1." + GRYFFINDOR_ANSWERS[i]);
      System.out.println("2." + RAVENCLAW_ANSWERS[i]);
      System.out.println("3." + HUFFLEPUFF_ANSWERS[i]);
      System.out.println("4." + SLYTHERIN_ANSWERS[i]);

      switch (choice.nextInt()) {
        case 1:
          gryffindor++;
          break;
        case 2:
          ravenclaw++;
          break;
        case 3:
          hufflepuff++;
          break;
        case 4:
          slytherin++;
          break;
        default:
          System.out.println("You must select a correct value");
          return;
      }
    }
  }

}

/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class anmac {
  public enum House {
    GRYFFINDOR("🦁", 0),
    SLYTHERIN("🐍", 0),
    RAVENCLAW("🦅", 0),
    HUFFLEPUFF("🦡", 0);

    private final String emoji;
    private int score;

    House(String emoji, int score) {
      this.emoji = emoji;
      this.score = score;
    }

    public String getEmoji() {
      return emoji;
    }

    public int getScore() {
      return score;
    }

    public void addScore(int score) {
      this.score += score;
    }

    public static House getHouseWithHighestScore() {
      List<House> topHouses = new ArrayList<>();
      int highestScore = -1;
      for (House house : House.values()) {
        if (house.getScore() > highestScore) {
          highestScore = house.getScore();
          topHouses.clear();
          topHouses.add(house);
        } else if (house.getScore() == highestScore) {
          topHouses.add(house);
        }
      }

      if (topHouses.size() > 1) {
        int index = random.nextInt(topHouses.size());
        return topHouses.get(index);
      }
      return topHouses.get(0);
    }

    public static void resetScores() {
      for (House house : House.values()) {
        house.score = 0;
      }
    }
  }

  private static final Random random = new SecureRandom();

  public static void main(String[] args) {
    System.out.println("========================================================================");
    System.out.println("Bienvenido al Sombrero Seleccionador del Universo Mágico de Harry Potter");
    System.out.println("========================================================================");

    List<Question> questions = new ArrayList<>();
    questions.add(
        new Question(
            "¿Cómo te definirías?",
            new Choice[] {
              new Choice("Valiente", House.GRYFFINDOR),
              new Choice("Ambicioso", House.SLYTHERIN),
              new Choice("Sabio", House.RAVENCLAW),
              new Choice("Leal", House.HUFFLEPUFF)
            }));
    questions.add(
        new Question(
            "¿Cúal es tu clase favorita?",
            new Choice[] {
              new Choice("Vuelo", House.GRYFFINDOR),
              new Choice("Pociones", House.SLYTHERIN),
              new Choice("Defensa contra las artes oscuras", House.RAVENCLAW),
              new Choice("Animales fantásticos", House.HUFFLEPUFF)
            }));
    questions.add(
        new Question(
            "¿Dónde pasarías más tiempo?",
            new Choice[] {
              new Choice("Invernadero", House.GRYFFINDOR),
              new Choice("Biblioteca", House.SLYTHERIN),
              new Choice("En la sala común", House.RAVENCLAW),
              new Choice("Explorando", House.HUFFLEPUFF)
            }));
    questions.add(
        new Question(
            "¿Cúal es tu color favorito?",
            new Choice[] {
              new Choice("Rojo", House.GRYFFINDOR),
              new Choice("Azul", House.SLYTHERIN),
              new Choice("Verde", House.RAVENCLAW),
              new Choice("Amarillo", House.HUFFLEPUFF)
            }));
    questions.add(
        new Question(
            "¿Cúal es tu mascota favorita?",
            new Choice[] {
              new Choice("Sapo", House.GRYFFINDOR),
              new Choice("Lechuza", House.SLYTHERIN),
              new Choice("Gato", House.RAVENCLAW),
              new Choice("Serpiente", House.HUFFLEPUFF)
            }));

    try (Scanner scanner = new Scanner(System.in)) {
      for (Question question : questions) {
        House house = askQuestion(question, scanner);
        house.addScore(1);
      }
    }
    House selectedHouse = House.getHouseWithHighestScore();
    System.out.println(
        "¡Has sido seleccionado para "
            + selectedHouse.name()
            + " "
            + selectedHouse.getEmoji()
            + "!");
    House.resetScores();
  }

  private static House askQuestion(Question question, Scanner scanner) {
    System.out.println(question.getText());
    for (int i = 0; i < question.getChoices().length; i++) {
      System.out.println((i + 1) + ". " + question.getChoices()[i].getText());
    }
    int answer = getInput(scanner, question.getChoices().length);
    return question.getChoices()[answer - 1].getHouse();
  }

  private static int getInput(Scanner scanner, int numberOfChoices) {
    while (true) {
      try {
        System.out.print("Selecciona una alternativa (e.g. 1): ");
        int answer = Integer.parseInt(scanner.nextLine());
        if (answer >= 1 && answer <= numberOfChoices) {
          return answer;
        }
        System.err.println("Respuesta incorrecta. Inténtalo de nuevo.");
      } catch (NumberFormatException | InputMismatchException e) {
        System.err.println("Debes ingresar un NÚMERO. Inténtalo de nuevo.");
      }
    }
  }
}

class Question {
  private final String text;
  private final Choice[] choices;

  public Question(String text, Choice[] choices) {
    this.text = text;
    this.choices = choices;
  }

  public String getText() {
    return text;
  }

  public Choice[] getChoices() {
    return choices;
  }
}

class Choice {
  private final String text;
  private final anmac.House house;

  public Choice(String text, anmac.House house) {
    this.text = text;
    this.house = house;
  }

  public String getText() {
    return text;
  }

  public anmac.House getHouse() {
    return house;
  }
}

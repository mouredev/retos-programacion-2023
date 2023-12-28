public class Qv1ko {

  public static void main(String[] args) {
    leetTranslator("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ex ex, volutpat vel metus vel, feugiat auctor metus. Mauris elit felis.");
  }// main

  private static void leetTranslator(String text) {
    String translatedText = "Text in leet -> ";
    for (int i = 0; i < text.length(); i++) {
      switch (text.toLowerCase().charAt(i)) {
        case 'a' -> translatedText += '4';
        case 'b' -> translatedText += "I3";
        case 'c' -> translatedText += '[';
        case 'd' -> translatedText += ')';
        case 'e' -> translatedText += '3';
        case 'f' -> translatedText += "|=";
        case 'g' -> translatedText += '&';
        case 'h' -> translatedText += '#';
        case 'i' -> translatedText += '1';
        case 'j' -> translatedText += ",_|";
        case 'k' -> translatedText += ">|";
        case 'l' -> translatedText += '1';
        case 'm' -> translatedText += "/\\/\\";
        case 'n' -> translatedText += "^/";
        case 'o' -> translatedText += '0';
        case 'p' -> translatedText += "|*";
        case 'q' -> translatedText += "(_,)";
        case 'r' -> translatedText += "I2";
        case 's' -> translatedText += '5';
        case 't' -> translatedText += '7';
        case 'u' -> translatedText += "(_)";
        case 'v' -> translatedText += "\\/";
        case 'w' -> translatedText += "\\/\\/";
        case 'x' -> translatedText += "><";
        case 'y' -> translatedText += 'j';
        case 'z' -> translatedText += '2';
        case '0' -> translatedText += 'o';
        case '1' -> translatedText += 'L';
        case '2' -> translatedText += 'R';
        case '3' -> translatedText += 'E';
        case '4' -> translatedText += 'A';
        case '5' -> translatedText += 'S';
        case '6' -> translatedText += 'b';
        case '7' -> translatedText += 'T';
        case '8' -> translatedText += 'B';
        case '9' -> translatedText += 'g';
        default -> translatedText += text.charAt(i);
      }// switch
    }
    System.out.println(translatedText);
  }// leetTranslator

}// class

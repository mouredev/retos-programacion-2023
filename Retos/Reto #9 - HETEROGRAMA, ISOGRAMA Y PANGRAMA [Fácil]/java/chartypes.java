import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Main {
  public static void main(String[] args) {
    System.out.println(Validator.heterogram("docu   menta ril,y"));
    System.out.println(Validator.pangram("Blowzy nightfrumps vexd Jack Q"));
    System.out.println(Validator.isogram("Caucasus"));

  }
}

class Validator {

  public static boolean isogram(String text) {
    Map<Character, Integer> counter = new HashMap<>();
    for (char letter : text.toLowerCase().toCharArray()) {

      if (!counter.containsKey(letter))
        counter.put(letter, 1);
      else {
        counter.put(letter, counter.get(letter) + 1);
      }

    }
    counter.remove(' ');
    Object[] values = counter.values().toArray();
    for (int i = 0; i < values.length; i++) {
      if (i == 0)
        continue;
      if (values[i] != values[i - 1])
        return false;
    }
    return true;
  }

  public static boolean pangram(String text) {
    List<Character> ALPHABET = List.of('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q',
        'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ');
    for (char letter : text.toUpperCase().toCharArray())
      if (!ALPHABET.contains(letter))
        return false;
    return true;
  }

  public static boolean heterogram(String text) {
    char[] arrayText = text.trim().toCharArray();
    for (int i = 0; i < arrayText.length; i++) {
      if (i == 0 || arrayText[i] == ' ')
        continue;
      int counter = 0;
      for (char j : arrayText)
        if (j == arrayText[i]) {
          counter++;
          if (counter > 1)
            return false;
        }
    }
    return true;
  }

}

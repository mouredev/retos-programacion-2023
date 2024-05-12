import java.util.Random;

public class chartypes {

  static final String[] ALPHABET = { "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
      "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" };
  static final String[] SYMBOLS = { "!", "@", "#", "$", "%", "&", "*", "_", "-", "?" };

  public static void main(String[] args) {
    try {
      System.out.println(passwordGenerator(8, false, false, false));
      System.out.println(passwordGenerator(16, false, true, false));
      System.out.println(passwordGenerator(12, true, true, true));
      System.out.println(passwordGenerator(6, false, false, false));
    } catch (Exception e) {
      System.out.println(e.getMessage());
    }

  }

  static StringBuilder passwordGenerator(int len, boolean mayus, boolean numbers, boolean symbols) throws Exception {

    if (len < 8 || len > 16)
      throw new Exception("length number range exceeded (must 8-16) ");

    StringBuilder password = new StringBuilder(len);
    while (password.length() < len) {
      int random = (int) (Math.random() * ALPHABET.length);
      password.append(ALPHABET[random]);

      if (mayus) {
        random = (int) (Math.random() * ALPHABET.length);
        password.append(ALPHABET[random].toUpperCase());
      }
      if (numbers){
        random = (int) (Math.random() * 10);
        password.append(random);
      }
      if (symbols) {
        random = (int) (Math.random() * SYMBOLS.length );
        password.append(SYMBOLS[random]);
      }

    }
    return password;
  }
}

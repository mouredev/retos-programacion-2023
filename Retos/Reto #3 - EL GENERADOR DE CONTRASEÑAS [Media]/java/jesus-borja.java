import java.util.Random;

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

class PassGenerator {
  private static final String NUMBERS      = "0123456789";
  private static final String LOWERLETTERS = "abcdefghijklmnopqrstuvwxyz";
  private static final String UPPERLETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  private static final String SYMBOLS      = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~";

  public static String generatePassword(int len, boolean includeUpperCaseLetters, boolean includeNumbers, boolean includeSymbols) {
    if (len < 8 || len > 16) {
      System.out.println("Error: password must be between 8 and 16 characters long.");
      System.out.printf("You chose %d characters.%n", len);
      return null;
    }

    String pass = "";
    String chars = LOWERLETTERS;
    Random random = new Random();
    
    if (includeUpperCaseLetters)
      chars += UPPERLETTERS;
    if (includeNumbers) 
      chars += NUMBERS;
    if (includeSymbols)
      chars += SYMBOLS;

    for (int i = 0; i < len; i++) {
      int rand = random.nextInt(chars.length());
      pass += chars.charAt(rand);
    }

    return pass;
  }

  public static void main(String... s) {
    String pass = generatePassword(17, true, true, false);

    System.out.printf("The pass generated is: %s%n", pass);
  }
}

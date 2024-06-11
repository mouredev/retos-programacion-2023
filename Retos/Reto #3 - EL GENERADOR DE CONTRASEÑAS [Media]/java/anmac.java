/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import java.io.Console;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class anmac {
  static int length;
  static boolean lowercase;
  static boolean uppercase;
  static boolean numbers;
  static boolean symbols;

  public static void main(String[] args) {
    if (args.length > 0) {
      setParametersFromArgs(args);
    } else {
      askForParameters();
    }

    final PasswordGenerator passwordGenerator =
        new PasswordGenerator.PasswordGeneratorBuilder()
            .setLength(length)
            .setLowercase(lowercase)
            .setUppercase(uppercase)
            .setNumbers(numbers)
            .setSymbols(symbols)
            .build();

    System.out.println(passwordGenerator.generate());
  }

  private static void askForParameters() {
    Console console = System.console();

    if (console == null) {
      System.err.println("No console found");
      System.exit(1);
    }

    length = readIntFromConsole(console, "Enter the length of the password: ", 8);
    lowercase =
        readBooleanFromConsole(console, "Do you want to include lowercase letters? [Y/n]: ", true);
    uppercase =
        readBooleanFromConsole(console, "Do you want to include uppercase letters? [y/N]: ", false);
    numbers = readBooleanFromConsole(console, "Do you want to include numbers? [y/N]: ", false);
    symbols = readBooleanFromConsole(console, "Do you want to include symbols? [y/N]: ", false);
  }

  private static int readIntFromConsole(Console console, String prompt, int defaultValue) {
    System.out.print(prompt);
    String input = console.readLine();
    if (input.trim().isEmpty()) {
      return defaultValue;
    }
    try {
      int customLength = Integer.parseInt(input);
      if (customLength < 8 || customLength > 16) {
        System.out.println("The number must be between 8 and 16 (inclusive)");
        return readIntFromConsole(console, prompt, defaultValue);
      }
      return customLength;
    } catch (NumberFormatException e) {
      System.out.println("The length must be a number");
      return readIntFromConsole(console, prompt, defaultValue);
    }
  }

  private static boolean readBooleanFromConsole(
      Console console, String prompt, boolean defaultValue) {
    System.out.print(prompt);
    String input = console.readLine();
    if (input.trim().isEmpty()) {
      return defaultValue;
    }
    return input.equals("y") || input.equals("Y");
  }

  private static void setParametersFromArgs(String[] args) {
    length = args.length > 0 ? parseIntOrDefault(args[0], 8) : 8;
    lowercase = args.length > 1 ? parseBooleanOrDefault(args[1], true) : true;
    uppercase = args.length > 2 ? parseBooleanOrDefault(args[2], false) : false;
    numbers = args.length > 3 ? parseBooleanOrDefault(args[3], false) : false;
    symbols = args.length > 4 ? parseBooleanOrDefault(args[4], false) : false;
  }

  private static int parseIntOrDefault(String value, int defaultValue) {
    try {
      return Integer.parseInt(value);
    } catch (NumberFormatException e) {
      return defaultValue;
    }
  }

  private static boolean parseBooleanOrDefault(String value, boolean defaultValue) {
    if (value.equalsIgnoreCase("true") || value.equalsIgnoreCase("false")) {
      return Boolean.parseBoolean(value);
    }
    return defaultValue;
  }
}

interface Builder {
  Builder setLength(int length);

  Builder setLowercase(boolean lowercase);

  Builder setUppercase(boolean uppercase);

  Builder setNumbers(boolean numbers);

  Builder setSymbols(boolean symbols);
}

final class PasswordGenerator {

  private static final String LOWER_CASE = "abcdefghijklmnopqrstuvwxyz";
  private static final String UPPER_CASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  private static final String NUMBERS = "0123456789";
  private static final String SYMBOLS = "!@#$%^&*()_-+={}[]|:;'<>?,./";
  private final int length;
  private final boolean lowercase;
  private final boolean uppercase;
  private final boolean numbers;
  private final boolean symbols;

  private PasswordGenerator(PasswordGeneratorBuilder builder) {
    this.length = builder.length;
    this.lowercase = builder.lowercase;
    this.uppercase = builder.uppercase;
    this.numbers = builder.numbers;
    this.symbols = builder.symbols;
  }

  static class PasswordGeneratorBuilder implements Builder {
    private int length;
    private boolean lowercase;
    private boolean uppercase;
    private boolean numbers;
    private boolean symbols;

    @Override
    public PasswordGeneratorBuilder setLength(final int length) {
      this.length = length;
      return this;
    }

    @Override
    public PasswordGeneratorBuilder setLowercase(final boolean lowercase) {
      this.lowercase = lowercase;
      return this;
    }

    @Override
    public PasswordGeneratorBuilder setUppercase(final boolean uppercase) {
      this.uppercase = uppercase;
      return this;
    }

    @Override
    public PasswordGeneratorBuilder setNumbers(final boolean numbers) {
      this.numbers = numbers;
      return this;
    }

    @Override
    public PasswordGeneratorBuilder setSymbols(final boolean symbols) {
      this.symbols = symbols;
      return this;
    }

    public PasswordGenerator build() {
      return new PasswordGenerator(this);
    }
  }

  String generate() {
    final StringBuilder password = new StringBuilder(this.length);
    final Random random = new SecureRandom();

    // Populate charList with requested char categories
    // and make sure to use at least one of each category chosen
    final List<String> charList = new ArrayList<>(4);
    if (lowercase) {
      charList.add(LOWER_CASE);
      password.append(LOWER_CASE.charAt(random.nextInt(LOWER_CASE.length())));
    }
    if (uppercase) {
      charList.add(UPPER_CASE);
      password.append(UPPER_CASE.charAt(random.nextInt(UPPER_CASE.length())));
    }
    if (numbers) {
      charList.add(NUMBERS);
      password.append(NUMBERS.charAt(random.nextInt(NUMBERS.length())));
    }
    if (symbols) {
      charList.add(SYMBOLS);
      password.append(SYMBOLS.charAt(random.nextInt(SYMBOLS.length())));
    }

    // Generate password
    for (int i = password.length(); i < this.length; i++) {
      String charCategory = charList.get(random.nextInt(charList.size()));
      password.append(charCategory.charAt(random.nextInt(charCategory.length())));
    }

    // Shuffle password to prevent predictable sequences
    List<Character> passwordChars = new ArrayList<>(this.length);
    for (char c : password.toString().toCharArray()) {
      passwordChars.add(c);
    }
    StringBuilder shuffledPassword = new StringBuilder(this.length);
    while (!passwordChars.isEmpty()) {
      int randomIndex = random.nextInt(passwordChars.size());
      shuffledPassword.append(passwordChars.remove(randomIndex));
    }

    return shuffledPassword.toString();
  }
}

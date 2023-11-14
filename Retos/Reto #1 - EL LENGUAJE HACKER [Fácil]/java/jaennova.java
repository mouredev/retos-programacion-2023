import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {

  public static final Map<Character, String> map = new HashMap<Character, String>();

  static {
    map.put('a', "4");
    map.put('b', "I3");
    map.put('c', "[");
    map.put('d', ")");
    map.put('e', "3");
    map.put('f', "|=");
    map.put('g', "&");
    map.put('h', "#");
    map.put('i', "1");
    map.put('j', ",_|");
    map.put('k', ">|");
    map.put('l', "1");
    map.put('m', "/\\/\\");
    map.put('n', "^/");
    map.put('o', "0");
    map.put('p', "|*");
    map.put('q', "(_,)");
    map.put('r', "I2");
    map.put('s', "5");
    map.put('t', "7");
    map.put('u', "(_)");
    map.put('v', "\\/");
    map.put('w', "\\/\\/");
    map.put('x', "><");
    map.put('y', "j");
    map.put('1', "L");
    map.put('2', "R");
    map.put('3', "E");
    map.put('4', "A");
    map.put('5', "S");
    map.put('6', "b");
    map.put('7', "T");
    map.put('8', "B");
    map.put('9', "g");
    map.put('0', "o");

  }

  public static String translate(String text) {
    return text.toLowerCase().chars()
        .mapToObj(c -> {
          if (map.containsKey((char) c)) {
            return map.get((char) c);
          }
          return String.valueOf((char) c);
        }).collect(Collectors.joining());
  }

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    System.out.print("Enter text: ");
    String text = sc.nextLine();

    System.out.printf("Leet: %s", translate(text));

    sc.close();
  }
}

import java.io.InputStream;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        InputStream steam = System.in;
        Scanner scanner = new Scanner(steam);
        System.out.print("Enter the text: ");
        String input = scanner.next();
        String resultConvert = convertTextToLeet(input.toUpperCase());
        System.out.print(resultConvert);
    }

    public static String convertTextToLeet(String text){
        text = text.replaceAll("A" ,"4");
        text = text.replaceAll("B", "|3");
        text = text.replaceAll("C", "[");
        text = text.replaceAll("D", "|)");
        text = text.replaceAll("E", "3");
        text = text.replaceAll("F", "ph");
        text = text.replaceAll("G", "6");
        text = text.replaceAll("H", "#");
        text = text.replaceAll("I", "1");
        text = text.replaceAll("J", "]");
        text = text.replaceAll("K", "|<");
        text = text.replaceAll("L", "1");
        text = text.replaceAll("M", "|V|");
        text = text.replaceAll("N", "И");
        text = text.replaceAll("Ñ", "И~");
        text = text.replaceAll("O", "0");
        text = text.replaceAll("P", "|>");
        text = text.replaceAll("Q", "0_");
        text = text.replaceAll("R", "|2");
        text = text.replaceAll("S", "5");
        text = text.replaceAll("T", "7");
        text = text.replaceAll("U", "(_)");
        text = text.replaceAll("V", "|/");
        text = text.replaceAll("W", "uu");
        text = text.replaceAll("X", "><");
        text = text.replaceAll("Y", "j");
        text = text.replaceAll("Z", "2");
        text = text.replaceAll(" ", " ");
        return text;
    }
}
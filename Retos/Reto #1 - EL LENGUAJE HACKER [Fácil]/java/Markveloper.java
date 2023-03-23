import java.util.HashMap;
import java.util.Scanner;

public class Markveloper {
    public static void main(String[] args) {
        HashMap<String, String> traductor = new HashMap<String, String>();
        traductor.put("A", "4");
        traductor.put("B", "(3");
        traductor.put("C", "{");
        traductor.put("D", "|>");
        traductor.put("E", "€");
        traductor.put("F", "ph");
        traductor.put("G", "gee");
        traductor.put("H", ":-:");
        traductor.put("I", "!");
        traductor.put("J", "_]");
        traductor.put("K", "1<");
        traductor.put("L", "7");
        traductor.put("M", "[V]");
        traductor.put("N", "{\\\\}");
        traductor.put("O", "oh");
        traductor.put("P", "?");
        traductor.put("Q", "0_");
        traductor.put("R", "Я");
        traductor.put("S", "ehs");
        traductor.put("T", "']['");
        traductor.put("U", "L|");
        traductor.put("V", "\\/");
        traductor.put("W", "(n)");
        traductor.put("X", "ecks");
        traductor.put("Y", "Ч");
        traductor.put("Z", "-/_");

        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce un texto cualquiera");
        String texto = sc.next().toUpperCase();

        String nuevaPalabra = "";

        for (int i = 0; i < texto.length(); i++) {
            nuevaPalabra = nuevaPalabra + traductor.get(String.valueOf(texto.charAt(i)));
        }
        System.out.println(nuevaPalabra);

    }
}

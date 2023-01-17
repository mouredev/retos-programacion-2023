import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class EspinoLeandroo {

    List<String> LETTERS = Arrays.asList("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z");
    List<String> NUMBERS = Arrays.asList("0", "1", "2", "3", "4", "5", "6", "7", "8", "9");
    List<String> SIMBOLS = Arrays.asList("!", "#", "$", "%", "&", "(", ")", "*", "+");

    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        Scanner sc = new Scanner(System.in);

        int length;
        String mayus, numbers, simbols;
        String password = "";
        List<String> allChars = new ArrayList<String>();

        System.out.print("Longitud de la contraseña [8-16]:");
        length = sc.nextInt();

        System.out.print("Incluir Mayusculas (S/N):");
        mayus = sc.next();

        System.out.print("Incluir Números (S/N):");
        numbers = sc.next();

        System.out.print("Incluir Simbolos (S/N):");
        simbols = sc.next();

        if(mayus.equalsIgnoreCase("S")){
            espinoLeandroo.LETTERS.forEach(c -> allChars.add(c.toUpperCase()));
        }
        
        espinoLeandroo.LETTERS.forEach(c -> allChars.add(c));

        if(numbers.equalsIgnoreCase("S")){
            espinoLeandroo.NUMBERS.forEach(c -> allChars.add(c));
        }

        if(simbols.equalsIgnoreCase("S")){
            espinoLeandroo.SIMBOLS.forEach(c -> allChars.add(c));
        }

        for (int i = 0; i < length; i++) {
            password += allChars.get((int) (Math.random() * allChars.size()));
        }
        
        System.out.println("Contraseña generada: " + password);
    }

}

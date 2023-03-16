import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class josepmonclus {

    List<String> LETTERS_MINUS = Arrays.asList("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z");
    List<String> LETTERS_MAYUS = Arrays.asList("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z");
    List<String> NUMBERS = Arrays.asList("1", "2", "3", "4", "5", "6", "7", "8", "9", "0" );
    List<String> SIMBOLS = Arrays.asList("!", "@", "$", "%", "&", "(", ")", "=", "?", "+", "-", "#");

    Password password = new Password();
    Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();
        

        int option;
        
        do {
            option = josepmonclus.printMenu(josepmonclus.password);

            if(option == 1) josepmonclus.password.mayus = !josepmonclus.password.mayus;
            if(option == 2) josepmonclus.password.numbers = !josepmonclus.password.numbers;
            if(option == 3) josepmonclus.password.simbols = !josepmonclus.password.simbols;
        } while (option != 0);

        josepmonclus.password.length = josepmonclus.getPasswordLength();

        System.out.println("Su password: " + josepmonclus.generatePassword(josepmonclus.password));
    }

    public int printMenu(Password password) {
        int option = -1;

        System.out.println("GENERADOR DE PASSWORDS");
        System.out.println(" 1 - Usar mayúsculas: " + (password.mayus ? "Si" : "No") );
        System.out.println(" 2 - Usar números: " + (password.numbers ? "Si" : "No"));
        System.out.println(" 3 - Usar símbolos: " + (password.simbols ? "Si" : "No"));
        System.out.println();
        System.out.println("Selecciona las opciones para generar el password, 0 para generar.");

        String line = entrada.nextLine();

        if(line.equals("1") || line.equals("2") || line.equals("3") || line.equals("0"))
            option = Integer.parseInt(line);
        
        return option;
    }

    public int getPasswordLength() {
        int length = 0;

        boolean done = false;
        do {
            System.out.println("Longitud del password [8-16]:");
            
            try{
                length = Integer.parseInt(entrada.nextLine());

                if(length >= 8 && length <= 16) done = true;
                else {
                    System.out.println("Longitud incorrecta!");
                }
            } catch(Exception e) {
                System.out.println("Longitud incorrecta!");
            }

        } while(!done);

        return length;
    }

    public String generatePassword(Password password) {
        String generated = "";

        List<String> all = new ArrayList<String>();
        all.addAll(LETTERS_MINUS);

        if(password.mayus) all.addAll(LETTERS_MAYUS);
        if(password.numbers) all.addAll(NUMBERS);
        if(password.simbols) all.addAll(SIMBOLS);

        Random random = new Random();
        for(int i = 0; i < password.length; i++) {
            generated = generated + all.get(random.nextInt(all.size()));
        }       

        return generated;
    }

    public class Password {
        private boolean mayus, numbers, simbols;
        private int length;
    }
}


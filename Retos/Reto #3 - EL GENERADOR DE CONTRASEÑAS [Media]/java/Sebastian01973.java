import java.util.*;

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
public class Sebastian01973 {
    Random random;
    private ArrayList<Character> lettersLowerCase;
    private ArrayList<Character> lettersUpperCase;
    private ArrayList<Character> symbols;

    public Sebastian01973() {
        this.random = new Random();
        this.lettersLowerCase = new ArrayList<>();
        this.lettersUpperCase = new ArrayList<>();
        this.symbols = new ArrayList<>();
        generateLettersAndNumbers();
        generateSymbols();
//        lettersUpperCase.forEach(System.out::print);
//        lettersLowerCase.forEach(System.out::print);
//        symbols.forEach(System.out::print);
    }

    private void generateSymbols() {
        char c;
        for (c = 58; c <= 64; ++c) // Valores de la tabla ascii de simbolos
            this.symbols.add(c);
        for (c = 91; c <= 96; ++c)
            this.symbols.add(c);
        for (c = 123; c <= 126; ++c)
            this.symbols.add(c);
    }

    private void generateLettersAndNumbers() {
        char c;
        for (c = 'A'; c <= 'Z'; ++c)
            this.lettersUpperCase.add(c);
        for (c = 'a'; c <= 'z'; ++c)
            this.lettersLowerCase.add(c);
    }

    private Character getRandomLetterUperCase() {
        int size = lettersUpperCase.size();
        return lettersUpperCase.get(random.nextInt(size));
    }

    private Character getRandomLetterLowerCase() {
        int size = lettersLowerCase.size();
        return lettersLowerCase.get(random.nextInt(size));
    }

    private char getRandomNumber() {
        return (char) random.nextInt(48, 57);
    }

    private char getRandomSymbol() {
        int size = symbols.size();
        return symbols.get(random.nextInt(size));
    }

    public String generatePassword(int size, boolean... parameters) {
        StringBuilder password = new StringBuilder();
        if (size >= 8 && size <= 16) {
            for (int i = 0; i < size; i++) {
                password.append(validations(parameters));
            }
            return password.toString();
        }
        return "null";
    }


    public char validations(boolean... parameters) {
        char letterRandom = 0;
        // 0: Con o Sin mayusculas
        // 1: Con o sin numeros
        // 2: Con o sin simbolos
        if (parameters[0] && parameters[1] && parameters[2]) {
            // Generar con todas las condiciones
            letterRandom = randomParameters(random.nextInt(0, 4));
        } else if (parameters[0] && parameters[1]) {
            // Genere minusculas,mayusculas y numeros
            letterRandom = randomParameters(random.nextInt(0, 3));
        } else if (parameters[0] && parameters[2]) {
            // Genere minusculas,mayusculas y simbolos
            letterRandom = randomParameters(random.nextInt(3, 6));
        } else if (parameters[1] && parameters[2]) {
            // Genere solo minusculas,numeros y simbolos
            letterRandom = randomParameters(random.nextInt(2, 5));
        } else if (parameters[0]) {
            // Genere solo minusculas y mayusculas
            letterRandom = randomParameters(random.nextInt(2));
        } else if (parameters[1]) {
            // Genere solo minusculas y numeros
            letterRandom = randomParameters(random.nextInt(2, 4));
        } else if (parameters[2]) {
            // Genere solo minusculas y simbolos
            letterRandom = randomParameters(random.nextInt(3, 4));
        } else {
            // Sin ninguna caracteristica
            letterRandom = this.getRandomLetterLowerCase();
        }
        return letterRandom;
    }

    public char randomParameters(int value) {
        switch (value) {
            case 1, 4 -> {
                return this.getRandomLetterUperCase();
            }
            case 2 -> {
                return this.getRandomNumber();
            }
            case 3 -> {
                return this.getRandomSymbol();
            }
            default -> {
                return this.getRandomLetterLowerCase();
            }
        }
    }

    public boolean getStatus(int value) {
        return value == 1;
    }

    public static void main(String[] args) {
        Sebastian01973 reto3 = new Sebastian01973();
        Scanner scanner = new Scanner(System.in);
        System.out.println("Sistema de generar contraseñas aleatorias");
        System.out.println("Generar contraseña con mayusculas 1 = si o 0 = no");
        boolean mayus = reto3.getStatus(Integer.parseInt(scanner.nextLine()));
        System.out.println("Generar contraseña con numeros 1 = si o 0 = no");
        boolean numbers = reto3.getStatus(Integer.parseInt(scanner.nextLine()));
        System.out.println("Generar contraseña con simbolos 1 = si o 0 = no");
        boolean symbols = reto3.getStatus(Integer.parseInt(scanner.nextLine()));
        String password = reto3.generatePassword(16, mayus, numbers, symbols);
        System.out.println("Su contraseña es la siguiente:");
        System.out.println(password);
    }
}

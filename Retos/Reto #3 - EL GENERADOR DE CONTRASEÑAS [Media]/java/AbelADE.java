import java.util.ArrayList;
import java.util.Scanner;

/**
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros: -
 * Longitud: Entre 8 y 16. - Con o sin letras mayúsculas. - Con o sin n. -
 * Con o sin símbolos. (Pudiendo combinar todos estos parámetros entre ellos)
 *
 * @author abel
 */
public class PasswordGenerator {

    /**
     * Longitud máxima de la contraseña.
     */
    public final static int MAX_LENGHT = 16;

    /**
     * Longitud mínima de la contraseña.
     */
    public final static int MIN_LENGHT = 8;

    /**
     * El tamaño de la contraseña.
     */
    private int lenght;

    /**
     * Si la contraseña contiene mayúsculas.
     */
    private boolean containsCapitalLetters;

    /**
     * Si la contraseña contiene números.
     */
    private boolean containsNumbers;

    /**
     * si la contraseña contiene símbolos.
     */
    private boolean containsSimbols;

    /**
     * Si la contraseña contiene letras. Se establece en el constructor.
     */
    private final boolean containsLetters;

    /**
     * ArrayList con la configuración del usuario.
     */
    private final ArrayList<String> configuratorPassword;

    /**
     * Devuelve el tamaño de la contraseña.
     * @return el tamaño de la contraseña.
     */
    public int getLenght() {
        return lenght;
    }

    /**
     * Sobrescribe el tamaño de la contraseña.
     * @param lenght el tamaño de la contraseña.
     */
    public void setLenght(int lenght) {
        this.lenght = lenght;
    }

    /**
     * Devuelve si la contraseña contiene mayúsculas.
     * @return si la contraseña contiene mayúsculas.
     */
    public boolean isContainsCapitalLetters() {
        return containsCapitalLetters;
    }

    /**
     * Sobrescribe si la contraseña contiene mayúsculas.
     * @param containsCapitalLetters si la contraseña contiene mayúsculas.
     */
    public void setContainsCapitalLetters(boolean containsCapitalLetters) {
        this.containsCapitalLetters = containsCapitalLetters;
    }

    /**
     * Devuelve si la contraseña contiene números.
     * @return si la contraseña contiene números.
     */
    public boolean isContainsNumbers() {
        return containsNumbers;
    }

    /**
     * Sobrescribe si la contraseña contiene números.
     * @param containsNumbers si la contraseña contiene números.
     */
    public void setContainsNumbers(boolean containsNumbers) {
        this.containsNumbers = containsNumbers;
    }

    /**
     * Devuelve si la contraseña contiene símbolos.
     * @return si la contraseña contiene símbolos.
     */
    public boolean isContainsSimbols() {
        return containsSimbols;
    }

    /**
     * Sobrescribe si la contraseña contiene símbolos.
     * @param containsSimbols si la contraseña contiene símbolos.
     */
    public void setContainsSimbols(boolean containsSimbols) {
        this.containsSimbols = containsSimbols;
    }

    /**
     * Constructor de la clase.
     */
    public PasswordGenerator() {
        this.containsLetters = true;

        configuratorPassword = new ArrayList<>();

        if (containsCapitalLetters) {
            configuratorPassword.add("containsCapitalLetters");
        }

        if (containsNumbers) {
            configuratorPassword.add("containsNumbers");
        }

        if (containsSimbols) {
            configuratorPassword.add("containsSimbols");
        }

        if (containsLetters) {
            configuratorPassword.add("containsLetters");
        }
    }

    /**
     * Genera una contraseña.
     * @return una contraseña.
     */
    public String GeneratePasword() {
        String pasword = "";

            for (int i = 0; i < lenght; i++) {

                int randomCharacterType = new java.util.Random().nextInt(configuratorPassword.size());

                String characterType = configuratorPassword.get(randomCharacterType);

                switch (characterType) {
                    case "containsCapitalLetters":
                        char capitalLetter = (char) (new java.util.Random().nextInt(25) + 65);
                        pasword += capitalLetter;
                        break;
                    case "containsLetters":
                        char letter = (char) (new java.util.Random().nextInt(25) + 97);
                        pasword += letter;
                        break;
                    case "containsNumbers":
                        int number = new java.util.Random().nextInt(10);
                        pasword += number;
                        break;
                    case "containsSimbols":
                        String[] simbols = new String[]{"@", "~", "$", "#", "&", "/", "?", "¿", "¡", "|", "!"};
                        int index = new java.util.Random().nextInt(simbols.length);
                        pasword += simbols[index];
                        break;
                }
            }
        return pasword;
    }

    /**
     * Pide al usuario como quiere su contraseña.
     * @param scan un objeto Scanner.
     */
    public void userConfigurePasword(Scanner scan) {
        
        do {
            System.out.print("Dime el número de caracteres de la contraseña a generar:");
            lenght = scan.nextInt();
            
            if (lenght < MIN_LENGHT || lenght > MAX_LENGHT) {
                System.err.println("El tamaño de la contraseña debe estar entre 8 y 16");
            }
        } while (lenght < MIN_LENGHT || lenght > MAX_LENGHT);

        System.out.println();
        
        System.out.println("¿La contraseña tendrá Mayúsculas? (true/false)");
        containsCapitalLetters = scan.nextBoolean();

        System.out.println();
         
        System.out.println("¿La contraseña tendrá números? (true/false)");
        containsCapitalLetters = scan.nextBoolean();

         System.out.println();
        
        System.out.println("¿La contraseña tendrá símbolos? (true/false)");
        containsCapitalLetters = scan.nextBoolean();
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        boolean notExit;

        System.out.println("Bienvenido al generador de contraseñas!!");
        System.out.println("----------------------------------------------------");
        System.out.println("");

        do {
            PasswordGenerator passwordGenerator = new PasswordGenerator();

            passwordGenerator.userConfigurePasword(scan);
            
            System.out.println("----------------------------------------------------");
            System.out.print("Su contraseña es: ");
            System.out.println(passwordGenerator.GeneratePasword());
            System.out.println("----------------------------------------------------");

            System.out.println("¿Quieres generar una nueva contraseña? (true/false)");
            notExit = scan.nextBoolean();

        } while (notExit);
    }

}


import java.util.Random;
import java.util.Scanner;

public class RoyMartinez3103 {

    private static final String LETRAS_MIN = "abcdefghijklmnopqrstuvwxyz";
    private static final String LETRAS_MAY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final String NUMEROS = "0123456789";
    private static final String SIMBOLOS = "!@#$%^&*()_-+=<>?";

    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        int longitud = 0;
        String numeros, mayus, simbolos;

        // Pedimos la longitud de la contraseña
        do {
            System.out.println("Ingresa la longitud del password (8-16): ");
            if (scan.hasNextInt()) {
                longitud = scan.nextInt();
                scan.nextLine(); // Limpiar el buffer
            } else {
                System.out.println("Por favor ingresa un número válido.");
                scan.nextLine(); // Limpiar la entrada inválida
            }
        } while (longitud < 8 || longitud > 16);

        // Preguntamos por los tipos de caracteres a incluir
        System.out.println("¿Deseas incluir números? S/N");
        numeros = scan.nextLine().toUpperCase();

        System.out.println("¿Deseas incluir mayúsculas? S/N");
        mayus = scan.nextLine().toUpperCase();

        System.out.println("¿Deseas incluir símbolos? S/N");
        simbolos = scan.nextLine().toUpperCase();

        // Generar y mostrar la contraseña
        String password = generarPassword(longitud, numeros.equals("S"), mayus.equals("S"), simbolos.equals("S"));
        System.out.println("Contraseña generada: " + password);
    }

    public static String generarPassword(int longitud, boolean incluirNumeros, boolean incluirMayusculas, boolean incluirSimbolos) {
        StringBuilder caracteres = new StringBuilder(LETRAS_MIN);  // Incluye siempre letras minúsculas
        if (incluirMayusculas) {
            caracteres.append(LETRAS_MAY);
        }
        if (incluirNumeros) {
            caracteres.append(NUMEROS);
        }
        if (incluirSimbolos) {
            caracteres.append(SIMBOLOS);
        }

        Random random = new Random();
        StringBuilder password = new StringBuilder(longitud);

        for (int i = 0; i < longitud; i++) {
            int indiceAleatorio = random.nextInt(caracteres.length());
            password.append(caracteres.charAt(indiceAleatorio));
        }

        return password.toString();
    }
}

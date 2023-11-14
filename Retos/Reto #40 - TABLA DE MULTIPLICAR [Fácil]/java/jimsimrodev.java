
import java.util.Scanner;

/**
 *
 * @author jhoan
 */
public class Multiplicar {

    public static void main(String[] args) {

        Scanner leer = new Scanner(System.in);

        System.out.print("Digita El Número Para Mostrar Su Tabla De Multiplicar ->");
        int numero = leer.nextInt();

        System.out.println("=================================");
        System.out.println("| Tabla de multiplicar del: " + numero + "|");

        for (int i = 1; i <= 10; i++) {
            System.out.println(numero + "*" + i + "=" + numero * i);
        }
        System.out.println("================");

    }

}

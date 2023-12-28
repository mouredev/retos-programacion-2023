import java.util.Scanner;

public class miguelex {
    public static int seed = (int) System.currentTimeMillis();

    public static void main(String[] args) {
        int contador;
        int a = (int) System.currentTimeMillis();
        int m = (int) System.currentTimeMillis() * 1000;

        System.out.println("¿Cuantos numeros quieres generar?: ");
        Scanner leer = new Scanner(System.in);
        contador = leer.nextInt();
        leer.close();

        for (int i = 0; i < contador; i++) {
            try {
                System.out.println("Numero " + (i + 1) + ": " + RandomNumber(a, m) % 100);
                Thread.sleep(3000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private static int RandomNumber(int a, int m) {
        int q = (int) a / m;
        int r = m % a;

        seed = a * (seed % q) - r * (int) (seed / q);

        if (seed < 0) {
            seed += m;
        }

        return Math.abs(seed);
    }
}
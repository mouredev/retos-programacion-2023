import java.util.Scanner;

class alvaruncio {
    public static void main(String[] args) {
        // Tabla multiplicar
        Scanner scanner = new Scanner(System.in); // Creacion del scanner
        System.out.print("Escriba el numero cuya tabla de multiplicacion quieres hacer: ");
        int numberTableOfMultiplication = scanner.nextInt(); // El usuario introduce el numero del que quiere la tabla de multiplicar
        System.out.printf("Tabla de multiplicacion de %d\n", numberTableOfMultiplication);
        for (int i = 1; i < 11; i++) {
            int result = i * numberTableOfMultiplication;
            System.out.printf("%d x %d = %d\n", numberTableOfMultiplication, i, result );
        }
    }
}
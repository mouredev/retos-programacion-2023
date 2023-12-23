import java.util.InputMismatchException;
import java.util.Scanner;

/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */
public class AgusWorld {

	public static void main(String[] args) {
		Scanner src = new Scanner(System.in);

		Double inputNumber = null;

		do {
			System.out.print("Please, write a number: ");
			try {
				inputNumber = src.nextDouble();
			} catch (Exception e) {
				if (e instanceof InputMismatchException)
					System.out.println("That's not a number!");
				else
					System.out.println("Unexpected error" + e);

				src.next();
			}
		} while (inputNumber == null);

		for (int i = 1; i <= 10; i++) {
			System.out.printf(inputNumber.intValue() == inputNumber ? "%.0f x %d = %.0f\n" : "%.2f x %d = %.2f\n",
					inputNumber, i, i * inputNumber);
		}

		src.close();
	}

}
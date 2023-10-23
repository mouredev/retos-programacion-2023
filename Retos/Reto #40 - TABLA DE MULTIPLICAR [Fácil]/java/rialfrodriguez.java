package retosprogramacion;

import java.util.Scanner;

public class rialfrodriguez {

	public static void main(String[] args) {	
		
		int number = askNumber();
		calculateTable (number);
	}
	
	public static int askNumber() {
		Scanner sc = new Scanner(System.in);
		int number;
		do {
		    System.out.println("Por favor ingrese un numero positivo: ");
		    while (!sc.hasNextInt()) {
		        System.out.println("No es un numero!");
		        sc.next();
		    }
		    number = sc.nextInt();
		} while (number <= 0);
		return number;
	}
	
	public static void calculateTable(int number) {

		System.out.println("Tabla de multiplicar de: " + number);
		for(int i = 1; i <= 10; i++) {
			String cal = String.format("%d x %d = %d", number, i, (number * i));
			System.out.println(cal);
		}
	}
}

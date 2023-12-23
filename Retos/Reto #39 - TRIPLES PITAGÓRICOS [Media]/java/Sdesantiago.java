/*
	Crea una función que encuentre todos los triples pitagóricos
	(ternas) menores o iguales a un número dado.
		- Debes buscar información sobre qué es un triple pitagórico.
		- La función únicamente recibe el número máximo que puede
	aparecer en el triple.
		- Ejemplo: Los triples menores o iguales a 10 están
	formados por (3, 4, 5) y (6, 8, 10).

*	Triple pitagórico -> a² = b² + c²
*/

import java.util.Scanner;

public class Sdesantiago {
	public static void main(String[] args) {
		int	entrada;

		Scanner scan = new Scanner(System.in);
		System.out.print("RETO 39 BY MOUREDEV\n- Ingresa un número positivo para comenzar: ");
		entrada = scan.nextInt();
		scan.close();
		if (entrada<=0) {
			System.err.print("ERROR: El valor ingresado no es válido. Finalizando ejecución del programa.");
			return;
		}
		for	(int a=entrada;a>0;a--){
			for (int b=a-1;b>0;b--){
				for (int c=b;c>0;c--){
					if (Math.pow(a,2)==Math.pow(b,2)+Math.pow(c,2))
						System.out.println("("+a+","+b+","+c+")");
				}
			}
		}
	}
}

/*
 * Reto #0: EL FAMOSO "FIZZ BUZZ"
 * Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23
 * 
 * Enunciado:
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

public class Main {
	
	public static void main(String[] args) {
		for(int i=1; i<=100; i++) {
			System.out.println(fizzbuzz(i));
		}
	}
	
	public static String fizzbuzz(int number) {
		String str = Integer.toString(number);
		
		if(number%3==0 && number%5==0)
			str = "fizzbuzz";
		else if(number%3==0)
			str = "fizz";
		else if(number%5==0)
			str = "buzz";
		
		return str;
	}
	
}

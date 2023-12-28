/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

class Main {
	public static void main(String[] args) {
		System.out.println(checkNumber(37));
		System.out.println(checkNumber(73));
		System.out.println(checkNumber(5));
		System.out.println(checkNumber(2));
		System.out.println(checkNumber(8));
		System.out.println(checkNumber(46));
		System.out.println(checkNumber(13));
  }

	static boolean isPrime(int number) {
		// comprobar si el número es par y así descartarlos todos con excepción del 2
		if (number < 2 || (number % 2 == 0 && number != 2)) {
			return false;
		}
    
		// Se revisa el modulo empezando en 3 y sin tener en cuenta los pares
		for (int i = 3; i <= (number / 2); i += 2) {
			if (number % i == 0) {
				return false;
			}
		}
  
		return true;
	}

    static boolean fibonnaci(int number) 
		// Se utliza la identidad de Binet para figurar si es de la secuencia de fibonnaci
		long binet = 5 * number * number;
		if ((int) Math.sqrt(binet + 4) == Math.sqrt(binet + 4)) {
				return true;
		}
		if ((int) Math.sqrt(binet - 4) == Math.sqrt(binet - 4)) {
			return true;
		}
		return false;
  }

	static String checkNumber(int number) {
		// Crea el mensaje sobre las condiciones descritas
		String message = "El número " + number;
		message += isPrime(number) ? "" : " no";
		message += " es primo,";
		message += fibonnaci(number) ? "" : " no";
		message += " es fibonnaci y";
		message += number % 2 != 0 ? " es impar" : " es par";
		return message;
  }
}
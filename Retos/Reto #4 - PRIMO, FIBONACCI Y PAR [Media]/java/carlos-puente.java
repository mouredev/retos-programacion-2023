/*
@Author
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

import static java.lang.Math.*;

import java.util.Scanner;

public class Reto4 {

	public static void main(final String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = -1;

		do {
			System.out.println("Please enter a positive int number: ");
			try {
				num = sc.nextInt();
				if(num<0){
					System.out.println("Oooops! Remember my friend..., a positive int number: )");
				}
			} catch (final Exception ex) {
				System.out.println("Ooops! I think you choose an invalid number, please try again!");
				num = -1;
				sc = new Scanner(System.in);
			}
		} while (num < 0);
		sc.close();
		System.out.println(generateChallengeText(num));
	}

	/**
	 * Generates the text required by the challenge
	 *
	 * @param num
	 * 		a positive number
	 * @return a text with the result
	 */
	private static String generateChallengeText(final int num) {
		return num +
				(isPrime(num) ? " es primo, " : " no es primo, ") +
				(isFibonacci(num) ? "fibonacci " : "no es fibonacci ") +
				(isPair(num) ? "y es par. " : "y es impar.");
	}

	/**
	 * Checks if a number is pair.
	 *
	 * @param num
	 * 		a positive number
	 * @return true if pair, false if not.
	 */
	public static boolean isPair(final int num) {
		return num % 2 == 0;
	}

	/**
	 * Binet's formula provides a proof that a positive integer x is a Fibonacci number if and only if at least one of
	 * 5x^{2}+4 or 5x^{2}-4 is a perfect square
	 *
	 * @param num
	 * 		a positive number
	 * @return true if number is a Fibonacci number, false otherwise.
	 */
	public static boolean isFibonacci(final int num) {
		return isSquare(5 * num * num + 4) || isSquare(5 * num * num - 4);
	}

	/**
	 * Checks if a number is square, 4 is square (integer result of sqrt(4) is 2 and 2*2 is 4).
	 * sqrt(3) is not square (integer result of sqrt(3) is 1 and 1 * 1 is not 3).
	 *
	 * @param num
	 * 		a positive number
	 * @return true if number is a square number, false otherwise.
	 */
	public static boolean isSquare(final int num) {
		final int result = Double.valueOf(sqrt(num)).intValue();
		return result * result == num;
	}

	/**
	 * Checks if a number is prime.
	 *
	 * @param num
	 * 		a positive number
	 * @return
	 */
	public static boolean isPrime(final int num) {

		//First static checks
		if (num < 2) {
			return false;
		}
		else if (num == 2 || num == 3) {
			return true;
		} 
		else if (num % 2 == 0 || num % 3 == 0) {
			return false;
		}
		//The other cases
		for (int i = 2; i <= Math.sqrt(num); i++) {
			if (num % i == 0) {
				return false;
			}
		}
		return true;

	}

}


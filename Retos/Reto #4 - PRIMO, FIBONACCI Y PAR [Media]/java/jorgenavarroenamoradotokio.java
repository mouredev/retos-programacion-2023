package com.retos.ej04;

import java.util.stream.IntStream;

public class jorgenavarroenamoradotokio {

	/*
	 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par. 
	 * Ejemplos: 
	 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par" 
	 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
	 */

	public static void main(String[] args) {

		int num1 = 2;
		int num2 = 21;
		
		System.out.println("El numero " + num1 + " es Primo " + esNumeroPrimo(num1) + " es fibonacci " + esFibonacci(num1) + " es par " + esPar(num1));
		System.out.println("El numero " + num2 + " es Primo " + esNumeroPrimo(num2) + " es fibonacci " + esFibonacci(num2) + " es par " + esPar(num2));
	}

	private static boolean esNumeroPrimo(int numero) {
		if (numero <= 1) {
			return false;
		}

		// Utilizamos la función noneMatch para verificar si no hay divisores entre 2 y  la raíz cuadrada del número
		return IntStream.rangeClosed(2, (int) Math.sqrt(numero)).noneMatch(i -> numero % i == 0);
	}

	private static boolean esFibonacci(int numero) {
		if (numero < 0)
			return false;

		int a = 0;
		int b = 1;

		while (b < numero) {
			int siguiente = a + b;
			a = b;
			b = siguiente;

			if (b == numero) {
				return true;
			}
		}
		return b == numero;
	}
	
	private static boolean esPar(int numero) {
		return numero % 2 == 0;
	}
}

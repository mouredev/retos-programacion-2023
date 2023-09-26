package com.retos.ej21;

import java.util.stream.IntStream;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		int rangoMaximo = 14; // Cambia este valor al rango máximo deseado

		System.out.println("Pares de números primos gemelos en el rango hasta " + rangoMaximo + ":");
		IntStream.rangeClosed(2, rangoMaximo - 2).filter(number -> isPrime(number) && isPrime(number + 2))
				.forEach(number -> System.out.println("(" + number + ", " + (number + 2) + ")"));
	}

	public static boolean isPrime(int number) {
		if (number <= 1) {
			return false;
		}

		if (number <= 3) {
			return true;
		}

		if (number % 2 == 0 || number % 3 == 0) {
			return false;
		}

		return IntStream.rangeClosed(5, (int) Math.sqrt(number))
				.allMatch(i -> number % i != 0 && number % (i + 2) != 0);
	}
}

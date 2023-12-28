package Reto9;

import java.util.Scanner;


public class CarlosCarrilloP {
	/*
	 * Crea 3 funciones, cada una encargada de detectar si una cadena de texto es un
	 * heterograma, un isograma o un pangrama.
	 */

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); 
		String cadena;
		//Introduce la cadena
		System.out.println("Ingrese la cadena a analizar:");
		cadena = sc.nextLine();
		analizarCadena(cadena);
		sc.close();
	}

	public static void analizarCadena(String cadena) {
		esHeterograma(cadena);
		esIsograma(cadena);
		esPangrama(cadena);
	}

	/**
	 * Metodo esHeterograma comprueba que la palabra no contiene ninguna letra
	 * repetida
	 */
	public static void esHeterograma(String cadena) {

		for (int i = 0; i < cadena.length(); i++) {
			char letra = cadena.charAt(i);
			if (cadena.indexOf(letra) != i) {
				System.out.println("La cadena no es un heterograma.");
				return;
			}
		}
		System.out.println("La cadena es un heterograma.");
	}

	/**
	 * Metodo esIsograma que no hay letras repetidas, pero también incluye la opción
	 * de tener espacios y signos de puntuación
	 */

	public static void esIsograma(String cadena) {
		cadena = cadena.toLowerCase().replaceAll("[^a-zA-Z]", ""); // eliminar espacios y signos de puntuación
		for (int i = 0; i < cadena.length(); i++) {
			char letra = cadena.charAt(i);
			if (cadena.indexOf(letra) != i) {
				System.out.println("La cadena no es un isograma.");
				return;
			}
		}
		System.out.println("La cadena es un isograma.");
	}

	/**
	 * Metodo esPangrama que es una frase que contiene todas las letras del
	 * alfabeto.
	 */
	public static void esPangrama(String cadena) {
		cadena = cadena.toLowerCase();
		boolean[] letras = new boolean[26]; //Abecedario contiene 26 letras.
		int indice;
		for (int i = 0; i < cadena.length(); i++) {
			char letra = cadena.charAt(i);
			if (letra >= 'a' && letra <= 'z') {
				indice = letra - 'a';
				letras[indice] = true;
			}
		}
		for (int i = 0; i < letras.length; i++) {
			if (!letras[i]) {
				System.out.println("La cadena no es un pangrama.");
				return;
			}
		}
		System.out.println("La cadena es un pangrama.");
	}

}

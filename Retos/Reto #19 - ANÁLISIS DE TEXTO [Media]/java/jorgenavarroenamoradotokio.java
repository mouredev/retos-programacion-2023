package com.retos.ej19;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		String texto = "Nos encontramos en un periodo de guerra civil. "
				+ "Las naves espaciales rebeldes, atacando desde una base oculta, "
				+ "han logrado su primera victoria contra el malvado Imperio Galáctico";		
		
		System.out.println(obtenerNumeroPalabras(texto));
		System.out.println(obtenerMediaLongitudPalabras(texto));
		System.out.println(obtenerNumeroOraciones(texto));
		System.out.println(obtenerPalabraMayorLongitud(texto));
	}

	private static long obtenerNumeroPalabras(String texto) {
		return Stream.of(texto.split("\\s+")).filter(palabra -> !palabra.isEmpty()).count();
	}

	private static int obtenerMediaLongitudPalabras(String texto) {
		List<String> palabras = Arrays.stream(texto.split("\\s+")).filter(palabra -> !palabra.isEmpty())
				.collect(Collectors.toList());

		int longitudTotal = palabras.stream().mapToInt(String::length).sum();

		return palabras.isEmpty() ? 0 : (int) longitudTotal / palabras.size();
	}

	private static long obtenerNumeroOraciones(String texto) {
		return Stream.of(texto.split("\\.")).filter(palabra -> !palabra.isEmpty()).count();
	}

	private static String obtenerPalabraMayorLongitud(String texto) {
		List<String> palabras = Arrays.stream(texto.split("\\s+")).filter(palabra -> !palabra.isEmpty())
				.collect(Collectors.toList());

		Optional<String> max = palabras.stream()
				.max((palabra1, palabra2) -> Integer.compare(palabra1.length(), palabra2.length()));

		return max.orElse("");
	}
}

package com.retos.ej09;

import java.text.Normalizer;
import java.util.Collection;
import java.util.Locale;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {

		boolean heterograma = isHeterogram("yuxtaponer");
		System.out.println(heterograma ? "es un heterograma": "no es un heterograma");
		
		boolean isograma = isIsogram("acondicionar ");
		System.out.println(isograma ? "es un isograma": "no es un isograma");
		
		boolean pangram = isPangram("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú");
		System.out.println(pangram ? "es un pangrama": "no es un pangrama");
		
	}

	public static Map<Character, Long> contarLetras(String cadena) {
		 cadena = Normalizer.normalize(cadena, Normalizer.Form.NFD)
	                .replaceAll("\\p{InCombiningDiacriticalMarks}+", "")
	                .replaceAll("[.¡!¿?\"']", "")
	                .replaceAll("\\s+", "")
	                .toLowerCase(Locale.ROOT);
		
		
		return cadena.toLowerCase().replaceAll("\\+s", "").chars()
				.mapToObj(c -> (char) c)
				.filter(Character::isLetter)
				.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
	}

	private static boolean isHeterogram(String texto) {
		Collection<Long> contadores = contarLetras(texto).values();
		for (Long contador : contadores) {
			if (contador > 1)
				return false;
		}
		return true;
	}

	private static boolean isIsogram(String texto) {
		Collection<Long> contadores = contarLetras(texto).values();
		int contadorExterno = 0;
		for (Long contador : contadores) {
			if (contadorExterno == 0)
				contadorExterno = contador.intValue();
			if (contador != contador.intValue())
				return false;
		}
		return true;
	}

	public static boolean isPangram(String texto) {
		return contarLetras(texto).keySet().size() == 26;
	}

}

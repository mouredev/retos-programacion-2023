package com.retos.ej15;

import java.text.Normalizer;
import java.util.HashMap;
import java.util.Locale;
import java.util.Map;

public class jorgenavarroenamoradotokio {

	private static final Map<String, String> basic_alphabet = new HashMap<>();

	static {
		basic_alphabet.put("a", "aurek");
		basic_alphabet.put("b", "besh");
		basic_alphabet.put("c", "cresh");
		basic_alphabet.put("d", "dorn");
		basic_alphabet.put("e", "esk");
		basic_alphabet.put("f", "forn");
		basic_alphabet.put("g", "grek");
		basic_alphabet.put("h", "herf");
		basic_alphabet.put("i", "isk");
		basic_alphabet.put("j", "jenth");
		basic_alphabet.put("k", "krill");
		basic_alphabet.put("l", "leth");
		basic_alphabet.put("m", "merm");
		basic_alphabet.put("n", "nern");
		basic_alphabet.put("o", "osk");
		basic_alphabet.put("p", "peth");
		basic_alphabet.put("q", "qek");
		basic_alphabet.put("r", "resh");
		basic_alphabet.put("s", "senth");
		basic_alphabet.put("t", "trill");
		basic_alphabet.put("u", "usk");
		basic_alphabet.put("v", "vev");
		basic_alphabet.put("w", "wesk");
		basic_alphabet.put("x", "xesh");
		basic_alphabet.put("y", "yirt");
		basic_alphabet.put("z", "zerek");
		basic_alphabet.put("ae", "enth");
		basic_alphabet.put("eo", "onith");
		basic_alphabet.put("kh", "krenth");
		basic_alphabet.put("ng", "nen");
		basic_alphabet.put("oo", "orenth");
		basic_alphabet.put("sh", "sen");
		basic_alphabet.put("th", "thesh");
	}

	public static void main(String[] args) {
		String frase = "Qué te ha parecido el reto? A mí me ha gustado mucho! Mañana sigue practicando.";
		String aurebesh = idiomaToStarWars(frase); 
		
		System.out.println(aurebesh);
		System.out.println(starWarsToIdioma(aurebesh));
		
		String frase2 = "The Mouredev";
		String aurebesh2 = idiomaToStarWars(frase2); 
		
		System.out.println(aurebesh2);
		System.out.println(starWarsToIdioma(aurebesh2));
		
	}

	private static String idiomaToStarWars(String palabra) {
		if (palabra == null || palabra.isEmpty())
			return "";

		palabra = Normalizer.normalize(palabra, Normalizer.Form.NFD)
				.replaceAll("\\p{InCombiningDiacriticalMarks}+", "")
				.replaceAll("[.¡!¿?\"']", "")
				.toLowerCase(Locale.ROOT);

		StringBuilder sb = new StringBuilder();
		String[] division = palabra.split(" ");

		for (String grupo : division) {
			char[] caracteres = grupo.toLowerCase().toCharArray();
			for (char c : caracteres) {
				String traduccion = basic_alphabet.get(String.valueOf(c));
				if (traduccion != null)
					sb.append(traduccion);
			}
			sb.append(" ");
		}
		return sb.toString();
	}

	private static String starWarsToIdioma(String palabra) {
		if (palabra == null || palabra.isEmpty())
			return "";

		Map<String, String> aurebeshAlphabet = new HashMap<>();
		for (Map.Entry<String, String> entry : basic_alphabet.entrySet()) {
			aurebeshAlphabet.put(entry.getValue(), entry.getKey());
		}

		StringBuilder translatedText = new StringBuilder(palabra);
		for (Map.Entry<String, String> entry : aurebeshAlphabet.entrySet()) {
			String key = entry.getKey();
			String value = entry.getValue();
			translatedText = new StringBuilder(translatedText.toString().replace(key, value));
		}

		return translatedText.toString();
	}
}

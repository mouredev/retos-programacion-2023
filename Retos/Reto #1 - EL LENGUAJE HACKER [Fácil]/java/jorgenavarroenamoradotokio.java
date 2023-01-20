package com.casa.retos.java.ejercicio02;

import java.util.Map;

public class ejercicio2 {

	public static void main(String[] args) {
		Map<String, String> diccionario = Map.ofEntries(Map.entry("A", "4"), Map.entry("b", "I3"), Map.entry("c", "["),
				Map.entry("D", ")"), Map.entry("E", "3"), Map.entry("F", "|="), Map.entry("G", "&"),
				Map.entry("H", "#"), Map.entry("I", "1"), Map.entry("J", "_|"), Map.entry("K", ">|"),
				Map.entry("L", "1"), Map.entry("M", "/\\/\\"), Map.entry("N", "^/"), Map.entry("O", "0"),
				Map.entry("P", "|*"), Map.entry("Q", "(,)"), Map.entry("R", "I2"), Map.entry("S", "5"),
				Map.entry("T", "7"), Map.entry("U", "(_)"), Map.entry("V", "\\/"), Map.entry("W", "\\/\\/"),
				Map.entry("X", "><"), Map.entry("Y", "j"), Map.entry("Z", "2"), Map.entry("1", "L"),
				Map.entry("2", "R"), Map.entry("3", "E"), Map.entry("4", "A"), Map.entry("5", "S"), Map.entry("6", "b"),
				Map.entry("7", "T"), Map.entry("8", "B"), Map.entry("9", "g"), Map.entry("0", "o"));

		String cadenaOriginal = "Leet";
		String resultado = "";
		char[] caracteres = cadenaOriginal.toCharArray();
		for (char caracter : caracteres) {
			String traduccion = diccionario.get(String.valueOf(caracter).toUpperCase());
			resultado += traduccion != null && !traduccion.isEmpty() ? traduccion : "";
		}

		System.out.println(resultado);
	}
}
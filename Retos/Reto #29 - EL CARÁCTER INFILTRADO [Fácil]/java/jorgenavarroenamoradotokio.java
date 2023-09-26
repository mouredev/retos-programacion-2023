package com.retos.ej29;

import java.util.ArrayList;
import java.util.List;

public class jorgenavarroenamoradotokio {
	
	public static void main(String[] args) {
		System.out.println(infiltratedCharacters("Me llamo mouredev", "Me llemo mouredov"));
		System.out.println(infiltratedCharacters("Me llamo.Brais Moure", "Me llamo brais moure"));
		System.out.println(infiltratedCharacters("Me llamo.Brais Moure", "Me llamo brais moure "));
		System.out.println(infiltratedCharacters("", ""));
	}

	private static List<Character> infiltratedCharacters(String firstText, String secondText) {
		List<Character> characters = new ArrayList<>();

		if (firstText.length() == secondText.length()) {
			for (int index = 0; index < firstText.length(); index++) {
				if (firstText.charAt(index) != secondText.charAt(index)) {
					characters.add(secondText.charAt(index));
				}
			}
		}

		return characters;
	}
}

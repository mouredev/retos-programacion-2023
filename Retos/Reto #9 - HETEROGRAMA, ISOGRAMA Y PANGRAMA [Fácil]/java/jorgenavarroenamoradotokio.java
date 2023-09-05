package com.retos.ej09;

import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		System.out.println(isHeterogram("hiperblanduzcos"));
		System.out.println(isHeterogram("hiperblanduzcós    !!w"));
		System.out.println(isIsogram("anna"));
		System.out.println(isPangram("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"));
	}
	
	
	private static boolean isHeterogram(String palabra) {
		return Stream.of(palabra.split(""))
				.map(String::toLowerCase)
				.filter(letra -> !letra.equals(" "))
				.collect(Collectors.groupingBy(letra -> letra, Collectors.counting()))
				.values()
				.stream().allMatch(cantidad -> cantidad == 1);
	}

	private static boolean isIsogram(String palabra) {
		return Stream.of(palabra.split(""))
				.map(String::toLowerCase)
				.filter(letra -> !letra.equals(" "))
				.collect(Collectors.groupingBy(letra -> letra, Collectors.counting()))
				.values()
				.stream().allMatch(cantidad -> cantidad == 1);
	}
	
	public static boolean isPangram(String frase) {
        String fraseLimpia = frase.toLowerCase().replaceAll("\\s+", "");
        
        Set<Character> letrasUnicas = fraseLimpia.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.toSet());
        
        return letrasUnicas.size() == 26;
    }

}

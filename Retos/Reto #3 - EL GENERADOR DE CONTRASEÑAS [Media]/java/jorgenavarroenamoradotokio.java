package com.retos.ej03;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {

		int longitudPassword = 15;
		boolean mayus = true;
		boolean numeros = true;
		boolean simbolos = true;

		// Registramos el codigo ascii de los caracteres del alfabeto en minusculas
		List<Integer> caracteres = IntStream.rangeClosed(97, 122).boxed().collect(Collectors.toList());

		// Registramos el codigo ascii de los caracteres del alfabeto en mayusculas
		if (mayus)
			caracteres.addAll(IntStream.rangeClosed(65, 90).boxed().collect(Collectors.toList()));
		
		// Registramos el codigo ascii de los numeros
		if (numeros) {
			caracteres.addAll(IntStream.rangeClosed(48, 57).boxed().collect(Collectors.toList()));
	    }
		
		// Registramos el codigo ascii de los caracteres 
		if (simbolos) {
			caracteres.addAll(IntStream.rangeClosed(33, 47).boxed().collect(Collectors.toList()));
			caracteres.addAll(IntStream.rangeClosed(58, 64).boxed().collect(Collectors.toList()));
			caracteres.addAll(IntStream.rangeClosed(91, 96).boxed().collect(Collectors.toList()));
		}
		
		// Ajustamos la longitud de la password
		if (longitudPassword < 8)
			longitudPassword = 8;
		else if (longitudPassword > 16)
			longitudPassword = 16;

		
		String password = "";
		while (password.length() < longitudPassword) {
			int caracterSeleccionado = (int) (Math.random() *caracteres.size()) + 1;
			password += (char) (int) caracteres.get(caracterSeleccionado);
		}
		
		System.out.println(password);
	}
}

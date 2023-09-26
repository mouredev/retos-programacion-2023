package com.retos.ej11;

import java.util.Arrays;
import java.util.Map;
import java.util.stream.Collectors;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {

		String url = "https://www.example.com/?param1=valor1&param2=valor2&param3=valor3";
		Map<String, String> parametros = obtenerParametros(url);

		// Imprimir los parámetros
		parametros.forEach((clave, valor) -> {
			System.out.println(clave + ": " + valor);
		});

	}

	public static Map<String, String> obtenerParametros(String url) {
		// Obtener la parte de la URL que contiene los parámetros
		int indice = url.indexOf("?");
		if (indice == -1) {
			return null; // No hay parámetros en la URL
		}
		String parametrosStr = url.substring(indice + 1);

		// Dividir los parámetros en pares clave=valor
		return Arrays.stream(parametrosStr.split("&")).map(parametro -> parametro.split("="))
				.collect(Collectors.toMap(arr -> arr[0], arr -> arr.length > 1 ? arr[1] : ""));
	}
}

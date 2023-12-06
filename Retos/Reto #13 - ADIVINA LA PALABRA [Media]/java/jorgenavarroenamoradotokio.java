package com.retos.ej13;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class jorgenavarroenamoradotokio {

	public static void main(String[] args) {
		String palabra = "mouredev"; 
		Map<String, Integer> mapLetrasOcultasPosicion = ocultarPalabra(palabra, 0);
		
		
		String palabraJuego = palabra;
		for (Integer posicion : mapLetrasOcultasPosicion.values()) {
			palabraJuego = cambiarCaracterPalabra(palabraJuego, '_', posicion);
		}
		
		System.out.println("La palabra que debe de adivinar es: ");
		
		Scanner sc = new Scanner(System.in);
		int numeroIntentos = 3;
		boolean ganar = false;
		while (numeroIntentos > 0 && !ganar) {
			System.out.println(palabraJuego);
			System.out.println("Le quedan " + numeroIntentos + " intentos");
			System.out.println("Inserte la letra o palabra que crea que puede ser");
			String opcion = sc.next();
			
			if (opcion.length() == palabra.length() && opcion.equalsIgnoreCase(palabra)) {
				ganar = true;
			} else if (opcion.length() > 1 && !opcion.equalsIgnoreCase(palabra)) {
				numeroIntentos--;
			} else if (opcion.length() == 1 && !mapLetrasOcultasPosicion.containsKey(opcion)) {
				numeroIntentos--;
			} else {
				char c = opcion.charAt(0);
				palabraJuego = cambiarCaracterPalabra(palabraJuego, c, mapLetrasOcultasPosicion.get(opcion));
				ganar = !palabraJuego.contains("_") ? true : false;
			}
		}
		sc.close();
		System.out.println(ganar ? "Ha ganado" : "Ha perdido");
	}
	
	private static Map<String, Integer> ocultarPalabra(String palabra, int porcentajeOcultar) {
		Map<String, Integer> mapLetraPosicion = new HashMap<>();
		
		double porcentaje = 0;
		if (porcentajeOcultar == 0 || porcentajeOcultar > 60) {
			porcentaje = 0.60;
		} else {
			porcentaje = (double)(porcentajeOcultar / 100);
		}
		int numeroLetrasOcultar = (int) (palabra.length() * porcentaje);
		
		int contadorLetrasOcultas = 0;
		while (contadorLetrasOcultas <= numeroLetrasOcultar) {
			int posicionOcultar = (int)(Math.random() * (palabra.length()-1)) + 1;
			mapLetraPosicion.put(String.valueOf(palabra.charAt(posicionOcultar)), posicionOcultar);
			contadorLetrasOcultas++;
		}
		return mapLetraPosicion;
	}
	
	private static String cambiarCaracterPalabra(String palabra, char caracter, int posicion) {
		char[] caracteres = palabra.toCharArray();
        caracteres[posicion] = caracter;
        return new String(caracteres);
	}
}

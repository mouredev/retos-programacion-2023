package reto;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.atomic.AtomicBoolean;

/*
 * Crea un juego interactivo por terminal en el que tendrás que adivinar 
 * el resultado de diferentes
 * operaciones matemáticas aleatorias (suma, resta, multiplicación 
 * o división de dos números enteros).
 * - Tendrás 3 segundos para responder correctamente.
 * - El juego finaliza si no se logra responder en ese tiempo.
 * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
 * - Cada 5 aciertos debes aumentar en uno el posible número de cifras 
 *   de la operación (cada vez en un operando):
 *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
 *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
 *   - Preguntas 11 a 15: XX operación YY
 *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
 *   ...
 */


// SOLUCIÓN IMPLEMENTADA CON THREADS

public class Adivinanzas {

	// Constante tiempo en milisegundos
	public static final int MILISEGUNDOS = 3000;

	public static int contadorAciertos = 0;
	public static Random randomIndice = new Random();
	public static List<String> operaciones = new ArrayList<String>();
	public static final Scanner scanner = new Scanner(System.in);
	public static AtomicBoolean continuar = new AtomicBoolean(true);
	public static int incrementadorX = 1;
	public static int incrementadorY = 1;
	public static int turno = 0;

	public static void main(String[] args) {

		Collections.addAll(operaciones, "+", "-", "*", "/"); // Añadir al array las operaciones que vamos a necesitar

		while (continuar.get()) {
			juegoAdivinanzas(); // Mientras la variable continuar sea true, el juego sigue
		}
	}

	// Función para resolver la operación generada, e imprimirla
	public static int resolver(String operacion, int num1, int num2) {

		int resultadoOperacion = 0;
		
		// Switch para traducir las operaciones
		switch (operacion) {
		case "+":
			resultadoOperacion = num1 + num2; break;
		case "-":
			resultadoOperacion = num1 - num2; break;
		case "*":
			resultadoOperacion = num1 * num2; break;
		case "/":
			if (num2 == 0) {
				num2++; // Evitamos la división entre 0
			}
			resultadoOperacion = num1 / num2; break;
		}
		
		System.out.println(num1 + " " + operacion + " " + num2 + ": ");

		return resultadoOperacion;
	}

	// Método principal del juego
	public static void juegoAdivinanzas() {
		int resultado;
		Random random = new Random();
		
		try {
			
			// Hilo temporizador. Duerme durante 3 segundos, si no se responde finaliza el programa
			Thread hiloTiempo = new Thread(() -> {
				try {
					Thread.sleep(MILISEGUNDOS);
					System.out.println("\n¡Tiempo agotado!");
					System.out.println("Juego finalizado. Número de aciertos: " + contadorAciertos);
					continuar.set(false);
					scanner.close();
					System.exit(0);
				} catch (InterruptedException e) {}
			});
			
			// Iniciar el hilo temporizador
			hiloTiempo.start();

			try {
				// generamos una operación a resolver y comparamos su resultado con la entrada
				resultado = resolver(operaciones.get(randomIndice.nextInt(operaciones.size())),
						random.nextInt(10 * incrementadorX), random.nextInt(10 * incrementadorY));
				int resultadoUser = Integer.parseInt(scanner.next());
				if (resultado == resultadoUser) {
					contadorAciertos++;
					if (contadorAciertos % 5 == 0) {
						// Variable turno, para incrementar el número de cifras en el operando correspondiente
						turno = (turno + 1) % 4;
						switch (turno) {
						case 0: 
							incrementadorY *= 10; break;
						case 1: 
							incrementadorX *= 10; break;
						case 2: 
							incrementadorY *= 10; break;
						case 3: 
							incrementadorX *= 10; break;
						}
					}
				}
			} finally {
				// Si se introduce un resultado, el hilo finaliza y se reinicia para el próximo
				hiloTiempo.interrupt();
			}
		} catch (NumberFormatException e) {
			// Si no se introduce un entero válido, finaliza
			System.err.println("Número no válido. " + e.getMessage());
			System.out.println("Juego finalizado. Número de aciertos: " + contadorAciertos);
			scanner.close();
			System.exit(0);
		}
	}
}

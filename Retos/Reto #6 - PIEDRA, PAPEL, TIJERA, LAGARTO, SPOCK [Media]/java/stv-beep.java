package pptls;

import java.util.Random;
import java.util.Scanner;

/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

/** He recuperado uno de los primeros programas que hice y lo he adaptado. */

public class Main {

	public static int NUM_PARTIDAS = 3;
	public static boolean running = true;
	public static int partidas = 0;

	public static void Menu() {
		System.out.println(
				"Escribe: \"1\" para piedra, \"2\" para papel, \"3\" para tijeras, \"4\" para lagarto o \"5\" para spock.	Y \"6\" para salir del programa: ");
	}
	
	public static int contadorJugador = 0;
	public static int contadorCompu = 0;
	public static int contadorEmpates = 0;
	
	public static String[] opciones = {"piedra", "papel", "tijera", "lagarto", "spock"};

	public static int cpuPPTLS() {
		int random = new Random().nextInt(opciones.length);
		return random;
	}

	public static void piedra(int rand) {
		if (opciones[rand] == "tijera" || opciones[rand] == "lagarto") {
			contadorJugador++;
			System.out.println(opciones[0]+" vs "+opciones[rand]+"! HAS GANADO!\n");
		} else if (opciones[rand] == "piedra") {
			contadorEmpates++;
			System.out.println(opciones[0]+" vs "+opciones[rand]+"! EMPATE!\n");
		} else {
			contadorCompu++;
			System.out.println(opciones[0]+" vs "+opciones[rand]+"! HAS PERDIDO!\n");
		}
		result();
	}
	
	public static void papel(int rand) {
		if (opciones[rand] == "piedra" || opciones[rand] == "spock") {
			contadorJugador++;
			System.out.println(opciones[1]+" vs "+opciones[rand]+"! HAS GANADO!\n");
		} else if (opciones[rand] == "papel") {
			contadorEmpates++;
			System.out.println(opciones[1]+" vs "+opciones[rand]+"! EMPATE!\n");
		} else {
			contadorCompu++;
			System.out.println(opciones[1]+" vs "+opciones[rand]+"! HAS PERDIDO!\n");
		}
		result();
	}
	
	public static void tijera(int rand) {
		if (opciones[rand] == "papel" || opciones[rand] == "lagarto") {
			contadorJugador++;
			System.out.println(opciones[2]+" vs "+opciones[rand]+"! HAS GANADO!\n");
		} else if (opciones[rand] == "tijera") {
			contadorEmpates++;
			System.out.println(opciones[2]+" vs "+opciones[rand]+"! EMPATE!\n");
		} else {
			contadorCompu++;
			System.out.println(opciones[2]+" vs "+opciones[rand]+"! HAS PERDIDO!\n");
		}
		result();
	}
	
	public static void lagarto(int rand) {
		if (opciones[rand] == "papel" || opciones[rand] == "spock") {
			contadorJugador++;
			System.out.println(opciones[3]+" vs "+opciones[rand]+"! HAS GANADO!\n");
		} else if (opciones[rand] == "lagarto") {
			contadorEmpates++;
			System.out.println(opciones[3]+" vs "+opciones[rand]+"! EMPATE!\n");
		} else {
			contadorCompu++;
			System.out.println(opciones[3]+" vs "+opciones[rand]+"! HAS PERDIDO!\n");
		}
		result();
	}
	
	public static void spock(int rand) {
		if (opciones[rand] == "piedra" || opciones[rand] == "tijera") {
			contadorJugador++;
			System.out.println(opciones[4]+" vs "+opciones[rand]+"! HAS GANADO!\n");
		} else if (opciones[rand] == "spock") {
			contadorEmpates++;
			System.out.println(opciones[4]+" vs "+opciones[rand]+"! EMPATE!\n");
		} else {
			contadorCompu++;
			System.out.println(opciones[4]+" vs "+opciones[rand]+"! HAS PERDIDO!\n");
		}
		result();
	}
	
	public static void result() {
		if (partidas == NUM_PARTIDAS) {
		    System.out.println("Resultado final:\n"
				+ "Player 1: "+contadorJugador+" | CPU: "+contadorCompu+" | Empates: "+contadorEmpates+"\n");
		
            if (contadorJugador > contadorCompu) {
                System.out.println("---HAS GANADO!---");
            } else if (contadorJugador < contadorCompu) {
                System.out.println("---HAS PERDIDO!---");
            } else {
                System.out.println("---EMPATE TOTAL!---");
            }
		}
	}

	public static void main(String[] args) {
		System.out.println(
				"Bienvenido a un 1 pa 1 sin camisa contra la 'aleatoriedad' de la CPU a un PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK. Suerte!\n");
		Scanner sc = new Scanner(System.in);

		while (partidas < NUM_PARTIDAS && running) {
			partidas++;
			Menu();

			int opt = sc.nextInt();
			int rndm = cpuPPTLS();
			switch (opt) {
			case 1:
				piedra(rndm);
				break;
			case 2:
				papel(rndm);
				break;
			case 3:
				tijera(rndm);
				break;
			case 4:
				lagarto(rndm);
				break;
			case 5:
				spock(rndm);
				break;
			default:
				running = false;
				System.out.println("ciao");
                sc.close();
			}
		}
	}
}

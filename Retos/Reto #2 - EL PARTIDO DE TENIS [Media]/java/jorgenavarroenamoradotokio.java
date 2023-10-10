package com.retos.ej02;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

public class jorgenavarroenamoradotokio {

	private static final Map<Integer, String> MAP_PUNTUACIONES_PARTIDA = new HashMap<>();
	private static final String DEUCE = "Deuce";
	private static final String VENTAJA = "Ventaja";

	static {
		MAP_PUNTUACIONES_PARTIDA.put(0, "Love");
		MAP_PUNTUACIONES_PARTIDA.put(1, "15");
		MAP_PUNTUACIONES_PARTIDA.put(2, "30");
		MAP_PUNTUACIONES_PARTIDA.put(3, "40");
	}
	
	// Clase interna encargada de almacenar la informacion de un jugador
	public class Jugador{
		
		private String nombre;
		private int puntuacion;
		private boolean advance;
		private boolean ganador;
		
		public Jugador(String nombre) {
			this.nombre = nombre;
			this.puntuacion = 0;
			this.advance = false;
			this.ganador = false;
		}
		
		public void addPunto() {
			puntuacion += 1;
			if (advance && puntuacion == 5)
				ganador = true;
			else if (!advance && puntuacion == 4)
				ganador = true;
		}

		public String getNombre() {
			return nombre;
		}

		public void setNombre(String nombre) {
			this.nombre = nombre;
		}

		public int getPuntuacion() {
			return puntuacion;
		}

		public boolean isAdvance() {
			return advance;
		}

		public void setAdvance(boolean advance) {
			this.advance = advance;
		}

		public boolean isGanador() {
			return ganador;
		}
	}
	
	// Clase interna encargada de la logica del partido
	public class Partido {
		private Jugador p1;
		private Jugador p2;
		
		public void inscribirJugadores(Jugador p1, Jugador p2) {
			this.p1 = p1;
			this.p2 = p2;
		}
		
		public void enfrentamiento() {
			do {
				int numP1 = (int) (Math.random() * 5) + 1;;
				int numP2 = (int) (Math.random() * 5) + 1;;

				if (numP1 > numP2)
					p1.addPunto();
				else
					p2.addPunto();

				if (isDeuce())
					System.out.println(DEUCE);
				else if (isAdvantagePlayer(p1, p2) || isAdvantagePlayer(p2, p1))
					System.out.println(VENTAJA);
				else if (!p1.isGanador() && !p2.isGanador())
					System.out.println(MAP_PUNTUACIONES_PARTIDA.get(p1.getPuntuacion()) + " - " + MAP_PUNTUACIONES_PARTIDA.get(p2.getPuntuacion()));
			} while (!p1.isGanador() && !p2.isGanador());

			System.out.println("Ha ganado el jugador " + (p1.isGanador() ? p1.getNombre() : p2.getNombre()));
		}
		
		private boolean isDeuce() {
			return p1.getPuntuacion() >= 4 && p1.getPuntuacion() == p2.getPuntuacion();
		}

		private boolean isAdvantagePlayer(Jugador consulta, Jugador rival) {
			boolean advance = (consulta.getPuntuacion() > 4) && (consulta.getPuntuacion() - rival.getPuntuacion() == 1);
			consulta.setAdvance(advance);
			return advance;
		}
		
	}

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		System.out.println("Desea lanzar una prueba: \n 1: dinamica \n 2: fija");
		String opcion = sc.nextLine();
		sc.close();
		
		if ("1".equals(opcion)) {
			jorgenavarroenamoradotokio tenis = new jorgenavarroenamoradotokio();
			jorgenavarroenamoradotokio.Jugador p1 = tenis.new Jugador("P1");
			jorgenavarroenamoradotokio.Jugador p2 = tenis.new Jugador("P2");

			jorgenavarroenamoradotokio.Partido partido = tenis.new Partido();
			partido.inscribirJugadores(p1, p2);
			partido.enfrentamiento();

		} else if ("2".endsWith(opcion)) {
			String[] jugadas = { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" };
			int puntosGanadosP1 = 0, puntosGanadosP2 = 0;
			
			for (String jugada : jugadas) {
				if ("P1".equals(jugada))
					puntosGanadosP1 += 1;
				else if ("P2".equals(jugada))
					puntosGanadosP2 += 1;

				if (puntosGanadosP1 == 3 && (puntosGanadosP1 == puntosGanadosP2))
					System.out.println(DEUCE);
				else if ((puntosGanadosP1 == 4 && puntosGanadosP2 == 3) || (puntosGanadosP2 == 4 && puntosGanadosP1 == 3))
					System.out.println(VENTAJA);
				else if ((puntosGanadosP1 == 4 || puntosGanadosP1 == 5) && puntosGanadosP2 == 3)
					System.out.println("Ha ganado el P1");
				else if ((puntosGanadosP2 == 4 || puntosGanadosP2 == 5) && puntosGanadosP1 == 3)
					System.out.println("Ha ganado el P2");
				else
					System.out.println(MAP_PUNTUACIONES_PARTIDA.get(puntosGanadosP1) + " - " + MAP_PUNTUACIONES_PARTIDA.get(puntosGanadosP2));
			}
		}
	}
}

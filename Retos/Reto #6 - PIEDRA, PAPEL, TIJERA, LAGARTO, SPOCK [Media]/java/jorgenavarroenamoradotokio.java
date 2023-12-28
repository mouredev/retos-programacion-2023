package com.retos.ej06;

public class jorgenavarroenamoradotokio {

	private static final String PIEDRA = "PIEDRA";
	private static final String PAPEL = "PAPEL";
	private static final String TIJERA = "TIJERA";
	private static final String LAGARTO = "LAGARTO";
	private static final String SPOCK = "SPOCK";

	public static void main(String[] args) {

		String elementoJugador1 = PIEDRA, elementoJugador2 = PIEDRA;

		int resultado = switch (elementoJugador1) {
			case PIEDRA -> isGanaRoca(elementoJugador2);
			case PAPEL -> isGanaPapel(elementoJugador2);
			case TIJERA -> isGanaTijeras(elementoJugador2);
			case LAGARTO -> isGanaLagarto(elementoJugador2);
			case SPOCK -> isGanaSpock(elementoJugador2);
			default -> throw new IllegalArgumentException("Unexpected value: " + elementoJugador1);
		};

		if (resultado < 0)
			System.out.println("El jugador 2 ha ganado");
		else if (resultado > 0)
			System.out.println("El jugador 1 ha ganado");
		else
			System.out.println("Empate");
	}

	private static int isGanaRoca(String opcionCombatir) {
		if (LAGARTO.equals(opcionCombatir) || TIJERA.equals(opcionCombatir))
			return 1;
		if (PIEDRA.equals(opcionCombatir))
			return 0;
		return -1;
	}

	private static int isGanaPapel(String opcionCombatir) {
		if (PIEDRA.equals(opcionCombatir) || SPOCK.equals(opcionCombatir))
			return 1;
		if (PAPEL.equals(opcionCombatir))
			return 0;
		return -1;
	}

	private static int isGanaTijeras(String opcionCombatir) {
		if (LAGARTO.equals(opcionCombatir) || PAPEL.equals(opcionCombatir))
			return 1;
		if (TIJERA.equals(opcionCombatir))
			return 0;
		return -1;
	}

	private static int isGanaLagarto(String opcionCombatir) {
		if (SPOCK.equals(opcionCombatir) || PAPEL.equals(opcionCombatir))
			return 1;
		if (LAGARTO.equals(opcionCombatir))
			return 0;
		return -1;
	}

	private static int isGanaSpock(String opcionCombatir) {
		if (LAGARTO.equals(opcionCombatir) || PAPEL.equals(opcionCombatir))
			return 1;
		if (SPOCK.equals(opcionCombatir))
			return 0;
		return -1;
	}
}

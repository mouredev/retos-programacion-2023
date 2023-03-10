import java.util.Arrays;
import java.util.List;

/**
 * Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
 * Dificultad: Media | Publicaci贸n: 06/02/23 | Correcci贸n: 13/02/23
 * 
 * Crea un programa que calcule quien gana m谩s partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La funci贸n recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "馃椏" (piedra), "馃搫" (papel),
 *   "鉁傦笍" (tijera), "馃" (lagarto) o "馃枛" (spock).
 * - Ejemplo. Entrada: [("馃椏","鉁傦笍"), ("鉁傦笍","馃椏"), ("馃搫","鉁傦笍")]. Resultado: "Player 2".
 * - Debes buscar informaci贸n sobre c贸mo se juega con estas 5 posibilidades.
 * 
 * Informaci贸n del juego:
 * https://bigbangtheory.fandom.com/es/wiki/Piedra,_Papel,_Tijera,_Lagarto_o_Spock
 * 
 * "Reglas:
 *   Tijeras cortan papel
 *   Papel cubre piedra
 *   Piedra aplasta lagarto
 *   Lagarto envenena Spock
 *   Spock destruye tijeras
 *   Tijeras decapitan lagarto
 *   Lagarto come papel
 *   Papel desaprueba Spock
 *   Spock vaporiza piedra
 *   Piedra aplasta tijeras"
 */
public class aronracso
{
    public static final String PIEDRA = "馃椏";
    public static final String PAPEL = "馃搫";
    public static final String TIJERAS = "鉁傦笍";
    public static final String LAGARTO = "馃";
    public static final String SPOCK = "馃枛";

    public static final String JUGADOR1 = "Player 1";
    public static final String JUGADOR2 = "Player 2";
    public static final String EMPATE = "Tie";

    public static class Jugada
    {
        public final String jugador1;
        public final String jugador2;
        public Jugada(String jugador1, String jugador2)
        {
            this.jugador1 = jugador1;
            this.jugador2 = jugador2;
        }
    }

    public static void main(String[] args)
    {
        List<Jugada> jugadas = Arrays.asList(
            new Jugada("馃椏","鉁傦笍"), new Jugada("鉁傦笍","馃椏"), new Jugada("馃搫","鉁傦笍")
        );
        String resultado = procesaEntrada(jugadas);
        System.out.println(resultado);
    }

    public static String procesaEntrada(List<Jugada> jugadas)
    {
        int puntosJ1 = 0;
        int puntosJ2 = 0;

        for (Jugada jugada : jugadas)
        {
            if(ganaElemento(jugada.jugador1, jugada.jugador2))
                puntosJ1 += 1;
            else 
                puntosJ2 += 1;
        }

        if(puntosJ1 > puntosJ2)
            return JUGADOR1;
        else if(puntosJ2 > puntosJ1)
            return JUGADOR2;
        else
            return EMPATE;
    }

    public static boolean ganaElemento(String elemento1, String elemento2)
    {
        switch(elemento1)
        {
            case PIEDRA:
                return elemento2.equals(LAGARTO) || elemento2.equals(SPOCK);
            case PAPEL:
                return elemento2.equals(PIEDRA) || elemento2.equals(SPOCK);
            case TIJERAS:
                return elemento2.equals(PAPEL) || elemento2.equals(LAGARTO);
            case LAGARTO:
                return elemento2.equals(PAPEL) || elemento2.equals(SPOCK);
            case SPOCK:
                return elemento2.equals(TIJERAS) || elemento2.equals(PIEDRA);
            default:
                return false;
        }
    }
}

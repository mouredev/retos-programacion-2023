import java.util.Arrays;
import java.util.List;

/**
 * Reto #6: Piedra, Papel, Tijera, Lagarto, Spock
 * Dificultad: Media | Publicación: 06/02/23 | Corrección: 13/02/23
 * 
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 * 
 * Información del juego:
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
    public static final String PIEDRA = "🗿";
    public static final String PAPEL = "📄";
    public static final String TIJERAS = "✂️";
    public static final String LAGARTO = "🦎";
    public static final String SPOCK = "🖖";

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
            new Jugada("🗿","✂️"), new Jugada("✂️","🗿"), new Jugada("📄","✂️")
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

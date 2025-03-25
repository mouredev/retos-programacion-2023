
import java.util.ArrayList;
import java.util.Scanner;

/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️ " (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 *
 * Rules:
 * - Tijeras cortan Papel. ✂️  > 📄
 * - Papel cubre Piedra. 📄 > 🗿
 * - Piedra tritura Lagarto. 🗿 > 🦎
 * - Lagarto envenena Spock. 🦎 > 🖖
 * - Spock rompe Tijeras. 🖖 > ✂️
 * - Tijeras decapitan Lagarto. ✂️ > 🦎
 * - Lagarto come Papel. 🦎 > 📄
 * - Papel desautoriza Spock. 📄 > 🖖
 * - Spock vaporiza Piedra. 🖖 > 🗿
 * - Piedra tritura Tijeras. 🗿 > ✂️
 *
 */
public class RoyMartinez3103 {

    public enum Opciones {
        PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
    }

    public static String[] IngresarJuego() {
        String[] juego;
        Scanner scan = new Scanner(System.in);
        String cadena;

        System.out.println("==== PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK ===");
        System.out.println("Ingresa el juego, separado por una coma cada movimiento: ");
        System.out.println("\t\tEJEMPLO: piedra,papel");
        cadena = scan.nextLine().toUpperCase();
        juego = cadena.split(",");

        if (juego.length % 2 != 0) {
            System.out.println("ERROR, la cantidad de movimientos debe ser par.\n");
            IngresarJuego();
        }

        if (juego.length == 2) {
            System.out.println("EL juego debe tener más de 1 jugada.\n");
            IngresarJuego();
        }

        return juego;
    }

    public static void Jugar(String[] juego) {
        Integer ptsP1 = 0, ptsP2 = 0;
        ArrayList<String> jugadaP1 = new ArrayList<>();
        ArrayList<String> jugadaP2 = new ArrayList<>();

        for (int j = 0; j < juego.length; j++) {
            if (j % 2 == 0) {
                jugadaP1.add(juego[j]);
            } else {
                jugadaP2.add(juego[j]);
            }
        }

        for (int i = 0; i < jugadaP1.size(); i++) {
            if (jugadaP1.get(i).equals(jugadaP2.get(i))) {
                continue;
            }
            if (jugadaP1.get(i).equals(Opciones.PIEDRA.toString())) {
                if (jugadaP2.get(i).equals(Opciones.LAGARTO.toString()) || jugadaP2.get(i).equals(Opciones.TIJERA.toString())) {
                    ptsP1++;
                } else {
                    ptsP2++;
                }
            }
            if (jugadaP1.get(i).equals(Opciones.PAPEL.toString())) {
                if (jugadaP2.get(i).equals(Opciones.PIEDRA.toString()) || jugadaP2.get(i).equals(Opciones.SPOCK.toString())) {
                    ptsP1++;
                } else {
                    ptsP2++;
                }
            }
            if (jugadaP1.get(i).equals(Opciones.TIJERA.toString())) {
                if (jugadaP2.get(i).equals(Opciones.PAPEL.toString()) || jugadaP2.get(i).equals(Opciones.LAGARTO.toString())) {
                    ptsP1++;
                } else {
                    ptsP2++;
                }
            }
            if (jugadaP1.get(i).equals(Opciones.LAGARTO.toString())) {
                if (jugadaP2.get(i).equals(Opciones.SPOCK.toString()) || jugadaP2.get(i).equals(Opciones.PAPEL.toString())) {
                    ptsP1++;
                } else {
                    ptsP2++;
                }
            }
            if (jugadaP1.get(i).equals(Opciones.SPOCK.toString())) {
                if (jugadaP2.get(i).equals(Opciones.PIEDRA.toString()) || jugadaP2.get(i).equals(Opciones.LAGARTO.toString())) {
                    ptsP1++;
                } else {
                    ptsP2++;
                }
            }
        }

        if (ptsP1 > ptsP2) {
            System.out.println("Player 1");
        } else if (ptsP2 > ptsP1) {
            System.out.println("Player 2");
        } else {
            System.out.println("Tie");
        }
    }

    public static void main(String args[]) {
        String[] juego;
        juego = IngresarJuego();
        Jugar(juego);

    }
}

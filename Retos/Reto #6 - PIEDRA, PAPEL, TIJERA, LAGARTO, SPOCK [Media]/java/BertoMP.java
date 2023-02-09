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
public class PPTLS {
    public static void main(String[] args) {
        Scanner scEntrada = new Scanner(System.in);

        String[] opciones = {"piedra", "papel", "tijeras", "lagarto", "spock"};
        int intContadorJ1 = 0;
        int intContadorJ2 = 0;
        String strOpcionJ1 = "";
        String strOpcionJ2 = "";
        int intOpcion;
        do {
            for (int intCont = 0; intCont < 2; intCont++) {
                System.out.println(intCont == 0 ? "J1" : "J2");
                System.out.println("""
                        Elige una opción:
                            1. Piedra.
                            2. Papel.
                            3. Tijera.
                            4. Lagarto.
                            5. Spock.""");
                System.out.print("Opción: ");
                intOpcion = scEntrada.nextInt();
                while (intOpcion < 1 || intOpcion > 5) {
                    System.out.println("La opción no vale. Vuelve a intentarlo.");
                    System.out.print("Opción: ");
                    intOpcion = scEntrada.nextInt();
                }
                if (intCont == 0) {
                    strOpcionJ1 = opciones[intOpcion - 1];
                } else {
                    strOpcionJ2 = opciones[intOpcion - 1];
                }
                System.out.println();
            }
            if (strOpcionJ1.equals(strOpcionJ2)) {
                System.out.println("Empate");
            } else if (strOpcionJ1.equals("piedra")) {
                if (strOpcionJ2.equals("tijeras") || strOpcionJ2.equals("lagarto")) {
                    System.out.println("Gana el J1.");
                    intContadorJ1++;
                } else {
                    System.out.println("Gana el J2.");
                    intContadorJ2++;
                }
            } else if (strOpcionJ1.equals("papel")) {
                if (strOpcionJ2.equals("piedra") || strOpcionJ2.equals("spock")) {
                    System.out.println("Gana el J1.");
                    intContadorJ1++;
                } else {
                    System.out.println("Gana el J2.");
                    intContadorJ2++;
                }
            } else if (strOpcionJ1.equals("tijeras")) {
                if (strOpcionJ2.equals("papel") || strOpcionJ2.equals("lagarto")) {
                    System.out.println("Gana el J1.");
                    intContadorJ1++;
                } else {
                    System.out.println("Gana el J2.");
                    intContadorJ2++;
                }
            } else if (strOpcionJ1.equals("lagarto")){
                if (strOpcionJ2.equals("papel") || strOpcionJ2.equals("spock")) {
                    System.out.println("Gana el J1.");
                    intContadorJ1++;
                } else {
                    System.out.println("Gana el J2.");
                    intContadorJ2++;
                }
            } else if (strOpcionJ1.equals("spock")) {
                if (strOpcionJ2.equals("tijeras") || strOpcionJ2.equals("piedra")) {
                    System.out.println("Gana el J1.");
                    intContadorJ1++;
                } else {
                    System.out.println("Gana el J2.");
                    intContadorJ2++;
                }
            }
            System.out.println();
            System.out.println("Marcador -> J1: " + intContadorJ1 + " - J2: " + intContadorJ2);
            System.out.print("¿Otra partida? (1: Sí / 2: No) ");
            intOpcion = scEntrada.nextInt();
            System.out.println();
        } while(intOpcion != 2);
        scEntrada.close();
    }
}

import java.util.Scanner;
public class sergiolpzgmz {
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
    public static void menu_juego(String jugador, int puntosJ1, int puntosJ2){
        System.out.println("Puntos: J1 = "+puntosJ1+" | "+"J2 = "+puntosJ2);
        System.out.println(jugador+" introduce una opción: " );
        System.out.println("1) Piedra");
        System.out.println("2) Papel");
        System.out.println("3) Tijera");
        System.out.println("4) Lagarto");
        System.out.println("5) Spock");
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce número de jugadas por partida: ");
        int numJugadas = sc.nextInt();

        boolean errorDatos = false;

        int puntosJ1 = 0;
        int puntosJ2 = 0;

        for(int i = 0; i < numJugadas; i++){

            menu_juego("Jugador1",puntosJ1,puntosJ2);
            int opcionJuador1 = sc.nextInt();
            menu_juego("Jugador2",puntosJ1,puntosJ2);
            int opcionJuador2 = sc.nextInt();

            if((opcionJuador2 > 1 && opcionJuador2 < 5) && (opcionJuador1 > 1 && opcionJuador1 < 5) && opcionJuador2 == opcionJuador1 ) System.out.println("Jugada empatada");

            if((opcionJuador2 > 1 && opcionJuador2 < 5) || (opcionJuador1 > 1 && opcionJuador1 < 5)) {
                errorDatos=true;
                System.out.println("Error en los datos introducidos");
                break;
            }

            switch (opcionJuador1){
                case 1:
                    if(opcionJuador2==2 || opcionJuador2==5) puntosJ2++;
                    else if (opcionJuador2==3 || opcionJuador2==4) puntosJ1++;
                    break;
                case 2:
                    if (opcionJuador2==3 || opcionJuador2==4) puntosJ2++;
                    else if (opcionJuador2==1 || opcionJuador2==5) puntosJ1++;
                    break;
                case 3:
                    if (opcionJuador2==1 || opcionJuador2==5) puntosJ2++;
                    else if (opcionJuador2==2 || opcionJuador2==4) puntosJ1++;
                    break;
                case 4:
                    if (opcionJuador2==1 || opcionJuador2==3) puntosJ2++;
                    else if (opcionJuador2==5 || opcionJuador2==2) puntosJ1++;
                    break;
                case 5:
                    if (opcionJuador2==2 || opcionJuador2==4) puntosJ2++;
                    else if (opcionJuador2==1 || opcionJuador2==3) puntosJ1++;
                    break;
            }
        }
        if(errorDatos == false){
            if(puntosJ1>puntosJ2) {
                System.out.println("Ganador: PLayer 1");
                System.out.println("Puntos: J1 = "+puntosJ1+" | "+"J2 = "+puntosJ2);
            }
            else if(puntosJ1<puntosJ2) {
                System.out.println("Ganador: PLayer 2");
                System.out.println("Puntos: J1 = "+puntosJ1+" | "+"J2 = "+puntosJ2);
            }
            else {
                System.out.println("Tie");
                System.out.println("Puntos: J1 = "+puntosJ1+" | "+"J2 = "+puntosJ2);
            }
        }
        sc.close();
    }
}

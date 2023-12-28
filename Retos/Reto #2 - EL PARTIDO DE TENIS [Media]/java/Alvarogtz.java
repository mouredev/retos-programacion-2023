import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Alvarogtz {

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

    private final String player1Name = "P1";
    private final String player2Name = "P2";

    private Player player1 = new Player(player1Name);
    private Player player2 = new Player(player2Name);

    private static boolean matchWinner = false;

    private Player[] players = {player1,player2};

    public static void main(String[] args){

        Alvarogtz start = new Alvarogtz();
        Scanner entrada = new Scanner(System.in);
        String result = "";
        System.out.println("Comienza el partido entre P1 y P2 ");

        do {
            result = start.getEntrada(entrada);
            System.out.println(result);
        }while(!matchWinner);

        System.out.println("Fin del partido");
    }

    public String getEntrada(Scanner entrada) {
        String result = "";

        try{
            result = entrada.nextLine().toUpperCase();

            if(!result.equalsIgnoreCase(player1Name) && !result.equalsIgnoreCase(player2Name)) {
                result = "Opcion no valida. Opciones disponibles: " + player1Name + " o " + player2Name;
            }else{
                result = updateResult(result);
            }

        }catch(Exception e){
            e.printStackTrace();
        }

        return result;
    }

    public String updateResult(String player){

        switch (player){
            case player1Name:
                sumaPunto(player1);
                break;

            case player2Name:
                sumaPunto(player2);
                break;

            default:
                break;
        }

        return getResult();
    }

    public void sumaPunto(Player player){

        if(player.total == 0 || player.total == 15){
            player.total += 15;
        }else if(player.total == 30){
            player.total += 10;
        }else if(player.total == 40){
            if(!player.advantage){
                for(Player playerAdvantage : players){
                    if(!playerAdvantage.name.equalsIgnoreCase(player.name))
                        if(playerAdvantage.advantage){
                            playerAdvantage.advantage = false;
                        }else{
                           player.advantage = true;
                        }
                }
            }else{
                player.winner = true;
                matchWinner = true;
            }
        }
    }

    public String getResult(){

        String texto = "";
        Player player1 = players[0];
        Player player2 = players[1];

        if(!matchWinner) {
            if (player1.advantage) {
                texto = "Ventaja " + player1.name;
            } else if (player2.advantage) {
                texto = "Ventaja " + player2.name;
            } else if (player1.total == player2.total && player1.total == 40) {
                texto = "Deuce";
            }else{
                texto += player1.total==0 ? "love":player1.total + " - ";
                texto+= player2.total==0?"love":player2.total;
            }
        }else{
            if (player1.winner) {
                texto = "Ha ganado el " + player1.name;
            } else {
                texto = "Ha ganado el " + player2.name;
            }
        }

        return texto;
    }

    public class Player{

        private int total = 0;
        private boolean advantage = false;
        private String name;
        private boolean winner = false;

        public Player(String name){
            this.name = name;
        }
    }
}

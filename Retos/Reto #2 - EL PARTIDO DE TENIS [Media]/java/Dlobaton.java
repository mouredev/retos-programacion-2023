
public class Dlobaton {
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

    private static final String  LOVE = "Love";
    private static final String  FIFTEEN = "15";
    private static final String  THIRTY = "30";
    private static final String  FORTY = "40";
    private static final String  DEUCE = "Deuce";
    private static final String  VENTAJA = "Ventaja";
    private static final String  GANAP1 = "Ha ganado el P1";
    private static final String  GANAP2 = "Ha ganado el P2";
    private static final String  VENTAJAP1 = "Ventaja P1";
    private static final String  VENTAJAP2 = "Ventaja P2";

    private static final String  WINS = "Wins";



    public static class MatchScore {
        String p1 = LOVE;
        String p2 = LOVE;

        public void incP1(){
            switch (p1) {
                case LOVE -> p1 = FIFTEEN;
                case FIFTEEN -> p1 = THIRTY;
                case THIRTY -> p1 = FORTY;
                case FORTY -> {
                    if (p2.equals(FORTY)) {
                        p1 = VENTAJA;
                    } else if (p2.equals(VENTAJA)) {
                        p2 = FORTY;
                    }
                }
                case VENTAJA -> p1 = WINS;
                case WINS -> {
                    p1 = LOVE;
                    p2 = LOVE;
                }
                default -> {
                }
            }
        }

        public void incP2(){
            switch (p2) {
                case LOVE -> p2 = FIFTEEN;
                case FIFTEEN -> p2 = THIRTY;
                case THIRTY -> p2 = FORTY;
                case FORTY -> {
                    if (p1.equals(FORTY)) {
                        p2 = VENTAJA;
                    } else if (p1.equals(VENTAJA)) {
                        p1 = FORTY;
                    }
                }
                case VENTAJA -> p2 = WINS;
                case WINS -> {
                    p1 = LOVE;
                    p2 = LOVE;
                }
                default -> {
                }
            }
        }

        public boolean deuce(){
            return p1.equals(p2);
        }

        public boolean ventajaP1(){
            return p1.equals(VENTAJA);
        }

        public boolean ventajaP2(){
            return p2.equals(VENTAJA);
        }

        public boolean winsP1(){
            return p1.equals(WINS);
        }

        public boolean winsP2(){
            return p2.equals(WINS);
        }

        // Referee will say the current result after each game
        public String referee(){
            if(winsP1()){
                return GANAP1;
            } else if(winsP2()){
                return GANAP2;
            } else if(ventajaP1()){
                return VENTAJAP1;
            } else if(ventajaP2()){
                return VENTAJAP2;
            } else if(deuce()){
                return DEUCE;
            } else {
                return p1 + " - " + p2;
            }
        }
    }

    public enum Player {
        P1,P2
    }

    public static void main (String [] args){
        String [] aux = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
        MatchScore matchScore = new MatchScore();

        for(String arg: aux){
            if (arg.equals(Player.P1.name())) {
                matchScore.incP1();
            } else {
                matchScore.incP2();
            }
            System.out.println(matchScore.referee());
        }
    }
}
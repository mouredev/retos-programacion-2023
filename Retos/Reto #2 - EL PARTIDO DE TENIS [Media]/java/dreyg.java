
public class Main {

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

    public static void main(String[] args) {
        System.out.println("¡¡ Marcador de Juego de Tenis / Padel !!");
        boolean endGame = false;
        String pointPlayer = "";
        String sScoreP1 = "Love";
        String sScoreP2 = "Love";
        String scoreMatchTotal = sScoreP1.concat(" - ").concat(sScoreP2);
        String [] resultsInputs = new String[] {"P1","P1","P1","P2","P2","P2","P1","P1"};
        int cont = 0;
        while (!endGame || (cont < resultsInputs.length)){
            pointPlayer = resultsInputs[cont]; //stringInput();
            switch (pointPlayer){
                case "P1":
                    sScoreP1 = updateScorePlayer(sScoreP1, sScoreP2);
                    break;
                case "P2":
                    sScoreP2 = updateScorePlayer(sScoreP2, sScoreP1);
                    break;
            }
            scoreMatchTotal = updateScoreMatch(sScoreP1, sScoreP2, scoreMatchTotal);
            if (scoreMatchTotal.equals("Ha ganado " + pointPlayer))
                endGame = true;
            System.out.println(scoreMatchTotal);
            cont = cont + 1;
        }
        //System.out.println(scoreMatchTotal);
    }

    private static String updateScorePlayer(String sScorePx, String sScoreLoser) {
        if (sScorePx.equals("Love"))
            sScorePx = "15";
        else if (sScorePx.equals("15"))
            sScorePx = "30";
        else if (sScorePx.equals("30"))
            sScorePx = "40";
        else if (sScorePx.equals("Deuce"))
            sScorePx = "Ventaja";
        else if (sScorePx.equals("40") && sScoreLoser.equals("40"))
            sScorePx = "Ventaja";
        else if (sScorePx.equals("40") && sScoreLoser.equals("Ventaja"))
            sScorePx = "Deuce";
        else if (sScorePx.equals("40") && !sScoreLoser.equals("40"))
            sScorePx = "Win";
        else if (sScorePx.equals("Ventaja"))
            sScorePx = "Win";
        return sScorePx;
    }

    private static String updateScoreMatch(String sScoreP1, String sScoreP2, String sScoreMatchTotal) {
        if (sScoreP1.equals("40") && sScoreP2.equals("40") ||
                (sScoreP2.equals("Ventaja") && (sScoreP1.equals("Ventaja"))))
            sScoreMatchTotal = "Deuce";
        else if(sScoreP1.equals("Win") ||
                (sScoreP1.equals("Ventaja") && (!sScoreP2.equals("40")) &&  (!sScoreP2.equals("Ventaja"))))
            sScoreMatchTotal = "Ha ganado " + "P1";
        else if(sScoreP2.equals("Win") ||
                (sScoreP2.equals("Ventaja") && (!sScoreP1.equals("40")) && (!sScoreP1.equals("Ventaja"))))
            sScoreMatchTotal = "Ha ganado " + "P2";
        else
            sScoreMatchTotal = sScoreP1.concat(" - ").concat(sScoreP2);
        return sScoreMatchTotal;
    }

    private static String stringInput() {
        System.out.println ("Por favor, inserte que jugador ha marcado: ['P1' / 'P2'] ");
        Scanner inputScanner = new Scanner (System.in); //Creación de un objeto Scanner
        return inputScanner.nextLine().toUpperCase(); //Invocamos un método sobre un objeto Scanner
    }

}
public class mario_16 {

    public static void main(String[] args) {

        String[] arrayJugadas = {"spock-tijera", "tijera-spock", "spock-lagarto"};
        String[] arrayJugadas2 = {"papel-tijera", "tijera-tijera", "piedra-tijera"};
        String[] arrayJugadas3 = {"spock-tijera", "tijera-spock", "spock-lagarto", "papel-piedra"};

        jugarPiedraPapelTijeraLagartoSpock(arrayJugadas);
        jugarPiedraPapelTijeraLagartoSpock(arrayJugadas2);
        jugarPiedraPapelTijeraLagartoSpock(arrayJugadas3);

    }

    private static void jugarPiedraPapelTijeraLagartoSpock(String[] jugadas) {

        int ptos1 = 0;
        int ptos2 = 0;

        for (String jugada : jugadas) {
            String[] ronda = jugada.split("-");
            String jugadaP1 = ronda[0];
            String jugadaP2 = ronda[1];

            if (jugadaP1.equalsIgnoreCase(jugadaP2)){
                ptos1 += 0;
                ptos2 += 0;
            }else{
                if (jugadaP1.equalsIgnoreCase("piedra")) {
                    if (jugadaP2.equalsIgnoreCase("tijera") || jugadaP2.equalsIgnoreCase("lagarto")) {
                        ptos1 += 1;
                    } else {
                        ptos2 += 1;
                    }
                }

                if (jugadaP1.equalsIgnoreCase("papel")){
                    if (jugadaP2.equalsIgnoreCase("piedra") || jugadaP2.equalsIgnoreCase("spock")){
                        ptos1 += 1;
                    }else{
                        ptos2 += 1;
                    }
                }

                if (jugadaP1.equalsIgnoreCase("tijera")){
                    if (jugadaP2.equalsIgnoreCase("papel") || jugadaP2.equalsIgnoreCase("lagarto")){
                        ptos1 += 1;
                    }else{
                        ptos2 += 1;
                    }
                }

                if (jugadaP1.equalsIgnoreCase("lagarto")){
                    if (jugadaP2.equalsIgnoreCase("spock") || jugadaP2.equalsIgnoreCase("papel")){
                        ptos1 += 1;
                    }else{
                        ptos2 += 1;
                    }
                }

                if (jugadaP1.equalsIgnoreCase("spock")){
                    if (jugadaP2.equalsIgnoreCase("tijera") || jugadaP2.equalsIgnoreCase("piedra")){
                        ptos1 += 1;
                    }else{
                        ptos2 += 1;
                    }
                }
            }
        }
        System.out.println(ptos1 == ptos2 ? "Empate!" : ptos1 > ptos2 ? "Ganador P1" : "Ganador P2");
    }

}


public class Dreyg {

    private static final String PIEDRA = "piedra";
    private static final String PAPEL = "papel";
    private static final String TIJERA = "tijera";
    private static final String LAGARTO = "lagarto";
    private static final String SPOCK = "spock";

    private static final String P1 = "Player 1";
    private static final String P2 = "Player 2";
    private static final String TIE = "Tie";

    public static void main(String[] args) {

        System.out.println();
        System.out.println("Reto #5: Juego \"piedra, papel, tijera, lagarto, spock\".");
        System.out.println();

        Map<String,String> results = new HashMap<>();
        results.put(PAPEL,TIJERA);
        results.put(PAPEL,PIEDRA);
        results.put(LAGARTO,LAGARTO);
        results.put(SPOCK,LAGARTO);
        results.put(SPOCK,TIJERA);

        int partialResult = 0;

        for (Map.Entry<String, String> entry : results.entrySet()) {
            partialResult += whoWins(entry.getKey(), entry.getValue());
        }

        //System.out.println(partialResult);
        if (partialResult == 0)
            System.out.println(TIE);
        else if (partialResult < 0)
            System.out.println(P2);
        else
            System.out.println(P1);

    }

    private static int whoWins(String score1, String score2) {
        int result = 0;
        switch (score1) {
            case TIJERA: {
                if (score2.equals(PAPEL) || score2.equals(LAGARTO))
                    result = 1;
                else if (score2.equals(PIEDRA) || score2.equals(SPOCK))
                    result = -1;
                else
                    result = 0;
                break;
            }
            case PAPEL: {
                if (score2.equals(PIEDRA) || score2.equals(SPOCK))
                    result = 1;
                else if (score2.equals(TIJERA) || score2.equals(LAGARTO))
                    result = -1;
                else
                    result = 0;
                break;
            }
            case PIEDRA: {
                if (score2.equals(LAGARTO) || score2.equals(TIJERA))
                    result = 1;
                else if (score2.equals(PAPEL) || score2.equals(SPOCK))
                    result = -1;
                else
                    result = 0;
                break;
            }
            case LAGARTO: {
                if (score2.equals(SPOCK) || score2.equals(PAPEL))
                    result = 1;
                else if (score2.equals(PIEDRA) || score2.equals(TIJERA))
                    result = -1;
                else
                    result = 0;
                break;
            }
            case SPOCK: {
                if (score2.equals(PIEDRA) || score2.equals(TIJERA))
                    result = 1;
                else if (score2.equals(LAGARTO) || score2.equals(PAPEL))
                    result = -1;
                else
                    result = 0;
                break;
            }
            default : result = 0;
        };
        return result;
    }


}
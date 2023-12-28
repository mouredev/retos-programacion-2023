import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
public class Alvarogtz {

    private enum options{PIEDRA,PAPEL,TIJERA,LAGARTO,SPOCK};
    public static void main(String[] args){

        System.out.println("The game has started ...\n");

        List<Pair> myPairs = new ArrayList();
        myPairs.add(new Pair(options.PIEDRA,options.TIJERA));
        myPairs.add(new Pair(options.TIJERA,options.PIEDRA));
        myPairs.add(new Pair(options.PAPEL,options.TIJERA));

        Alvarogtz.evaluateGame(myPairs);

        myPairs = new ArrayList();
        myPairs.add(new Pair(options.PIEDRA,options.TIJERA));
        myPairs.add(new Pair(options.TIJERA,options.TIJERA));
        myPairs.add(new Pair(options.PAPEL,options.TIJERA));

        Alvarogtz.evaluateGame(myPairs);

        myPairs = new ArrayList();
        myPairs.add(new Pair(options.PIEDRA,options.LAGARTO));
        myPairs.add(new Pair(options.LAGARTO,options.PIEDRA));
        myPairs.add(new Pair(options.TIJERA,options.PAPEL));
        myPairs.add(new Pair(options.PAPEL,options.LAGARTO));
        myPairs.add(new Pair(options.SPOCK,options.LAGARTO));

        Alvarogtz.evaluateGame(myPairs);
    }

    public static void evaluateGame(List<Pair> game){
        int pointsPlayer1 = 0;
        int pointsPlayer2 = 0;
        Map<String,options> rules = getRules();

        for(Pair pair : game){
            options player1 = pair.value1;
            options player2 = pair.value2;

            System.out.println(pair.toString());
            options result = rules.get(pair.toString());

            if(player1 == result)
                pointsPlayer1++;
            if(player2 == result)
                pointsPlayer2++;
        }

        String resultado = "Resultado -> ";
        resultado += pointsPlayer1>pointsPlayer2?"Player 1":pointsPlayer2>pointsPlayer1?"Player2":"deuce";

        System.out.println(resultado + "\n");
    }

    public static Map<String,options> getRules(){
        Map<String,options> rules = new HashMap<>();
        rules.put(new Pair(options.PIEDRA,options.PAPEL).toString(),options.PAPEL);
        rules.put(new Pair(options.PIEDRA,options.TIJERA).toString(),options.PIEDRA);
        rules.put(new Pair(options.PIEDRA,options.LAGARTO).toString(),options.PIEDRA);
        rules.put(new Pair(options.PIEDRA,options.SPOCK).toString(),options.SPOCK);

        rules.put(new Pair(options.PAPEL,options.PIEDRA).toString(),options.PAPEL);
        rules.put(new Pair(options.PAPEL,options.TIJERA).toString(),options.TIJERA);
        rules.put(new Pair(options.PAPEL,options.LAGARTO).toString(),options.LAGARTO);
        rules.put(new Pair(options.PAPEL,options.SPOCK).toString(),options.PAPEL);

        rules.put(new Pair(options.TIJERA,options.PAPEL).toString(),options.TIJERA);
        rules.put(new Pair(options.TIJERA,options.PIEDRA).toString(),options.PIEDRA);
        rules.put(new Pair(options.TIJERA,options.LAGARTO).toString(),options.TIJERA);
        rules.put(new Pair(options.TIJERA,options.SPOCK).toString(),options.SPOCK);

        rules.put(new Pair(options.LAGARTO,options.PAPEL).toString(),options.LAGARTO);
        rules.put(new Pair(options.LAGARTO,options.TIJERA).toString(),options.TIJERA);
        rules.put(new Pair(options.LAGARTO,options.PIEDRA).toString(),options.PIEDRA);
        rules.put(new Pair(options.LAGARTO,options.SPOCK).toString(),options.LAGARTO);

        rules.put(new Pair(options.SPOCK,options.PAPEL).toString(),options.PAPEL);
        rules.put(new Pair(options.SPOCK,options.TIJERA).toString(),options.SPOCK);
        rules.put(new Pair(options.SPOCK,options.LAGARTO).toString(),options.LAGARTO);
        rules.put(new Pair(options.SPOCK,options.PIEDRA).toString(),options.SPOCK);

        return rules;

    }

    public static class Pair{
        private options value1,value2;
        public Pair(options value1,options value2) {
            this.value1 = value1;
            this.value2 = value2;
        }
        public String toString(){
            return this.value1.toString() + " - " + this.value2.toString();
        }
    }
}
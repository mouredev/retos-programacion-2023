import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class josepmonclus {

    private enum Play{PIEDRA,PAPEL,TIJERA,LAGARTO,SPOCK};

    Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        //Player 2 wins
        List<Turn> game = new ArrayList<>();
        game.add(josepmonclus.new Turn(Play.PIEDRA, Play.TIJERA));
        game.add(josepmonclus.new Turn(Play.TIJERA, Play.PIEDRA));
        game.add(josepmonclus.new Turn(Play.PAPEL, Play.TIJERA));

        josepmonclus.evaluateGame(game);

        //Player 1 wins
        game = new ArrayList<>();
        game.add(josepmonclus.new Turn(Play.LAGARTO, Play.SPOCK));
        game.add(josepmonclus.new Turn(Play.LAGARTO, Play.TIJERA));
        game.add(josepmonclus.new Turn(Play.PIEDRA, Play.TIJERA));

        josepmonclus.evaluateGame(game);

        //Tie
        game = new ArrayList<>();
        game.add(josepmonclus.new Turn(Play.LAGARTO, Play.SPOCK));
        game.add(josepmonclus.new Turn(Play.LAGARTO, Play.TIJERA));
        game.add(josepmonclus.new Turn(Play.PIEDRA, Play.TIJERA));
        game.add(josepmonclus.new Turn(Play.TIJERA, Play.SPOCK));

        josepmonclus.evaluateGame(game);
    }

    public void evaluateGame(List<Turn> game) {
        int score1 = 0, score2 = 0;
        System.out.println();
        System.out.println("-----------------------------------------");
        System.out.println("¡NUEVA PARTIDA!");
        System.out.println("---------------");
        for(Turn turn : game) {
            System.out.println(turn);

            int winner = evaluateTurn(turn);

            if(winner == 1) score1++;
            else if (winner == 2) score2++;
        }

        System.out.println("---------------");
        System.out.println("Puntuación final:");
        System.out.println(" Jugador 1 -> " + score1);
        System.out.println(" Jugador 2 -> " + score2);
        System.out.println("");
        System.out.print("Resultado: ");

        if(score1 == score2) System.out.println("Empate");
        else if(score1 > score2) System.out.println("¡¡Jugador 1 gana!!");
        else if(score2 > score1) System.out.println("¡¡Jugador 2 gana!!");

        System.out.println("-----------------------------------------");
    }

    // return: 1 = P1, 2 = P2, 0 = TIE
    public int evaluateTurn(Turn turn) {
        int winner = 0;

        if(turn.p1 == Play.PIEDRA) {
            if(turn.p2 == Play.PIEDRA) winner = 0;
            else if(turn.p2 == Play.PAPEL) winner = 2;
            else if(turn.p2 == Play.TIJERA) winner = 1;
            else if(turn.p2 == Play.LAGARTO) winner = 1;
            else if(turn.p2 == Play.SPOCK) winner = 2;
        } else if (turn.p1 == Play.PAPEL) {
            if(turn.p2 == Play.PIEDRA) winner = 1;
            else if(turn.p2 == Play.PAPEL) winner = 0;
            else if(turn.p2 == Play.TIJERA) winner = 2;
            else if(turn.p2 == Play.LAGARTO) winner = 2;
            else if(turn.p2 == Play.SPOCK) winner = 1;            
        } else if (turn.p1 == Play.TIJERA) {
            if(turn.p2 == Play.PIEDRA) winner = 2;
            else if(turn.p2 == Play.PAPEL) winner = 1;
            else if(turn.p2 == Play.TIJERA) winner = 0;
            else if(turn.p2 == Play.LAGARTO) winner = 1;
            else if(turn.p2 == Play.SPOCK) winner = 2;            
        } else if (turn.p1 == Play.LAGARTO) {
            if(turn.p2 == Play.PIEDRA) winner = 2;
            else if(turn.p2 == Play.PAPEL) winner = 1;
            else if(turn.p2 == Play.TIJERA) winner = 2;
            else if(turn.p2 == Play.LAGARTO) winner = 0;
            else if(turn.p2 == Play.SPOCK) winner = 1;            
        } else if (turn.p1 == Play.SPOCK) {
            if(turn.p2 == Play.PIEDRA) winner = 1;
            else if(turn.p2 == Play.PAPEL) winner = 2;
            else if(turn.p2 == Play.TIJERA) winner = 1;
            else if(turn.p2 == Play.LAGARTO) winner = 2;
            else if(turn.p2 == Play.SPOCK) winner = 0;            
        }

        return winner;
    }

    public class Turn{
        public Play p1, p2;
        
        public Turn(Play p1, Play p2) {
            this.p1 = p1;
            this.p2 = p2;
        }

        @Override
        public String toString() {
            return "J1: " + p1.toString() + "\t" + "J2: " + p2.toString();
        }
    }
}

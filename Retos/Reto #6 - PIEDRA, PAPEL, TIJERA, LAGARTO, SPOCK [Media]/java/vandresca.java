import java.util.Random;
import java.util.Scanner;

/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "PlayerResult 1", "PlayerResult 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "PlayerResult 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

public class vandresca {
    public static void main(String[] args) {
        System.out.println("Pulsa 'Enter' para continuar o 'F' para terminar");
        String input;
        Scanner scanner;
        
        do{
            scanner = new Scanner(System.in);
            input = scanner.nextLine();            
            if(input.equals("F")) break;
            playGame();
            printGameResult();
            setScoreBoard();
        }while(hasEnd(input));
        scanner.close(); 

        printFinalWinner();
    }

    private static void playGame(){     
        Game.resultPlayer1 = randomOption();
        Game.resultPlayer2 = randomOption();
        Game.winner = switch(Game.resultPlayer1){
            case ROCK -> hasWinROCK(Game.resultPlayer1, Game.resultPlayer2); 
            case PAPER -> hasWinPAPER(Game.resultPlayer1, Game.resultPlayer2);
            case SCISSORS -> hasWinSCISSORS(Game.resultPlayer1, Game.resultPlayer2);
            case LIZARD -> hasWinLIZARD(Game.resultPlayer1, Game.resultPlayer2);
            case SPOCK -> hasWinSPOCK(Game.resultPlayer1, Game.resultPlayer2);
            default -> PlayerResult.TIE; 
        };
    }

    private static Posibility randomOption(){
        Random random = new Random();
        return Posibility.getElement(random.nextInt(5)+1);   
    }

    public static PlayerResult hasWinROCK(Posibility player1, Posibility player2){
        Boolean result;
        if(Posibility.LIZARD.equals(player2) || 
            Posibility.PAPER.equals(player2) ){ 
            result = true;
        }else{
            result = false;
        }
        if(Posibility.ROCK.equals(player2)) return PlayerResult.TIE;
        return result && Posibility.ROCK.equals(player1)? PlayerResult.ONE:PlayerResult.TWO;        
    }

    public static PlayerResult hasWinPAPER(Posibility player1, Posibility player2){
        Boolean result;
        if(Posibility.ROCK.equals(player2) || 
            Posibility.SPOCK.equals(player2) ){ 
            result = true;
        }else{
            result = false;
        }
        if(Posibility.PAPER.equals(player2)) return PlayerResult.TIE;
        return result && Posibility.PAPER.equals(player1)? PlayerResult.ONE:PlayerResult.TWO;
    }

    public static PlayerResult hasWinSCISSORS(Posibility player1, Posibility player2){
        Boolean result;
        if(Posibility.LIZARD.equals(player2) || 
            Posibility.PAPER.equals(player2) ){ 
            result = true;
        }else{
            result = false;
        }
        if(Posibility.SCISSORS.equals(player2)) return PlayerResult.TIE;
        return result && Posibility.SCISSORS.equals(player1)? PlayerResult.ONE:PlayerResult.TWO;
    }

    public static PlayerResult hasWinLIZARD(Posibility player1, Posibility player2){
        Boolean result;
        if(Posibility.SPOCK.equals(player2) || 
            Posibility.PAPER.equals(player2) ){ 
            result = true;
        }else{
            result = false;
        }
        if(Posibility.LIZARD.equals(player2)) return PlayerResult.TIE;
        return result && Posibility.LIZARD.equals(player1)? PlayerResult.ONE:PlayerResult.TWO;
    }

    public static PlayerResult hasWinSPOCK(Posibility player1, Posibility player2){
        Boolean result;
        if(Posibility.LIZARD.equals(player2) || 
            Posibility.PAPER.equals(player2) ){ 
            result = true;
        }else{
            result = false;
        }
        if(Posibility.SPOCK.equals(player2)) return PlayerResult.TIE;
        return result && Posibility.ROCK.equals(player1)? PlayerResult.ONE:PlayerResult.TWO;
    }

    private static void printGameResult(){
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append(Game.resultPlayer1);
        stringBuilder.append(" - ");
        stringBuilder.append(Game.resultPlayer2);
        stringBuilder.append("");
        stringBuilder.append(" => ");
        stringBuilder.append(Game.winner);
        System.out.println(stringBuilder.toString());
    }

    private static void setScoreBoard(){
        if(PlayerResult.ONE.equals(Game.winner)){
            ScoreBoard.playerOne++;
        }else if(PlayerResult.TWO.equals(Game.winner)){
            ScoreBoard.playerTwo++;
        }
    }

    private static Boolean hasEnd(String input){
        return switch(input){
            case "F"->false;
            default ->true;
        };
    }

    private static void printFinalWinner(){
        if(ScoreBoard.playerOne > ScoreBoard.playerTwo){
            System.out.println("Ha ganado el jugador 1");
        }else if (ScoreBoard.playerOne < ScoreBoard.playerTwo){
            System.out.println("Ha ganado el jugador 2");
        }else{
            System.out.println("Ha habido un empate");
        }
        System.out.printf("Jugador 1= %d <-> Jugador 2= %d", ScoreBoard.playerOne, ScoreBoard.playerTwo);
    }
}

enum Posibility{ 
        ROCK(1), PAPER(2), SCISSORS(3), LIZARD(4), SPOCK(5);
        
        private int value;
        
        Posibility(int value){ 
            this.value=value;
        }

        public static Posibility getElement(int value){
            for (Posibility element : Posibility.values()) {
                if (element.value() == value) {
                    return element;
                }
            }
            throw new IllegalArgumentException("Valor entero inválido");
        }

        private int value(){
            return this.value;
        }
}

enum PlayerResult{
    ONE, TWO, TIE
}

class ScoreBoard {
    static int playerOne = 0;
    static int playerTwo = 0;   
}

class Game{
    static Posibility resultPlayer1;
    static Posibility resultPlayer2;
    static PlayerResult winner;
}




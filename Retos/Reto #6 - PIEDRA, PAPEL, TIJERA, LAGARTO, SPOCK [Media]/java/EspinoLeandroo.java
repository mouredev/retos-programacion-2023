import java.util.Scanner;
import java.util.StringTokenizer;

public class EspinoLeandroo {

    final String PIEDRA     = "PIEDRA";     //"🗿";
    final String PAPEL      = "PAPEL";      //"📄";
    final String TIJERA     = "TIJERA";     //"✂️";
    final String LAGARTO    = "LAGARTO";    //"🦎";
    final String SPOCK      = "SPOCK";      //"🖖";

    final String PLAYER1    = "Player1";
    final String PLAYER2    = "Player2";

    int rounds = 0;
    int player1Wins = 0;
    int player2Wins = 0;

    Scanner sc = new Scanner(System.in);
        

    public static void main(String[] args) {
        EspinoLeandroo eL = new EspinoLeandroo();
        eL.printScore();

        System.out.println("Input:");
        String playersOptions = eL.sc.nextLine();
        playersOptions = eL.clearInput(playersOptions);

        StringTokenizer st = new StringTokenizer(playersOptions, ",");
        while(st.hasMoreTokens()){
            eL.rounds++;
            String player1Option = st.nextToken();
            String player2Option = st.nextToken();
            
            String winner = eL.whoWin(player1Option, player2Option);
            if(winner.equals(eL.PLAYER1)){
                eL.player1Wins++;
            }else if(winner.equals(eL.PLAYER2)){
                eL.player2Wins++;
            }
        }
        eL.printScore();
        if(eL.player1Wins == eL.player2Wins){
            System.out.println("Tie");
        }else if(eL.player1Wins > eL.player2Wins){
            System.out.println(eL.PLAYER1);
        }else if(eL.player1Wins < eL.player2Wins){
            System.out.println(eL.PLAYER2);
        }
    }

    private String whoWin(String player1, String player2){
        if(player1.equals(player2)){
            return "Tie";
        }else if(player1.equals(PIEDRA)){
            if(player2.equals(TIJERA) || player2.equals(LAGARTO)){
                return PLAYER1;
            }else{
                return PLAYER2;
            }
        }else if(player1.equals(TIJERA)){
            if(player2.equals(PAPEL) || player2.equals(LAGARTO)){
                return PLAYER1;
            }else{
                return PLAYER2;
            }
        }else if(player1.equals(PAPEL)){
            if(player2.equals(SPOCK) || player2.equals(PIEDRA)){
                return PLAYER1;
            }else{
                return PLAYER2;
            }
        }else if(player1.equals(SPOCK)){
            if(player2.equals(TIJERA) || player2.equals(PIEDRA)){
                return PLAYER1;
            }else{
                return PLAYER2;
            }
        }else if(player1.equals(LAGARTO)){
            if(player2.equals(PAPEL) || player2.equals(SPOCK)){
                return PLAYER1;
            }else{
                return PLAYER2;
            }
        }
        return "";
    }

    private void printScore(){
        System.out.println("**********");
        System.out.println("Rounds " + rounds);
        System.out.println("**********");
        System.out.println("Player1 = " + player1Wins);
        System.out.println("Player2 = " + player2Wins);
        System.out.println("**********");
    }

    private String clearInput(String playersOptions){
        playersOptions = playersOptions.trim();
        playersOptions = playersOptions.toUpperCase();
        playersOptions = playersOptions.replace("[", "");
        playersOptions = playersOptions.replace("]", "");
        playersOptions = playersOptions.replace("(", "");
        playersOptions = playersOptions.replace(")", "");
        return playersOptions;
    }

}

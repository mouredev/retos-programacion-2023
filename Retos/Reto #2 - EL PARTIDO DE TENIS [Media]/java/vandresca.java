import java.util.Random;

/**
 * Escribe un programa que muestre un juego de tenis y quien
 * lo ha ganado.
 * El programa rebira una secuencia formada por:
 * "P1" (Player 1) o "P2" (Player 2) segun quien gane cada juego
 * - Las puntuaciones son:
 *  "Love" (cero), "15", "30", "40", "Deuce" (empate), "Advantage",  ventaja
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1] el programa
 *  mostraría:
 *      15 - Love
 *      30 - Love
 *      30 - 15
 *      30 - 30
 *      40 - 30
 *      Deuce
 *      Advantage P1
 *      Ha ganado P1
 * - Es posible controlar errores en la entrada de datos.
 * - Consulta las reglas de juego si tienes dudas sobre el sistema de puntos.
 */
public class vandresca {

    private static Player player1;

    private static Player player2;

    public static void main(String[] args) {
        init();
        while(!hasEnd()){
            setWinner();
            showScoreBoard();
            playGame(getWinner());
        }
    }

    private static Boolean hasEnd(){
        return player1.isWinner() || player2.isWinner();
    }

    private static void setWinner(){
        if(player1.isMoreThanFORTY() && differenceOfWin(player1, player2)) player1.setWinner();
        if(player2.isMoreThanFORTY() && differenceOfWin(player2, player1)) player2.setWinner();
    }

    private static Boolean differenceOfWin(Player player1, Player player2){
        return (player1.getNumberPoints() - player2.getNumberPoints())>1;
    }

    private static void init(){
        player1 = new Player();
        player2 = new Player();
    }

    private static Player getWinner(){
        Random rd = new Random();
        return (rd.nextBoolean())? player1 : player2;
    }

    private static void playGame(Player winner){
        winner.addPoint();
    }

    private static void showScoreBoard(){
        if(isDeuce()) print("DEUCE");
        else if(isAdvantagePlayer1()) print("ADVANTAGE PLAYER 1");
        else if(isAdvantagePlayer2()) print("ADVANTAGE PLAYER 2");
        else if(player1.isWinner()) print("WIN PLAYER 1");
        else if(player2.isWinner()) print("WIN PLAYER 2");
        else System.out.println(player1.getTypePoint() + " - " + player2.getTypePoint());
    }

    private static Boolean isDeuce(){
        return player1.getNumberPoints()>= Player.TypePoint.FORTY.ordinal() && player1.getNumberPoints()== player2.getNumberPoints();
    }

    private static Boolean isAdvantagePlayer1(){
        return (player1.getNumberPoints()> Player.TypePoint.FORTY.ordinal()) && (player1.getNumberPoints() - player2.getNumberPoints()==1);
    }

    private static Boolean isAdvantagePlayer2(){
        return (player2.getNumberPoints()> Player.TypePoint.FORTY.ordinal()) && (player2.getNumberPoints() - player1.getNumberPoints()==1);
    }

    private static void print(String text){
        System.out.println(text);
    }
}

class Player {
    private int points;

    private Boolean passFORTY;
    private Boolean winner;

    public enum TypePoint {
        LOVE, FIFTEEN, THIRTY, FORTY;
    }

    public Player() {
        this.points = 0;
        this.passFORTY = false;
        this.winner = false;
    }

    public int getNumberPoints(){
        return this.points;
    }

    public TypePoint getTypePoint(){
        return switch(this.points){
            case 0 -> TypePoint.LOVE;
            case 1 -> TypePoint.FIFTEEN;
            case 2 -> TypePoint.THIRTY;
            default -> TypePoint.FORTY;
        };
    }

    public void addPoint(){
        this.points++;
    }

    public Boolean isMoreThanFORTY(){
        return this.points > TypePoint.FORTY.ordinal();
    }

    public void setWinner(){
        this.winner = true;
    }

    public Boolean isWinner(){
        return this.winner;
    }
}

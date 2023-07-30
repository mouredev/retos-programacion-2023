package Reto6;

import java.util.Random;
import java.util.Scanner;

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

public class vandresca {

    public enum Player{
        ONE, TWO
    }

    public enum Posibility{ 
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

    public static void main(String[] args) {
        System.out.println("Pulsa 'Enter' para continuar o 'F' para terminar");
        String input;
        Scanner scanner;
        int scorePlayer1 = 0;
        int scorePlayer2 = 0;
        do{
            scanner = new Scanner(System.in);
            input = scanner.nextLine();
            
            if(input.equals("F")) break;
            if(playGame().equals(Player.ONE)){
                scorePlayer1++;
            }else{
                scorePlayer2++;
            }

        }while(hasEnd(input));
        scanner.close();
        printFinalWinner(scorePlayer1, scorePlayer2);
    }

    private static void printFinalWinner(int scorePlayer1, int scorePlayer2){
        if(scorePlayer1 > scorePlayer2){
            System.out.println("Ha ganado el jugador 1");
        }else if (scorePlayer1 < scorePlayer2){
            System.out.println("Ha ganado el jugador 2");
        }else{
            System.out.println("Ha habido un empate");
        }
        System.out.printf("Jugador 1= %d <-> Jugador 2= %d", scorePlayer1, scorePlayer2);
    }

    private static Boolean hasEnd(String input){
        return switch(input){
            case "F"->false;
            default ->true;
        };
    }

    private static Posibility randomOption(){
        Random random = new Random();
        return Posibility.getElement(random.nextInt(5)+1);   
    }

    private static Player playGame(){
        Posibility resultPlayer1 = randomOption();
        Posibility resultPlayer2 = randomOption();
        Player winner;

        if(resultPlayer1.equals(Posibility.ROCK)){ 
           if(resultPlayer2.equals(Posibility.LIZARD) || 
              resultPlayer2.equals(Posibility.PAPER) ){ 
                winner=Player.ONE;
            }else{
                winner=Player.TWO;
            }
        }else if(resultPlayer1.equals(Posibility.PAPER)){
            if(resultPlayer2.equals(Posibility.ROCK) || 
              resultPlayer2.equals(Posibility.SPOCK) ){ 
                winner=Player.ONE;
            }else{
                winner=Player.TWO;
            }
        }else if(resultPlayer1.equals(Posibility.SCISSORS)){
            if(resultPlayer2.equals(Posibility.PAPER) || 
              resultPlayer2.equals(Posibility.LIZARD) ){ 
                winner=Player.ONE;
            }else{
                winner=Player.TWO;
            }
        }else if(resultPlayer1.equals(Posibility.LIZARD)){
            if(resultPlayer2.equals(Posibility.SPOCK) || 
              resultPlayer2.equals(Posibility.PAPER) ){ 
                winner=Player.ONE;
            }else{
                winner=Player.TWO;
            }
        }else{
            if(resultPlayer2.equals(Posibility.SCISSORS) || 
              resultPlayer2.equals(Posibility.ROCK) ){ 
                winner=Player.ONE;
            }else{
                winner=Player.TWO;
            }
        }
        System.out.println(resultPlayer1 + " - "+ resultPlayer2+" => " + winner);
        return winner;
    }

}

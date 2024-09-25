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
package reto_06_papel_tijera_lagarto_Spock;

import java.util.Scanner;

public class IASR1987 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//introducir por teclado
		Scanner teclado = new Scanner(System.in);
		//jugadas posibles;
		String [] jugadas= {"Piedra","Papel","Tijera","Lagarto","Spock"};
		//salir del juego
		int respuesta=0;
		//calculo de las partidas.
		int statsPlayer1=0;
		int statsPlayer2=0;
		int empates=0;
		
		do {
			//Sorteamos lo que le toca a cada jugador
			int azarPlayer1=(int)(Math.random()*5);
			String Player1=jugadas[azarPlayer1];
			
			int azarPlayer2=(int)(Math.random()*5);
			String Player2=jugadas[azarPlayer2];
			
			
			//comprobamos las jugadas
			if(Player1.equals(Player2)){
				System.out.println(Player1+" vs "+ Player2);
				System.out.println("Empate");
				empates++;
			}else if(Player1.equals("Piedra")) {
				if(Player2.equals("Tijera")|| Player2.equals("Lagarto")) {
					statsPlayer1++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 1");
				}else {
					statsPlayer2++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 2");
				}
			}else if(Player1.equals("Papel")) {
				if(Player2.equals("Piedra")|| Player2.equals("Spock")) {
					statsPlayer1++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 1");
				}else {
					statsPlayer2++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 2");
				}
			}else if(Player1.equals("Tijera")) {
				if(Player2.equals("Papel")|| Player2.equals("Lagarto")) {
					statsPlayer1++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 1");
				}else {
					statsPlayer2++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 2");
				}
			}else if(Player1.equals("Lagarto")) {
				if(Player2.equals("Papel")|| Player2.equals("Spock")) {
					statsPlayer1++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 1");
				}else {
					statsPlayer2++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 2");
				}
			}else if(Player1.equals("Spock")){
				if(Player2.equals("Piedra")|| Player2.equals("Tijera")) {
					statsPlayer1++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 1");
				}else {
					statsPlayer2++;
					System.out.println(Player1+" vs "+ Player2);
					System.out.println("Gana jugador 2");
				}
			}
			
			System.out.println("Quieres abandonar el juego pulsa 0, para continuar pulsa 1");
			respuesta= teclado.nextInt();
		}while(respuesta!=0);
	
		int partidaTotal=statsPlayer1+statsPlayer2+empates;
		System.out.println("Estadisticas");
		System.out.println("Partidas totales => "+ partidaTotal+".");
		System.out.println("Partidas Player1 => "+ statsPlayer1+".");
		System.out.println("Partidas Player2 => "+ statsPlayer2+".");
		System.out.println("Partidas empates => "+ empates+".");
		teclado.close();
	}
}

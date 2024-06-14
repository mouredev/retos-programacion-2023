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
package reto_02_ElPartidoDeTenis;

public class IASR1987 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int P1=0;
		int P2=0;
		String[] secuencia= {"P1","P1","P1","P2","P2","P2","P1","P2","P2","P1","P1","P1"};
		String[] puntuacion= {"love","15","30","40","Deuce","Ventaja","Ganaste"};
		boolean ganador= false;
		
		for(int i=0;ganador==false;i++) {
			
			if(secuencia[i].equals("P1")) {
				P1++;
			}else {
				P2++;
			}
			
			if(P1<4 && P2<4) {
				System.out.println(puntuacion[P1]+"--"+puntuacion[P2]);
			}else if(P1>=4 || P2>=4){
				if(P1>=(P2+2)) {
					System.out.println("Ganador Jugador 1");
					ganador=true;
				}else if(P2>=(P1+2)) {
					System.out.println("Ganador Jugador 2");
					ganador=true;
				}else if(P1==P2) {
					System.out.println("Deuce");
				}else {
					if(P1>P2) {
						System.out.println("Ventaja jugador 1");
					}else {
						System.out.println("Ventaja Jugador 2");
					}
				}
			}
		
			System.out.println("Puntuacion 1 = " + P1 + "  Puntuacion 2 = "+ P2);
			
		}
	}

}

/**
 * 
 */
package ec.com.vijes.retos;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import ec.com.vijes.retos.common.HackerUtil;
import ec.com.vijes.retos.common.TennisMatchUtil;

/**
 * @author vijes
 *
 */
public class VictorJaramillo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
			PartidoTenisReto2();
	}

	public static void PartidoTenisReto2() {
		Integer playerOne = 0;
		Integer playerTwo = 0;
		List<String> partidas = Arrays.asList("P1", "P1", "P2", "P2", "P1", "P2", "P2", "P2");
		if ( partidas != null && partidas.size()  > 0) {
			for (String jugadorGana: partidas ) {
				if ( !jugadorGana.equals("P1") && !jugadorGana.equals("P2") ) {
					System.out.println("Jugada no permitida...!!!!");
					continue;
				} else if ( jugadorGana.equals("P1") ) {
					playerOne = TennisMatchUtil.getPoint(playerOne);					
				} else if ( jugadorGana.equals("P2") ) {
					playerTwo = TennisMatchUtil.getPoint(playerTwo);
				}
				// imprimir resultados
				// El primero que haga mas de 50 puntos gana y termina el juego.
				if ( playerOne > 50 ) {
					System.out.println("Ha ganado el P1");
					break;
				} else if ( playerTwo > 50 ) {
					System.out.println("Ha ganado el P2");
					break;
				}
				if ( playerOne == 40 && playerTwo == 40 ) {
					System.out.println("Deuce");
				} else if ( playerOne > 40 && playerTwo <= 40 ) {
					System.out.println("Ventaja P1");
				} else if ( playerOne <= 40 && playerTwo > 40 ) {
					System.out.println("Ventaja P2");
				} else {
					System.out.println( "".concat(playerOne == 0 ? "Love" : playerOne.toString())
							.concat(" - ")
							.concat(playerTwo == 0 ? "Love" : playerTwo.toString()));
				}
			}
			
		} else {
			System.out.println("No se encontraron partidas.");
		}
		
	}
}

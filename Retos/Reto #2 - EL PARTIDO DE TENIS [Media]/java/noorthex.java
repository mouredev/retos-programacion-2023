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
public class noorthex {
	
	public void juegoTenis()
	{
		String secuencia[] = {"P1","P1","P2","P2","P1","P2","P1","P1"};
		int P1 = 0; int P2 = 0; int contador = 4;
		for(int i = 0;i<secuencia.length;i++)
		{
			switch(secuencia[i])
			{
				case "P1":
				{
					P1 = P1 + 15;
					break;
				}
				case "P2":
				{
					P2 = P2 + 15;
					break;
				}
			}
			if(i == contador)
			{
				if(secuencia[i] == "P1")
				{
					P1 = P1 - 5;
					contador = contador + 1;
				}
				if(secuencia[i] == "P2")
				{
					P2 = P2 - 5;
					contador = contador + 1;
				}
				if(P1 == P2)
				{
					System.out.println("Deuce");
					continue;
				}
				if(P1 == 50)
				{
					System.out.println("Ventaja P1");
					continue;
				}
				if(P1 == 60)
				{
					System.out.println("Ha ganado el P1");
					continue;
				}
			}
			System.out.println(P1+"-"+P2);
		}
	}
}
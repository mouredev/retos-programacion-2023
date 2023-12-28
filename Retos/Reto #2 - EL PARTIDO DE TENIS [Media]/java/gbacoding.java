public class Reto2ElPartidoDeTenis {

	public static void main(String[] args) {
	
		
		// ENTRADA DE DATOS
		String [] secuenciaPartido = {"P1","P1","P2","P2","P1","P2","P1","P1","P1"};
		String [] puntuacionesJuego = {"Love","15","30","40","Deuce","Ventaja", "Ha ganado"};
		
		// PROCESAMIENTO
		 
		for (int i=0, contadorJuegoPlayer1=0, contadorJuegoPlayer2=0; i < 9; i++) {
			
				if (secuenciaPartido[i].equals("P1"))  {
					contadorJuegoPlayer1 = contadorJuegoPlayer1 + 1;
						if (contadorJuegoPlayer1 == 4) {
							System.out.println(puntuacionesJuego[contadorJuegoPlayer1]);
							} else if(contadorJuegoPlayer1 == 5){
							System.out.println(puntuacionesJuego[contadorJuegoPlayer1] + " P1");
							} else if (contadorJuegoPlayer1 == 6){
								System.out.println(puntuacionesJuego[contadorJuegoPlayer1] + " P1");
							
						} else {
							System.out.println(puntuacionesJuego[contadorJuegoPlayer1]+ "-" + puntuacionesJuego[contadorJuegoPlayer2]);
						}
					
				} else if (secuenciaPartido[i].equals("P2")) {
					contadorJuegoPlayer2 = contadorJuegoPlayer2 + 1;
					System.out.println(puntuacionesJuego[contadorJuegoPlayer1]+ "-" + puntuacionesJuego[contadorJuegoPlayer2]);
					}
					
				
				} // cierre for
		
		
			}// cierre main
}// cierre class

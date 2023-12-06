
public class Elez95 {
	
	private String [] tablero = {"Love", "15", "30", "40","Game"};
	private int indice_punto_actual_p1;
	private int indice_punto_actual_p2;
	private boolean deuce;
	private boolean ganador;
	
	public static void main(String [] args) {
		Elez95 reto = new Elez95();
		String [] puntos = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
		reto.juego(puntos);
	}
	
	
	public void juego(String [] puntos) {
		indice_punto_actual_p1 = 0; 
		indice_punto_actual_p2 = 0;
		deuce = false;
		ganador = false;
		int iterador = 0;
		
		while (iterador < puntos.length && !deuce && !ganador) {
			iterador = servicio(puntos, iterador);
		}
			
	}	
	
	
	private int servicio(String[] puntos, int iterador) {
		switch (puntos[iterador]) {
		case "P1": {
			indice_punto_actual_p1++;
			break;
		}
		case "P2":{
			indice_punto_actual_p2++;
			break;	
		}
		default:
			throw new IllegalArgumentException("Unexpected value: " + puntos[iterador]);
		}

		if (indice_punto_actual_p1 == 3 && indice_punto_actual_p2 == 3) {
			System.out.println("Deuce");
			iterador++;
			deuce (puntos,iterador);
		}else if (indice_punto_actual_p1 == 4) {
			System.out.println("Ganador P1");
			ganador = true;
		}else if (indice_punto_actual_p2 == 4) {
			System.out.println("Ganador P2");
			ganador = true;
		}else{
			System.out.println(tablero[indice_punto_actual_p1] + " - " + tablero[indice_punto_actual_p2]);
			iterador++;
		}

		return iterador;
	}
	
	
	private void deuce (String [] puntos, int iterador) {
		int distancia_de_ventaja = 0;
		while (distancia_de_ventaja > -2 && distancia_de_ventaja < 2) {

			switch (puntos[iterador]) {
			case "P1": {
				distancia_de_ventaja++;
				switch (distancia_de_ventaja) {

				case 0: System.out.println("Deuce");
				break;

				case 1: System.out.println("Ventaja P1");
				break;

				case 2: System.out.println("Ha ganado el P1");
					break;
				default:
					throw new IllegalArgumentException("Unexpected value: " + distancia_de_ventaja);
				}
				break;
			}
			case "P2":{
				distancia_de_ventaja--;
				switch (distancia_de_ventaja) {

				case 0: System.out.println("Deuce");
				break;

				case -1: System.out.println("Ventaja P2");
				break;
				
				case -2: System.out.println("Ha ganado el P2");
					break;

				default:
					throw new IllegalArgumentException("Unexpected value: " + distancia_de_ventaja);
				}

				break;	
			}
			default:
				throw new IllegalArgumentException("Unexpected value: " + distancia_de_ventaja);
			}
			iterador++;
		}
		ganador = true;
	}
	

}

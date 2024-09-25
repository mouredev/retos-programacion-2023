/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */
package reto_08_GeneradorPseudoAleatorio;

import java.time.LocalDateTime;
import java.util.Scanner;

public class IASR1987 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		//iniciamos el Scanner
		Scanner teclado = new Scanner(System.in);
		String respuesta="Y";
		String newNumero=" ";
		int contador=0;
		do {
			System.out.println("Quieres un número aleatorio");
			
			System.out.println(ObtenerNumeroAzar());
			
			System.out.println("Quieres otro Y/N");
		
			respuesta= teclado.nextLine();	
		}while(respuesta.equals("Y")||respuesta.equals("y"));
		
	}
	
	public static int ObtenerNumeroAzar() {
		// Obtener la fecha y hora actual con milisegundos
        LocalDateTime horaActual = LocalDateTime.now();
		
		int tiempoNano =  horaActual.getNano();
		
		int retorno=tiempoNano % 101;
		
		return retorno;
	}

}

/*
 ## Enunciado

```
/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

package reto_13_AdivinaLaPalabra;

import java.lang.reflect.Array;
import java.util.Scanner;

public class IASR1987 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		//arrays de palabras a adivinar
		 String[] palabras = {
		            "CASCADA", "RINOCERONTE", "AVIONETA", "AGUJERO", 
		            "MONTEVIDEO", "AUSTRALIA", "MURCIELAGO", "ELEFANTE", "BALLENA", 
		            "ZARIGUEYA", "DESPERTADOR", "ESCALERA", "AMAPOLA", "QUIRURGICO", 
		            "ORDENADOR", "TELEVISION", "FELICIDAD", "CONFIANZA", "JERUSALEN", 
		            "DELFIN", "UNIVERSIDAD", "MUSICA", "FERROCARRIL", "DINOSAURIO", 
		            "ESPACIO", "BIBLIOTECA", "HIPÓDROMO", "EXTINCION", "CONCIERTO", 
		            "PINTOR", "DELICATESEN", "QUINTA", "TORNADO", "ESPELEOLOGO", 
		            "ANESTESIA", "DICTADURA", "ARQUEOLOGO", "FARAON", "MAESTRANZA", 
		            "OBSERVATORIO", "EXTRATERRESTRE", "ELEFANTIASIS", "AERONAVE", "NEUROTICO", 
		            "JAGUAR", "ZAFARRANCHO", "POLINIZADOR", "ORGANICO", "QUIROMANCIA", 
		            "HIDROELECTRICIDAD", "SINFONIA", "EQUILATERO", "RADIOTELESCOPIO", "METEOROLOGIA"
		        };
		
		
		//se elige la palabra aleatroiamente
		int numeroAzar= (int)(Math.random()*palabras.length);
		String palabraElegida=palabras[numeroAzar];
				
		System.out.println("Bienvenido al juego de adivinar la palabra");
		System.out.println("------------------------------------------");
		
		//se calculan los guiones
		int guiones = guiones(palabraElegida);
		
		//se colocan en la palabra
		String palabraGuiones=mostrarLetras(palabraElegida,guiones);
		
		//la palabraGuiones la construimos como un StringBuilder que nos permite modificarlo caracter a caracter
		StringBuilder palabraSB = new StringBuilder(palabraGuiones);
		
		//pasamos la palabraElegida a char para poder buscar en ella
		char [] palabraEle= palabraElegida.toCharArray();
		
		//comprobar si la palabra es correcta
		boolean palabraCorrecta=false;
		//contabiliazar errores
		int errores =5;
				
		do {
			//se reinica en cada ciclo
			boolean letraCorrecta=false;
			
			System.out.println("1. Introduce una letra.");
			System.out.println("2. Adivina la palabra");
			System.out.println("RECUERDA USAR MAYÚSCULAS");
			int opcion = teclado.nextInt();
			//limpiar buffer
			teclado.nextLine();
			
			switch(opcion) {
			case 1:
				
				System.out.println("introduce una letra");
				//solo nos quedamos con la primera letra 
				char letra = teclado.nextLine().charAt(0);
				
				//recorremos la palabraElegida buscando coincidencias
				for(int i=0; i<palabraElegida.length();i++) {
					//si esxiste coincidencias
					if(palabraEle[i]==letra) {
						//sustituimos el guión por una letra(indica la posicion y el char)
						palabraSB.setCharAt(i, letra);
						letraCorrecta=true;
					}
					
				}
				
				if(letraCorrecta) {
					System.out.println("Has acertado");
					System.out.println(palabraSB);
				}else {
					errores--;
					System.out.println("Te quedan "+errores+" intentos.");
				}
				palabraCorrecta=comprobarPalabra(palabraElegida, palabraSB);
				
				break;
			case 2:
				String palabraTeclado;
				do {
					System.out.println("Adivina la palabra");
					palabraTeclado=teclado.nextLine();
					if(palabraElegida.length()!=palabraTeclado.length()) {
						System.out.println("Revisa la longitud de la palabra");
					}
				}while(palabraElegida.length()!=palabraTeclado.length());
				
				
				if(palabraTeclado.equals(palabraElegida)){
					palabraCorrecta=true;
				}else {
					errores--;
					System.out.println("Te quedan "+errores+" intentos.");
				}
				
				break;
	
			default:
				 System.out.println("Opción no válida. Por favor, elige 1 o 2.");
				 
				break;
		}
		
	}while(errores>0&&!palabraCorrecta);
		
		if(palabraCorrecta) {
			System.out.println("Has ganado el juego");
		}else{
			System.out.println("Has perdido el juego la palabra que buscabamos era "+ palabraElegida+".");
		}
		
	}

		//decidimos los guiones que tendrá la palabra
		public static int guiones(String palabraElegida) {
			
			//los guiones seran el 60 por cuiento de la palabra
	    	int guiones = (int) (palabraElegida.length()*0.6);
	    	
			return guiones;
		}
		
	 	// Ponemos guiones a la palabra
	    public static String mostrarLetras(String palabraElegida, int guiones) {
	        //palabra que retornarámos ya con guiones puestos
	    	String palabraGuiones="";
	        
	    	//colocamos los guiones a las palabrasb
	        if(guiones==palabraElegida.length()) {
	        	for(int i=0; i<palabraElegida.length(); i++) {
	        		palabraGuiones+="-";
	        	}
	        }else {
	        	//contador para contabilizar los guiones
	        	int contadorGuiones= 1;
	        	//palabraElegida se igual a la palabra Guiones para sustituir letras por valores
	        	palabraGuiones=palabraElegida;
	        	//pondremos tantos guiones como nos haya tocado
	        	while(contadorGuiones<=guiones) {
	        		//azar para el lugar de los guiones
	        		int posicionGuion =(int)(Math.random()*palabraElegida.length());
	        		
	        		//para colocar los guiones comprobando que ya no se ha colocado otro antes
	        		if(palabraGuiones.charAt(posicionGuion)!='-') {
	        			// Crea una nueva cadena con el carácter cambiado
	                    palabraGuiones = palabraGuiones.substring(0, posicionGuion) + '-' + palabraGuiones.substring(posicionGuion + 1);
	        			//borramos una en el contador de guiones de este modo
	        			contadorGuiones++;
	        			
	        		}
	        	}
	        }
	        
	        System.out.println(palabraGuiones);
	        
	        return palabraGuiones;
	   }
	    
	   public static boolean comprobarPalabra(String palabraElegida, StringBuilder palabra) {
		   boolean palabrasIguales;
		   
		   if(palabraElegida.equals(palabra.toString())) {
			   palabrasIguales=true;
		   }else {
			   palabrasIguales=false;
		   }
		   
		   return palabrasIguales;
	   }
}

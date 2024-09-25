/*
 * # Reto #15: Aurebesh
#### Dificultad: Fácil | Publicación: 10/04/23 | Corrección: 17/04/23

## Enunciado

```
/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *  
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */
package reto_15_Aurebesh;

import java.util.Scanner;

public class IASR1987 {
	public static void main(String[]args) {
		String[] alfabetoAurabesh ={"Aurek", "Besh", "Cresh", "Dorn", "Esk", "Forn", 
		"Grek", "Hesk", "Ithk", "Jenth", "Kesk", "Leth", "Mern", "Nern", "Osk", "Peth",
		"Qek", "Resh", "Sesk", "Tesh", "Usk", "Vev", "Wesk", "Xesh", "Yeveth", "Zesh"," "};
		char[] alfabeto = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
		'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '};
		
		//abrimos Scanner
		Scanner teclado=new Scanner(System.in);
		
		
		int opcion;
		
		do{
			
			String frase;
			
			System.out.println("1.- ESPAÑOL/AUREBESH");
			System.out.println("2.- AUREBESH/ESPAÑOL");
			System.out.println("3.- SALIR");
			opcion= teclado.nextInt();
			teclado.nextLine();
			String fraseTraducida="";
			
			if(opcion==1) {
				System.out.println("Introduce la frase");
				frase=teclado.nextLine().toUpperCase();
				char[] fraseChar= frase.toCharArray();
				
				for(int i=0; i<fraseChar.length; i++) {
					for(int j=0; j<alfabeto.length;j++) {
						if(fraseChar[i]==alfabeto[j]) {
							fraseTraducida+=alfabetoAurabesh[j]+" ";
						}
					}
				}
				System.out.println("FRASE TRADUCIDA "+fraseTraducida);
			
			}else if(opcion==2) {
				System.out.println("Introduce la frase");
				frase=teclado.nextLine();
				
				String[] palabrasAurebesh= frase.split(" ");
				
				for(int i=0; i<palabrasAurebesh.length; i++) {
					System.out.println(palabrasAurebesh[i]);
					for(int j=0; j<alfabetoAurabesh.length;j++) {
						if(palabrasAurebesh[i].equals(alfabetoAurabesh[j])) {
							fraseTraducida+=alfabeto[j];
						}
					}
				}
				
				System.out.println("FRASE TRADUCIDA "+fraseTraducida);
				
			}else {
				System.out.println("opcion incorrecta");
			}
						
		}while(opcion!=3);
	
		teclado.close(); // Cerrar el scanner
	}
}

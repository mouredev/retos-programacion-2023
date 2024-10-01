/*# Reto #20: La Trifuerza
#### Dificultad: Media | Publicación: 15/05/23 | Corrección: 22/05/23

## Enunciado

```
/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */
package reto_20_La_Trifuerza;

import java.util.Scanner;

public class IASR1987 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado= new Scanner(System.in);
		
		System.out.println("Indica el número de filas de nuestro triangulo");
		int n= teclado.nextInt();
		int alturaTotal=2*n;
		int asteriscos=1;
		int asteriscos2=1;
		int negativo=n*2-1;
		
		for(int i=0; i<2*n;i++) {
			
			if(i<n) {
				imprimirEspacios(alturaTotal);
				imprimirAsteriscos(asteriscos);
				asteriscos+=2;
				alturaTotal--;
				System.out.println(" ");
			}else {
				imprimirEspacios(alturaTotal);
				imprimirAsteriscos(asteriscos2);
				piramideInvertidaEspacios(negativo);
				imprimirAsteriscos(asteriscos2);
				asteriscos2+=2;
				alturaTotal--;
				negativo-=2;
				System.out.println(" ");
			}
		}
		
	}
	
	public static void imprimirEspacios(int alturaTotal) {
		for(int i=1; i<alturaTotal;i++) {
			System.out.print(" ");
		}
	}
	
	
	public static void imprimirAsteriscos(int asteriscos) {
		for(int j=0;j<asteriscos;j++) {
			System.out.print("*");
		}
		
	}
	
	public static void piramideInvertidaEspacios(int negativo) {
		for(int i=negativo; i>0;i--) {
			System.out.print(" ");
		}
	}
}


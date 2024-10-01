/*# Reto #16: La escalera
#### Dificultad: Media | Publicación: 17/04/23 | Corrección: 24/04/23

## Enunciado

```
/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 * 
 * Ejemplo: 4
 *         _
 *       _|       
 *     _|
 *   _|
 * _|
 * 
 */
package reto_16_laEscalera;

import java.util.Scanner;

public class IASR1987 {
		public static void main(String[] args) {
			// TODO Auto-generated method stub
			Scanner teclado = new Scanner(System.in);
			
			System.out.println("Introduce un número");
			int numero= teclado.nextInt();
			int contador;
		
			if(numero>0) {
				contador=numero*2;
						
				//escalera ascendente
				while(contador>=0) {
					espacios(contador,numero);
					if(contador==8) {
						System.out.println("_");
					}else {
						System.out.println("_|");
					}
					contador-=2;
				};

			}else if(numero<0) {
				//escalera descendente
				contador=1;
				int numeroAbs=Math.abs(numero)*2;
						
				while(contador<=numeroAbs) {
					
					
					
					if(contador==1) {
						System.out.println("_");
					}
					    espacios(contador,numero);	
						System.out.println("|_");
						contador+=2;
				}
			}else {
				System.out.println("__");
			}
			
			teclado.close();
		}
		
		public static void espacios(int contador, int numero) {
			if(numero>0) {
				while(contador>0) {
					System.out.print(" ");
					contador--;
				};
			}else {
				while(contador>0) {
					System.out.print(" ");
					contador--;
				}
			}
			
		}
	}


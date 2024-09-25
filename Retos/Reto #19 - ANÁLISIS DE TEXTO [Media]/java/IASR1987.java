/*# Reto #19: Análisis de texto
#### Dificultad: Media | Publicación: 11/05/23 | Corrección: 15/05/23

## Enunciado

```
/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
package reto_19_Analisis_de_Texto;

import java.util.Scanner;

public class IASR1987 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Introduce un texto");
		String texto=teclado.nextLine();
		//dividimos la frase 
		 // Realizar el split usando múltiples delimitadores (espacio,coma, punto y punto y coma)
		String[] palabras = texto.split("[\\s,;:.…]+");
        //numero total de palabras
        System.out.println("El texto contiene "+ palabras.length+ " palabras.");
        
        //variable se guarda la posicon de la palabra larga
        int palabraLarga=0;
        double sumaLetras=0;
        int contadorLetras=0;
        
        for(int i=0; i<palabras.length;i++) {
        	sumaLetras+=palabras[i].length();
        	
        	if(palabras[i].length()>contadorLetras) {
        		contadorLetras=palabras[i].length();
        		palabraLarga=i;      		
        	};
        }
    
        System.out.println("la media de las palabras es " +(sumaLetras/palabras.length)+ ".");
        //contabilizamos los puntos. Hay que tener en cuienta q el punto es carcater escape, por lo que debemos
        //poner las barras inclinadas\\
        String[] puntos = texto.split("\\.");
        System.out.println("El texto esta compuesto por "+ (puntos.length-1)+" oraciones.");
        System.out.println("la palabra más larga es "+ palabras[palabraLarga]);
        		
	}

}

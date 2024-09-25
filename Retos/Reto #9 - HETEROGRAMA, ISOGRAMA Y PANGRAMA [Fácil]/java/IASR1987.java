/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
package reto_09_heterogram_isograma_pangrama;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class IASR1987 {
	public static void main(String[] args) {
		//iniciamos el scanner
		Scanner teclado= new Scanner(System.in);
		
		//introducimos la palabra
		System.out.println("Introduce la palabra a analizar");
		String frase= teclado.nextLine();
		//convertimos la frase en minusculas
		frase = frase.toLowerCase();
		// Usar un conjunto para almacenar caracteres únicos
        Set<Character> ListaCaracteres = new HashSet<>();
        
        
		
		boolean heterograma=heterograma(frase,ListaCaracteres);
		
		if(heterograma==true) {
			System.out.println("La frase es un heterograma, ya que no se repite ninguna letra.");
		}else {
			System.out.println("La frase no es un heterograma. hay letras repetidas.");
		}
		
		boolean isograma= isograma(frase, heterograma, ListaCaracteres);
		
		if(isograma==true) {
			System.out.println("La frase es un isograma, las letras se repiten las misma veces, 1 vez todas o 2 veces todas.");
		}else {
			System.out.println("La frase no es un isograma.");
		}
		
		boolean pangrama=pangrama(frase);
		if(pangrama==true) {
			System.out.println("La frase es un pangrama, contiene todas las letras del alfabeto español.");
		}else {
			System.out.println("La frase no es un pangrama, no contiene todas las letras del alfabeto español.");
		}
		
		//cerramos el scanner
		teclado.close();
	}
	
	public static boolean heterograma(String frase, Set<Character> ListaCaracteres) {
		//si retorna true la frase es un heterograma
		boolean retorno=true;
        
        
        //guardar cada caracter en ListaCaracteres
        for(int i=0; i<frase.length() && retorno==true;i++) {
        	if(frase.charAt(i)!=' ') {
        		if(ListaCaracteres.contains(frase.charAt(i))==false) {
        			ListaCaracteres.add(frase.charAt(i));
        		}else {
        			retorno=false;
        		}
   
        	}
        }
		
		return  retorno;
	}
	
	public static boolean isograma(String palabra, boolean heterograma, Set<Character> ListaCaracteres) {
		//si retorna true la frase es un heterograma
		boolean retorno=true;
		
		//siempre que es heterograma es isograma
		if(heterograma==true) {
			retorno=true;
		}else {
			//creamos un mapa para almacenar las veces que van apareciendo;
			Map<Character, Integer> contadorApariciones = new HashMap<>();
			
			//introducimos los caracteres en el mapa
			for(Character c: ListaCaracteres) {
				contadorApariciones.put(c, 0);
			};
			
			//recorremos la frase, debemos convertirla en un array de char
			for(Character c: palabra.toCharArray()) {
				if(contadorApariciones.containsKey(c)) {
					contadorApariciones.put(c, contadorApariciones.get(c)+1);
				}
			}
			
			//comparamos los valores del mapa, como tienen que ser todos iguales pues cogemos el primero como referencia.
			int contador=0;
			int valorReferencia=0;
			for(Integer c : contadorApariciones.values()) {
				if(contador==0) {
					valorReferencia=c;
					contador++;
				}else {
					if(valorReferencia!=c) {
						retorno=false;
					}
				}
			}
			
		}
		
		return  retorno;
	}
	public static boolean pangrama(String frase) {
		boolean retorno=false;
		List<Character> abecedario = new ArrayList<>(Arrays.asList('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
				 'l', 'm','n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'));
		List<Boolean> letrasEncontradas = new ArrayList<>(Arrays.asList(false, false, false, false, false, false, false,
	                false, false, false, false, false, false, false, false, false, false, false, false, false, false,
	                false, false, false, false, false, false));
		
		
		int contador=0;
		//introducimos la frase en el mapa
		for(int i=0; i<frase.length();i++) {
			for(int j=0;j<abecedario.size();j++) {
				if(abecedario.get(j).compareTo(frase.charAt(i))==0 && !letrasEncontradas.get(j)) {
					letrasEncontradas.set(j, true);
					contador++;
				}
			}	
		}
		
		if(contador==27) {
			retorno=true;
		}
		
		return  retorno;
	}
}

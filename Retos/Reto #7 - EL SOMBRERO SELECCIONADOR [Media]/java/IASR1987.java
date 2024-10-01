/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
package reto_07_Sombrero_Seleccionador;

import java.util.Scanner;

public class IASR1987 {
	public static void main(String [] args) {
		
		//abrimos scanner
		Scanner teclado= new Scanner(System.in);
		//contadores por casa
		int Gryffindor =0;
		int Hufflepuf=0;
		int Ravenclaw=0;
		int Slytherin=0;
		//controlamos las respuestas incorrectas
		boolean respuestaIncorrecta=true;
		
		while( respuestaIncorrecta==true) {
			System.out.println("¿Cuál de las siguientes cualidades valoras más en un amigo?");
			System.out.println("1. Valentía.");
			System.out.println("2. Lealtad.");
			System.out.println("3. Inteligencia.");
			System.out.println("4. Ambición.");
			String respuesta= teclado.nextLine();
			switch(respuesta) {
			case "1":
				Gryffindor++;
				respuestaIncorrecta=false;
				break;
			case "2":
				Hufflepuf++;
				respuestaIncorrecta=false;
				break;
			case "3":
				Ravenclaw++;
				respuestaIncorrecta=false;
				break;
			case "4":
				Slytherin++;
				respuestaIncorrecta=false;
				break;
			default:
				System.out.println("Respuesta incorrecta, intentalo de nuevo");
				break;
			}
				
		}
		
		//reiniciamos respuestaIncorrecta
		respuestaIncorrecta=true;
		
		while( respuestaIncorrecta==true) {
			System.out.println("¿Qué criatura mágica te resulta más fascinante?");
			System.out.println("1. El Fénix.");
			System.out.println("2.  El Puffskein.");
			System.out.println("3. El Águila Calva .");
			System.out.println("4.  El Basilisco.");
			String respuesta= teclado.nextLine();
			switch(respuesta) {
			case "1":
				Gryffindor++;
				respuestaIncorrecta=false;
				break;
			case "2":
				Hufflepuf++;
				respuestaIncorrecta=false;
				break;
			case "3":
				Ravenclaw++;
				respuestaIncorrecta=false;
				break;
			case "4":
				Slytherin++;
				respuestaIncorrecta=false;
				break;
			default:
				System.out.println("Respuesta incorrecta, intentalo de nuevo");
				break;
			}
				
		}
		
		//reiniciamos respuestaIncorrecta
		respuestaIncorrecta=true;
				
		while( respuestaIncorrecta==true) {
			System.out.println("En un grupo de trabajo, ¿qué rol prefieres asumir?");
			System.out.println("1. El líder que toma decisiones.");
			System.out.println("2.  El que apoya y colabora con todos.");
			System.out.println("3. El que investiga y aporta ideas innovadoras.");
			System.out.println("4. El estratega que planea cómo alcanzar el objetivo.");
			String respuesta= teclado.nextLine();
			switch(respuesta) {
			case "1":
				Gryffindor++;
				respuestaIncorrecta=false;
				break;
			case "2":
				Hufflepuf++;
				respuestaIncorrecta=false;
				break;
			case "3":
				Ravenclaw++;
				respuestaIncorrecta=false;
				break;
			case "4":
				Slytherin++;
				respuestaIncorrecta=false;
				break;
			default:
				System.out.println("Respuesta incorrecta, intentalo de nuevo");
				break;
			}
				
		}
		
		//reiniciamos respuestaIncorrecta
		respuestaIncorrecta=true;
		
		while( respuestaIncorrecta==true) {
			System.out.println("¿Cuál de las siguientes materias te interesa más?");
			System.out.println("1. Defensa Contra las Artes Oscuras.");
			System.out.println("2. Herbología .");
			System.out.println("3. Aritmancia .");
			System.out.println("4. Pociones .");
			String respuesta= teclado.nextLine();
			switch(respuesta) {
			case "1":
				Gryffindor++;
				respuestaIncorrecta=false;
				break;
			case "2":
				Hufflepuf++;
				respuestaIncorrecta=false;
				break;
			case "3":
				Ravenclaw++;
				respuestaIncorrecta=false;
				break;
			case "4":
				Slytherin++;
				respuestaIncorrecta=false;
				break;
			default:
				System.out.println("Respuesta incorrecta, intentalo de nuevo");
				break;
			}
				
		}
		
		//reiniciamos respuestaIncorrecta
		respuestaIncorrecta=true;
				
		while( respuestaIncorrecta==true) {
			System.out.println("Si te encuentras con una situación difícil, ¿cómo reaccionas?");
			System.out.println("1. Enfrentándola con coraje.");
			System.out.println("2. Buscando la forma más justa de resolverla.");
			System.out.println("3.  Analizando todas las posibles soluciones.");
			System.out.println("4. Utilizando cualquier medio necesario para superarla.");
			String respuesta= teclado.nextLine();
			switch(respuesta) {
			case "1":
				Gryffindor++;
				respuestaIncorrecta=false;
				break;
			case "2":
				Hufflepuf++;
				respuestaIncorrecta=false;
				break;
			case "3":
				Ravenclaw++;
				respuestaIncorrecta=false;
				break;
			case "4":
				Slytherin++;
				respuestaIncorrecta=false;
				break;
			default:
				System.out.println("Respuesta incorrecta, intentalo de nuevo");
				break;
			}
				
		}
		
		
		if(Gryffindor>Hufflepuf && Gryffindor>Ravenclaw && Gryffindor>Slytherin) {
			System.out.println("Uhmmmmmmm. eres un Gryffindor");
		}else if(Hufflepuf>Gryffindor && Hufflepuf>Ravenclaw && Hufflepuf>Slytherin) {
			System.out.println("Uhmmmmmmm. eres un Hufflepuf");
		}else if(Ravenclaw>Gryffindor && Ravenclaw>Hufflepuf && Ravenclaw>Slytherin) {
			System.out.println("Uhmmmmmmm. eres un Ravenclaw");
		}else {
			System.out.println("Uhmmmmmmm. eres un Slytherin");
		}
	}		
}


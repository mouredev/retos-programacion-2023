package challenge_45;

import java.util.Random;
import java.util.Scanner;

public class Challenge_45 {
	
	public static void main (String[]args) {
		
		Scanner read = new Scanner(System.in);
		Random alea = new Random();
		
		int id;
		String participantes[];
		String accion, nombre;
		boolean cerrar = false;
        
        participantes = new String [0];
		
		while (!cerrar) {
			System.out.print("Indica la acción que deseas realizar: ");
			accion = read.nextLine();
			System.out.println();
			switch (accion) {
				case "añadir":
					System.out.print("\tIntroduce el nombre del participante que deseas añadir: ");
					nombre = read.nextLine();
					System.out.println();
					id = buscarParticipante(participantes,nombre);
					if(id<0) {
				        participantes = añadirParticipante(participantes, nombre);
						System.out.println("\t\tParticipante añadido");
					} else {
						System.out.println("\t\tEl participante ya existe!");
					}
					break;
				case "borrar":
					System.out.print("\tIntroduce el nombre del participante que deseas borrar: ");
					nombre = read.nextLine();
					System.out.println();
					id = buscarParticipante(participantes,nombre);
					if(id<0) {
						System.out.println("\t\tEl participante no existe!");
					} else {
						participantes = borrarParticipante(participantes,id);
						System.out.println("\t\tParticipante borrado");
					}
					break;
				case "mostrar":
					System.out.println("\tEste es el listado de participantes: \n");
					for(id = 0; id<participantes.length; id++) {
						System.out.println("\t\t"+participantes[id]);
					}
					break;
				case "sorteo":
					id = alea.nextInt(0,participantes.length);
					System.out.println("\t"+participantes[id]);
					participantes = borrarParticipante(participantes,id);
					break;
				case "salir":
					System.out.println();
					System.out.println("Cerrando el programa...");
					cerrar = true;
					break;
				default:
					System.out.println("Acción incorrecta!!");
			}
			System.out.println();
		}
	}
	static String[] añadirParticipante(String[] myArray, String newElement) {
	       //we create a new Object here, an array of bigger capacity
	       String[] array = new String[myArray.length + 1];
	       System.arraycopy(myArray, 0, array, 0, myArray.length);
	       array[myArray.length] = newElement;
	       return array;
	   }
	static int buscarParticipante(String [] participantes, String nombre) {
		int id;
		for(id = 0; id<participantes.length; id++) {
			if(participantes[id].equals(nombre)) {
				return id;
			}
		}
		return -1;
	}
	static String[] borrarParticipante(String [] participantes, int id) {
		while(id<participantes.length-1) {
			participantes[id]=participantes[id+1];
			id++;
		}
		String[] array = new String[participantes.length - 1];
	    System.arraycopy(participantes, 0, array, 0, participantes.length-1);
	    return array;
	}
}
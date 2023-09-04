import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Random;
import java.util.Set;



public class Elez95 {
	
	
	public static void main(String [] args) {
		
		//variable tipo String
		String tipoString = "Elez95";
		//variable tipo numérico entero
		int numEntero = 10;	
		//variable tipo numérico decimal
		double numDecimal = 15.5;
		//variable tipo booleano
		boolean flag = true;
		//dato constante
		String DATO_CONSTANTE = "ROJO";
		
		
		//- Bloque if-else if- else
		if(numEntero > numDecimal) {
			System.out.println("El número entero es mayor al número decimal");
		}
		else if(numEntero < numDecimal) {
			System.out.println("El número entero es menor al número decimal");			
		}
		else
			System.out.println("El número entero es igual al número decimal");
		
		
		//- Bloque array
		String[] colores = new String[7];
		colores[0] = DATO_CONSTANTE;
		colores[1] = "VERDE";
		
		
		//- Bloque lista
		LinkedList <Integer> numerosPrimos = new LinkedList<>();
		numerosPrimos.add(2);
		numerosPrimos.add(3);
		numerosPrimos.add(5);
		numerosPrimos.get(1);
		//numerosPrimos.remove(0);
		
		
		//- Bloque Set
		Set<Integer> ids = new HashSet<>();
		ids.add(12990878);
		ids.add(45984332);
		ids.remove(12990878);
		
		
		//- Bloque diccionario
		HashMap<Integer,String> dorsales = new HashMap<>();
		dorsales.put(1, "Dibu Martinez");
		dorsales.put(10, "Leonel Messi");
		dorsales.get(1);
		dorsales.remove(1);
		
		
		//- Bloque for
		for(int iterador = 0; iterador > 10; iterador++) {
			
			System.out.println("Iteración número " + iterador);
			
		}
		
		
		//- Bloque for each
		for (Integer iteradorForEach : numerosPrimos) {
			System.out.println(iteradorForEach + " ");
		}
		
		
		//- Bloque while
		Random random = new Random();
		while(flag) {
			if(random.nextInt(0,5) == 3) { //toma un número aleatorio, y si es igual a 3, el flag true pasa a falso
				flag = false;
			}
		}
			
		
	}
	
	//- Función sin parámetro/sin retorno
	public static void saludo() {
		System.out.println("Hola, esta es mi primera contribución");
	}
	
	
	//- Función con parámetro/sin retorno
	public static void saludo_personalizado(String nombre) {
		System.out.println("Hola " + nombre);
	}

	
	//- Función con parámetros/con retorno
	public static boolean es_par(int numero) {
		if(numero % 2 == 0) {
			return true;
		}else
			return false;
	}
	
	
	//- Función sin parámetros/con retorno
	public static int dorsal_de_jugador_aleatorio() {
		Random random = new Random();
		return random.nextInt(1,23);
	}
	
 
	//control de excepciones
	public static void control_excepciones(int algunNumero) {
		
		if(algunNumero < 0) {
			throw new IllegalArgumentException("No se pueden elegir números negativos");
		}
		else
			System.out.println("El número es " + algunNumero);
		
	}
	
	//- Creación de clase
	class Persona {

		private int id;
		private int edad;
		private String nombre;

		Persona(int id, int edad, String nombre){
			this.id = id;
			this.edad = edad;
			this.nombre = nombre;
		}
	}
}


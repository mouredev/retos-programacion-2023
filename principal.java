public class Principal {
	public static void main(String[] args) {
		/*
		 * Escribe un programa que muestre por consola (con un print) los
		 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
		 * cada impresión), sustituyendo los siguientes:
		 * - Múltiplos de 3 por la palabra "fizz".
		 * - Múltiplos de 5 por la palabra "buzz".
		 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
		 */
		
		//Planteamiento del ejercicio de otra manera ya que todo el munndo lo hara de la misma mannera.
		String fizz,buzz;
		for(int i=1;i<=100;i++){
			fizz="";
			buzz="";
			if(i%3==0){
				fizz="fizz";
			}
			if(i%5==0){
				buzz="buzz";
			}
			if(buzz=="" && fizz=="") {
				System.out.println(i);
			}else {
				System.out.println(fizz+buzz);
			}
		}
	}
}

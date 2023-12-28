import java.util.Scanner; // Importamos paquete para la clase Scanner

public class Reto1_LenguajeHacker {

	public static void main(String[] args) {
		
		// ---------------------------
		//   DECLARACION DE VARIABLES
		// ----------------------------

		// Variables de Entrada
		String texto = "";
		
		// Variables Auxiliares
		int longitudTexto;
		char caracter=' ';
		
		// Constructor clase Scanner
		Scanner src = new Scanner (System.in);

		// ---------------------------
		//       ENTRADA DE DATOS
		// ----------------------------
		System.out.println("Inserte el texto a transformar en lenguaje hacker.");
		texto = src.nextLine(); // objeto con el texto incluido
		
		// ---------------------------
		//        PROCESAMIENTO
		// ----------------------------
		// Preparativos
		longitudTexto=texto.length();
		
		 // Bucle for que recorra cada letra del texto
		for (int i = 0; i<longitudTexto; i++) { // bucle for para recorrer cada caracter del texto
			caracter = texto.charAt(i);	
			if (caracter >='0' && caracter <='9') {
				switch (caracter) {
					case '0': 
						System.out.print("o");
						break; 
					case '1': 
						System.out.print("L");
						break; 
					case '2': 
						System.out.print("R");
						break; 
					case '3': 
						System.out.print("E");
						break; 
					case '4': 
						System.out.print("A");
						break; 
					case '5': 
						System.out.print("S");
						break; 
					case '6': 
						System.out.print("b");
						break; 
					case '7': 
						System.out.print("T");
						break; 
					case '8': 
						System.out.print("B");
						break; 
					case '9': 
						System.out.print("g");
						break; 
				}
				
			} else if (caracter>='a'&& caracter<='z'||caracter>='A'&& caracter<='Z') { // condicion letras
				switch (caracter) {
					case 'a','A': 
						System.out.print(4);
						break; 
					case 'b', 'B':
						System.out.print("l"+3);
						break;
					case 'c','C': 
						System.out.print("[");
						break; 
					case 'd','D': 
						System.out.print(")");
						break; 
					case 'e','E': 
						System.out.print(3);
						break; 
					case 'f','F': 
						System.out.print("|=");
						break; 
					case 'g','G': 
						System.out.print("&");
						break; 
					case 'h','H': 
						System.out.print("#");
						break; 
					case 'i','I': 
						System.out.print(1);
						break; 
					case 'j','J': 
						System.out.print(",_|");
						break; 
					case 'l','L': 
						System.out.print(1);
						break; 
					case 'm','M': 
						System.out.print("/\\/\\");
						break; 
					case 'n','N': 
						System.out.print("^/");
						break; 
					case 'o','O': 
						System.out.print(0);
						break; 
					case 'p','P': 
						System.out.print("|*");
						break; 
					case 'q','Q': 
						System.out.print("_,");
						break; 
					case 'r','R': 
						System.out.print("|"+2);
						break; 
					case 's','S': 
						System.out.print(5);
						break; 
					case 't','T': 
						System.out.print(7);
						break; 
					case 'u','U': 
						System.out.print("(_)");
						break; 
					case 'v','V': 
						System.out.print("\\/");
						break; 
					case 'w','W': 
						System.out.print("\\/\\/");
						break; 
					case 'x','X': 
						System.out.print("><");
						break; 
					case 'y','Y': 
						System.out.print("j");
						break; 
					case 'z','Z': 
						System.out.print(2);
						break; 
					}
				
			} else {
				System.out.print(caracter); // para signos de puntuación, espaciados y otros caracteres distintos a alfanuméricos
			}
			
		} // cierre for
		
	} // cierre método main

} // cierre clase

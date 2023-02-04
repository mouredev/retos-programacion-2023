
import java.util.Scanner;

public class Reto4_VerificacionNumeroPrimoFibonacciPar {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		// ---------------------------
		//   DECLARACION DE VARIABLES
		// ----------------------------

		// Array
		int [] fibonacci = {0,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597}; 

		// Variables de Entrada
		int numeroIntroducido;
		
		// Variables de Salida
		String primo = "", textoFibonacci = "", par = "";
		
		// Variables Auxiliares
		int contador = 0, posicion;
		boolean fibo = false;
		
		// Constructor Clase Scanner
		Scanner src = new Scanner(System.in);
		
		// ---------------------------
		//       ENTRADA DE DATOS
		// ----------------------------
		
		System.out.println("Por favor, introduzca un número entero.");
		numeroIntroducido = src.nextInt();
		src.nextLine();
		
		// ---------------------------
		//        PROCESAMIENTO
		// ----------------------------
		
		//Comprobacion primo (resto cero cuando se dividen por el mismo o 1
		
		for (int i = 1; i<1599; i++) {
			if (numeroIntroducido % i == 0)
				contador++;
		}
		primo = (contador == 2) ? " es primo" :  " no es primo";		
		
		// comprobación Fibonacci
		for (int i = 0; i <17 && fibo==false ;i++) {
			posicion = fibonacci [i];
			if (numeroIntroducido == posicion) {
				textoFibonacci = "es fibonacci";
				fibo = true;
			} else {
				textoFibonacci = "no es fibonacci";
				fibo = false;
			}
		}
		
		// Comprobación par (resto cero al dividir entre 2)
		par = (numeroIntroducido % 2 == 0) ? "es par" : "no es par";
		
		// ---------------------------
		//        SALIDA DE DATOS
		// ----------------------------
    
		System.out.println("//// VERIFICACIÓN DE NÚMEROS ////");
		System.out.println("---------------------------------");
		System.out.println(numeroIntroducido + primo +", "+ textoFibonacci + " y " + par + ".");
	}

}

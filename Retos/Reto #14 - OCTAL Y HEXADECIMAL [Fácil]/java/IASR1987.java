/*# Reto #14: Octal y Hexadecimal
#### Dificultad: Fácil | Publicación: 03/04/23 | Corrección: 10/04/23

## Enunciado

```
/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
package reto_14_Octal_Hexadecimal;

import java.util.Scanner;

public class IASR1987 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Introduce un número");
		int decimal= teclado.nextInt();
		System.out.println("OCTAL: "+octal(decimal));
		System.out.println("HEXADECIMAL: "+hexadecimal(decimal));
	}
	
	public static String octal(int decimal) {
		int octal;
		String octalS="";
		
		//De decimal a octal
		do {
			//esta división nos dará el dividendo, se irá relaizando hasta que sea menor de 8
			octal=decimal/8;
			//nos dará los digitos del octal, teniendo en cuenta que primero vendrá el ultimo valor, por ello tendremos
			//que darle la vuelta
			octalS += String.valueOf(decimal%8);
			decimal=octal;
			//si es menor de 8 significa que el dividendo ya no se puede dividir por 8, este dígito será
			//el primero de nuestro numero octal.
			if(octal<8) {
				octalS += octal;
			}
		}while(octal>=8);
		
		//necesidad de darle la vuelta
		String retorno = new StringBuilder(octalS).reverse().toString();
		return retorno;
	}
	
	public static String hexadecimal(int decimal) {
		int hexadecimal;
		String hexadecimalS="";
		
		//se repite la dinamica del anterior método
		do {
			hexadecimal=decimal/16;
			//calcular el modulo teniendo en cuenta que 10 es A, 11 es B; etc
			int modulo=decimal%16;
			
			if(modulo>9) {
				if(modulo==10) {
					hexadecimalS += "A";
				}else if(modulo==11) {
					hexadecimalS += "B";
				}else if(modulo==12) {
					hexadecimalS += "C";
				}else if(modulo==13) {
					hexadecimalS += "D";
				}else if(modulo==14) {
					hexadecimalS += "E";
				}else{
					hexadecimalS += "F";
				}
			}else {
				hexadecimalS += String.valueOf(modulo);
			}
			
			decimal=hexadecimal;
			if(hexadecimal<16&&hexadecimal>0) {
				hexadecimalS += hexadecimal;
			}
		}while(hexadecimal>=16);
		
		//necesidad de darle la vuelta
		String retorno = new StringBuilder(hexadecimalS).reverse().toString();
		return retorno;
	}

}

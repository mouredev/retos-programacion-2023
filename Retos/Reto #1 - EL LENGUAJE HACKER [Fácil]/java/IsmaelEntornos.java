package reto_01_LenguajeHacker;

import java.util.Scanner;

public class IsmaelEntornos {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		char lista[] = {' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
				  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
				  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
		String leet[] = {" ","4", "l3", "[", ")", "3",".=","&&","-","1",",.","-","1","/A./",
				   "-/","0","-*","(a,)","l2","5","7","(o)","-/","-/","-","j","2",
				   "o","L","R","E","A","S","b","T","B","g"};
		System.out.println("Introduce una frase para traducirla a lenguaje");
		String frase= teclado.nextLine();
		
		boolean letraEncontrada;
		
		for(int i=0; i<frase.length();i++) {
			letraEncontrada=false;
			for(int j=0; j<=lista.length && letraEncontrada==false;j++) {
				if(frase.charAt(i)==lista[j]) {
					letraEncontrada=true;
					System.out.print(leet[j]);
				};
			}
		}
		
	}

}

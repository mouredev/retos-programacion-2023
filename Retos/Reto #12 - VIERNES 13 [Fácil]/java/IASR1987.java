package reto_12_Viernes_13;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Scanner;

public class IASR1987 {
	public static void main(String[] args) {
		
		Scanner teclado = new Scanner(System.in);
		
		System.out.println("Introduce el mes");
		int mes= teclado.nextInt();
		System.out.println("Introduce el año");
		int anno = teclado.nextInt();
		
		
		LocalDate fechaBusqueda = LocalDate.of(anno,mes,13) ;
		//obtenemos el dia de la semana
		DayOfWeek comprobarDia = fechaBusqueda.getDayOfWeek();
		
		//podemos o comprobar por el valor
		//o por (comprobarDia==DayOfWeek.FRIDAY)
		if(comprobarDia.getValue()==5) {
			System.out.println("VERDADERO");
		}else {
			System.out.println("FALSO");
		}
	    System.out.println("Hoy es: " + comprobarDia);
		
	}
	
	/*
	 * Definición de los días de la semana:
La clase DayOfWeek define siete constantes, una para cada día de la semana:

    DayOfWeek.MONDAY
    DayOfWeek.TUESDAY
    DayOfWeek.WEDNESDAY
    DayOfWeek.THURSDAY
    DayOfWeek.FRIDAY
    DayOfWeek.SATURDAY
    DayOfWeek.SUNDAY

Métodos útiles:

    getValue(): Devuelve un valor entero del 1 al 7 correspondiente al día de la semana, donde 1 es lunes y 7 es domingo.
    plus(long days): Devuelve el día de la semana sumando un número específico de días, ajustándose cíclicamente dentro de la semana.
    minus(long days): Devuelve el día de la semana restando un número específico de días, ajustándose cíclicamente dentro de la semana.*/
}

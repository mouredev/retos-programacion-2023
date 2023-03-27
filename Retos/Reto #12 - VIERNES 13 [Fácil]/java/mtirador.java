import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Scanner;

public class mtirador {

	public static void main(String[] args) {

		
			
			Scanner ent=new Scanner(System.in);
			int anio=0;
			int mes=0;
		
			System.out.println("Ingresa el anioo: ");
			anio=ent.nextInt();
			System.out.println("Ingresa el mes: ");
			mes=ent.nextInt();
			
			LocalDate fecha=LocalDate.of(anio, mes, 13);
			
			if(fecha.getDayOfWeek()== DayOfWeek.FRIDAY) {
				System.out.println("Existe un viernes 13, en el anio y mes ingresados");
			}else {
				System.out.println("No lo hay");
			}
			
			
			
	}//fin main

}//fin class

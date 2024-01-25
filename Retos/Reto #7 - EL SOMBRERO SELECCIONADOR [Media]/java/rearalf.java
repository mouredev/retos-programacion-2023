package com.example.myfirstproject;

import java.util.Scanner;

public class MyFirstProjectApplication {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int repeat = 0;

		do {
			int griffindor = 0;
			int hufflepuff = 0;
			int ravenclaw = 0;
			int slytherin = 0;
			String option = "";

			System.out.println("");
			System.out.println("");
			System.out.println(
					"Bienvenid@ a Hogwarts!. El sombrero seleccionador.");

			System.out.println("");

			System.out.println("1. ¿Qué rasgo te caracteriza más?");
			System.out.println("a. Valentía");
			System.out.println("b. Lealtad");
			System.out.println("c. Creatividad");
			System.out.println("d. Astucia");

			option = sc.nextLine();
			switch (option) {
				case "a":
					griffindor++;
					break;
				case "b":
					hufflepuff++;
					break;
				case "c":
					ravenclaw++;
					break;
				case "d":
					slytherin++;
			}

			System.out.println("2. ¿Dónde te gustaría que estuviera tu casa común?");
			System.out.println("a. Mazmorras");
			System.out.println("b. Torre del colegio");
			System.out.println("c. En una sala amplia");
			System.out.println("d. Bodega");
			option = sc.nextLine();
			switch (option) {
				case "a":
					griffindor++;
					break;
				case "b":
					hufflepuff++;
					break;
				case "c":
					ravenclaw++;
					break;
				case "d":
					slytherin++;
			}

			System.out.println("3. ¿Como actúas ante una injusticia?");
			System.out.println("a. Solo actúas si está involucrado algún amigo o familiar");
			System.out.println("b. Defiendes con valentía lo que crees justo sea quien sea");
			System.out.println("c. Defiendes la justicia pero no haces mucho ruido");
			System.out.println("d. Actúas solo si sacas un beneficio propio");
			option = sc.nextLine();
			switch (option) {
				case "a":
					griffindor++;
					break;
				case "b":
					hufflepuff++;
					break;
				case "c":
					ravenclaw++;
					break;
				case "d":
					slytherin++;
			}

			System.out.println("4. ¿Qué eligirias de mascota?");
			System.out.println("a. Araña");
			System.out.println("b. Suricato");
			System.out.println("c. Lechuza");
			System.out.println("d. Gato");
			option = sc.nextLine();
			switch (option) {
				case "a":
					griffindor++;
					break;
				case "b":
					hufflepuff++;
					break;
				case "c":
					ravenclaw++;
					break;
				case "d":
					slytherin++;
			}

			System.out.println("5. ¿Qué clase te interesa más?");
			System.out.println("a. Artes Oscuras");
			System.out.println("b. Adivinación");
			System.out.println("c. Herbolistería");
			System.out.println("d. Transformaciones");
			option = sc.nextLine();
			switch (option) {
				case "a":
					griffindor++;
					break;
				case "b":
					hufflepuff++;
					break;
				case "c":
					ravenclaw++;
					break;
				case "d":
					slytherin++;
			}

			if (griffindor > hufflepuff && griffindor > slytherin && griffindor > ravenclaw) {
				System.out.println("GRIFFINDOR!!!!!!!!");
			}
			if (hufflepuff > griffindor && hufflepuff > slytherin && hufflepuff > ravenclaw) {
				System.out.println("HUFFLEPUFF!!!!!!!!");
			}
			if (ravenclaw > griffindor && ravenclaw > slytherin && ravenclaw > hufflepuff) {
				System.out.println("RAVENCLAW!!!!!!!!");
			}
			if (slytherin > griffindor && slytherin > ravenclaw && slytherin > hufflepuff) {
				System.out.println("SSSSSSLYTHERIN!!!!!!!!");
			}

			System.out.println("Desea continuar (1 = si): ");
			repeat = sc.nextInt();

		} while (repeat == 1);

		sc.close();
	}
}

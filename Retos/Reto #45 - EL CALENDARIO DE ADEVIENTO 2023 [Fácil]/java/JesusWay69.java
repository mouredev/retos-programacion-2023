package reto_45;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
 * ¿Conoces el calendario de aDEViento de la comunidad?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su newName y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el newName no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar 
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
 */
public class JesusWay69 {

    public static void main(String[] args) {
        List<String> contestants = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        String num;
        boolean flag = true;

        while (flag) {

            System.out.println("\nMenú Principal");
            System.out.println("----------------\n");
            System.out.println("Elija una opción: \n");
            System.out.print("0: Salir - ");
            System.out.print("1: Añadir participante - ");
            System.out.print("2: Borrar participante - ");
            System.out.print("3: Mostrar participantes - ");
            System.out.print("4: Lanzar sorteo\n");

            num = sc.nextLine();

            if (num.matches("[0-4]") == false) {
                System.out.println("\nSólo se pueden elegir opciones del 0 al 5");
            }

            int winner = 0;

            switch (num) {

                case "0":
                    flag = false;
                    break;

                case "1":
                    System.out.print("introduzca nombre a añadir: ");

                    String newName = sc.nextLine().toUpperCase();
                    if (!contestants.contains(newName)) {
                        contestants.add(newName);
                    } else {
                        System.out.println("\nEl nombre ya existe, escriba otro diferente\n");
                    }

                    break;

                case "2":
                    System.out.print("introduzca nombre a borrar: ");
                    String deleteName = sc.next().toUpperCase();
                    sc.nextLine();

                    if (contestants.contains(deleteName)) {
                        contestants.remove(deleteName);
                        System.out.println("El concursante " + deleteName + " se ha eliminado de la lista");
                        break;

                    } else System.out.println("El nombre " + deleteName + " no está en la lista");
                    
                    break;

                case "3":
                    System.out.println("Lista de participantes: \n");
                    for (int i = 0; i < contestants.size(); i++) {
                        String contestant = contestants.get(i);
                        System.out.println(contestant);

                    }
                    break;

                case "4":
                    if (!contestants.isEmpty()) {
                        winner = (int) (Math.random() * contestants.size());
                        System.out.println("Es ganador es....." + contestants.get(winner));
                        contestants.remove(winner);
                    } else System.out.println("\nNo hay concursantes para realizar el sorteo");

                    break;

            }

        }

    }

}

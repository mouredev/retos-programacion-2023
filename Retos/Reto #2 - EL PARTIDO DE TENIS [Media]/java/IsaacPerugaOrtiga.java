import java.util.Scanner;

public class Main {


    public static void main(String[] args) {

        int p1 = 0;
        int p2 = 0;
        String game;
        boolean gameOn = true;

        Scanner sc = new Scanner(System.in);

        //Puntuaran p1 si el String es igual a "P1" y punturará p2 si el String es igual a "P2"
        System.out.println("Empieza el partido: ");

        do {
            game = sc.nextLine();

            if (game.equals("P1")) {
                p1++;
            } else if (game.equals("P2")) {
                p2++;
            }

            if (p1 == 1 && p2 == 0) {
                System.out.println("15 - Love");
            } else if (p1 == 0 && p2 == 1) {
                System.out.println("Love - 15");
            } else if (p1 == 1 && p2 == 1) {
                System.out.println("15 - 15");
            } else if (p1 == 2 && p2 == 1) {
                System.out.println("30 - 15");
            } else if (p1 == 1 && p2 == 2) {
                System.out.println("15 - 30");
            } else if (p1 == 2 && p2 == 2) {
                System.out.println("30 - 30");
            } else if (p1 == 3 && p2 == 2) {
                System.out.println("40 - 30");
            } else if (p1 == 2 && p2 == 3) {
                System.out.println("30 - 40");
            } else if (p1 == 0 && p2 == 3) {
                System.out.println("Love - 40");
            } else if (p1 == 0 && p2 == 2) {
                System.out.println("Love - 30");
            } else if (p1 == 2 && p2 == 0) {
                System.out.println("30 - Love");
            } else if (p1 == 3 && p2 == 0) {
                System.out.println("40 - Love");
            } else if (p1 == 3 && p2 == 1) {
                System.out.println("40 - 15");
            } else if (p1 == 4 && p2 == 1) {
                System.out.println("P1 gana el partido");
                gameOn = false;
            } else if (p1 == 4 && p2 == 2) {
                System.out.println("P1 gana el partido");
                gameOn = false;
            } else if (p1 == 1 && p2 == 4) {
                System.out.println("P2 gana el partido");
                gameOn = false;
            } else if (p1 == 2 && p2 == 4) {
                System.out.println("P2 gana el partido");
                gameOn = false;
            } else if (p1 == 4 && p2 == 0) {
                System.out.println("P1 gana el partido");
                gameOn = false;
            } else if (p1 == 0 && p2 == 4) {
                System.out.println("P2 gana el partido");
                gameOn = false;
            }


            if (p1 == 3 && p2 == 3) {
                System.out.println("Deuce");
            } else if (p1 == 4 && p2 == 3) {
                System.out.println("Ventaja para P1");
            } else if (p1 == 3 && p2 == 4) {
                System.out.println("Ventaja para P2");
            } else if (p1 == 4 && p2 == 4) {
                System.out.println("Deuce");
                p1 = 3;
                p2 = 3;
            } else if (p1 == 5 && p2 == 3) {
                System.out.println("P1 gana el partido");
                gameOn = false;
            } else if (p1 == 3 && p2 == 5) {
                System.out.println("P2 gana el partido");
                gameOn = false;
            }

        } while (gameOn);

    }
}

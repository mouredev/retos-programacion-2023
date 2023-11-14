//18/04/2023 Reto #16 (Java)
//Jordi Beltrà

import java.util.Scanner;

class Escalera {

    //Definir los métodos
    public static void DibujarEscalera(int x) {
        if (x == 0) {
            System.out.println("__");
        } else if (x < 0) {
            System.out.println("_");
            for (int i = 0; i <= Math.abs(x) - 1; i++) {
                System.out.println(" ".repeat(i + 1) + " ".repeat(i) + "|_");
            }
        } else {
            System.out.println(" ".repeat(x * 2 + 2) + "_");
            for (int i = 0; i <= x - 1; i++) {
                System.out.println(" ".repeat(x - i) + " ".repeat(x - i) + "_|");
            }
        }
    }

    //Loop
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int input = sc.nextInt();
            DibujarEscalera(input);
        }
    }
}

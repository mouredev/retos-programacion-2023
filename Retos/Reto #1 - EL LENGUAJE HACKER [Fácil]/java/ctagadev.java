package Reto1;

/***
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 * se caracteriza por sustituir caracteres alfanuméricos.
 * Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 * con el alfabeto y los números en "leet".
 * (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 *
 * @author CtagaDev
 */

import java.util.Scanner;

public class CtagaDev {
    public static void main(String[] args) {
        int i;
        Scanner input = new Scanner(System.in);
        System.out.println("Conversor lenguaje humano a lengua leet.");
        System.out.print("Introduce el texto a convertir: ");
        String human = input.nextLine().toLowerCase();

        for (i = 0; i < human.length(); i++) {
            switch (human.charAt(i)) {
                case 'a' -> System.out.print("4");
                case 'b' -> System.out.print("I3");
                case 'c' -> System.out.print("[");
                case 'd' -> System.out.print(")");
                case 'e' -> System.out.print("3");
                case 'f' -> System.out.print("|=");
                case 'g' -> System.out.print("&");
                case 'h' -> System.out.print("#");
                case 'i' -> System.out.print("1");
                case 'j' -> System.out.print(",_|");
                case 'k' -> System.out.print(">|");
                case 'l' -> System.out.print("£");
                case 'm' -> System.out.print("/\\/\\");
                case 'n' -> System.out.print("^/");
                case 'o' -> System.out.print("0");
                case 'p' -> System.out.print("|*");
                case 'q' -> System.out.print("(_,)");
                case 'r' -> System.out.print("I2");
                case 's' -> System.out.print("5");
                case 't' -> System.out.print("7");
                case 'u' -> System.out.print("(_)");
                case 'v' -> System.out.print("\\/");
                case 'w' -> System.out.print("\\/\\/");
                case 'x' -> System.out.print("><");
                case 'y' -> System.out.print("j");
                case 'z' -> System.out.print("2");
                case '1' -> System.out.print("L");
                case '2' -> System.out.print("R");
                case '3' -> System.out.print("E");
                case '4' -> System.out.print("A");
                case '5' -> System.out.print("S");
                case '6' -> System.out.print("b");
                case '7' -> System.out.print("T");
                case '8' -> System.out.print("B");
                case '9' -> System.out.print("g");
                case '0' -> System.out.print("o");
                default -> System.out.print(human.charAt(i));
            }
        }
        input.close();
    }
}
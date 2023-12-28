package com.company;
import java.util.Scanner;

public class reto1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Por favor escriba una frase en mayúscula: ");
        String frase = sc.nextLine();
            frase = frase.replaceAll("A", "4").replaceAll("B", "8").replaceAll("C", "<").replaceAll("D", ">").replaceAll("E", "3").replaceAll("F", "|=").replaceAll("G", "6").replaceAll("H", "#").replaceAll("I", "1")
                    .replaceAll("J", ",_|").replaceAll("K", "|<").replaceAll("L", "|_").replaceAll("M", "[V]").replaceAll("N", "^/").replaceAll("O", "0").replaceAll("P", "|*").replaceAll("Q", "(_,)").replaceAll("R", "|^")
                    .replaceAll("S", "5").replaceAll("T", "7").replaceAll("U", "(_)").replaceAll("V", "|/").replaceAll("W", "VV").replaceAll("X", "><").replaceAll("Y", "`/").replaceAll("Z", "7_");
        System.out.println(frase);
    }
}

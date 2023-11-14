package org.classroom;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        String[] abacus = {
                "O---OOOOOOOO",
                "OOO---OOOOOO",
                "---OOOOOOOOO",
                "OO---OOOOOOO",
                "OOOOOOO---OO",
                "OOOOOOOOO---",
                "---OOOOOOOOO"};

        System.out.println(readAbacus(abacus));

    }

    public static String readAbacus(String[] abacus) {
        StringBuilder result = new StringBuilder();
        Arrays.stream(abacus).forEach(row -> result.append(calculateRow(row)));
        return String.format("%,d",Integer.parseInt(result.toString()));
    }

    public static String calculateRow(String row) {
        return String.valueOf(row.indexOf('-'));
    }
}
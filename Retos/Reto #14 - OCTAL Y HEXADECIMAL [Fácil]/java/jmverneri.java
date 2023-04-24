package reto14OctalHexadecimal;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class jmverneri {
    public static void main(String[] args) {
        int octal = decimalToOctal(451);
        String hex = decimalToHexa(451);
        System.out.println("El numero en Octal: " + octal);
        System.out.println("El numero en Hexadecimal: " + hex);
    }

    public static int decimalToOctal(Integer number) {
        int octal;
        List<String> totalNumber = new ArrayList<>();
        String numberToReturn = "";

        while (number >= 8) {
            totalNumber.add(Integer.toString(number % 8));
            number = number / 8;
        }

        numberToReturn += Integer.toString(number);

        for (int i = totalNumber.size() - 1; i >= 0; i--) {
            numberToReturn = numberToReturn + totalNumber.get(i);
        }

        octal = Integer.parseInt(numberToReturn);

        return octal;
    }

    public static String decimalToHexa(Integer number) {

        List<String> totalNumber = new ArrayList<>();
        String numberToReturn = "";
        Map<Integer, String> numbersMap = new HashMap<>();

        numbersMap.put(10,"A");
        numbersMap.put(11,"B");
        numbersMap.put(12,"C");
        numbersMap.put(13,"D");
        numbersMap.put(14,"E");
        numbersMap.put(15,"F");

        while (number >= 16) {
            if((number % 16) >= 10) {
                totalNumber.add(numbersMap.get(number % 16));
            }
            else
                totalNumber.add(Integer.toString(number % 16));
            number = number / 16;
        }

        numberToReturn += Integer.toString(number);

        for (int i = totalNumber.size() - 1; i >= 0; i--) {
            numberToReturn = numberToReturn + totalNumber.get(i);
        }

        return numberToReturn;
    }
}
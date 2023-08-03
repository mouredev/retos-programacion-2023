import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        int decimal = josepmonclus.getNumber();

        
        String octal = josepmonclus.doDecimalToOctal(decimal);

        String hexa = josepmonclus.doDecimalToHexadecimal(decimal);

        System.out.println("Decimal => " + decimal);
        System.out.println("Octal => " + octal);
        System.out.println("Hexadecimal => " + hexa);
    }

    private String doDecimalToOctal(int decimal) {
        Map<Integer, String> octal = new HashMap<>();
        octal.put(0, "0");
        octal.put(1, "1");
        octal.put(2, "2");
        octal.put(3, "3");
        octal.put(4, "4");
        octal.put(5, "5");
        octal.put(6, "6");
        octal.put(7, "7");

        List<Integer> convertedDigits = convertDecimalTo(8, decimal);

        StringBuilder sb = new StringBuilder();

        for(int i = convertedDigits.size() - 1; i >= 0; i--) {
            int digit = convertedDigits.get(i);

            sb.append(octal.get(digit));
        }

        return sb.toString();
    }

    private String doDecimalToHexadecimal(int decimal) {
        Map<Integer, String> hexadecimal = new HashMap<>();
        hexadecimal.put(0, "0");
        hexadecimal.put(1, "1");
        hexadecimal.put(2, "2");
        hexadecimal.put(3, "3");
        hexadecimal.put(4, "4");
        hexadecimal.put(5, "5");
        hexadecimal.put(6, "6");
        hexadecimal.put(7, "7");
        hexadecimal.put(8, "8");
        hexadecimal.put(9, "9");
        hexadecimal.put(10, "A");
        hexadecimal.put(11, "B");
        hexadecimal.put(12, "C");
        hexadecimal.put(13, "D");
        hexadecimal.put(14, "E");
        hexadecimal.put(15, "F");

        List<Integer> convertedDigits = convertDecimalTo(16, decimal);

        StringBuilder sb = new StringBuilder();

        for(int i = convertedDigits.size() - 1; i >= 0; i--) {
            int digit = convertedDigits.get(i);

            sb.append(hexadecimal.get(digit));
        }

        return sb.toString();
    }

    private List<Integer> convertDecimalTo(int base, int decimal) {
        List<Integer> digits = new ArrayList<>();

        if(decimal < base){
            digits.add(decimal);
        } else {
            int divisor = 0;

            do {
                divisor = decimal / base;

                int resto = decimal % base;
                digits.add(resto);

                decimal = divisor;
            } while (divisor > 0);
        }

        return digits;
    }

    private int getNumber() {
        int decimal = 0;

        System.out.println("CONVERSOR DECIMAL -> OCTAL y HEXADECIMAL");
        System.out.println("___________________________________________");

        boolean validNumber = false;
        while(!validNumber) {
            System.out.println("Introduce el número para su conversión:");

            try{
                decimal = Integer.parseInt(entrada.nextLine());

                validNumber = true;
            } catch(Exception e) {
                System.out.println("Número introducido no válido!");
                validNumber = false;
            }
        }

        return decimal;
    }
}

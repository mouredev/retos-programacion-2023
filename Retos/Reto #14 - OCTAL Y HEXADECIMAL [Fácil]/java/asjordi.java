import java.util.HashMap;
import java.util.Map;

public class ConvertOctalAndHexadecimal {

    public int convertDecimalToOctal(int decimalNumber){
        int quotient = decimalNumber;
        int remainder;
        StringBuilder octalResult = new StringBuilder();

        if (decimalNumber == 0) return 0;

        while (quotient > 0) {
            remainder = quotient % 8;
            octalResult.append(remainder);
            quotient = quotient / 8;
        }

        return Integer.parseInt(octalResult.reverse().toString());
    }

    public String convertDecimalToHexadecimal(int decimalNumber){
        Map<Integer, Character> hexMap = createHexMap();
        StringBuilder hexadecimalResult = new StringBuilder();

        while (decimalNumber > 0) {
            int remainder = decimalNumber % 16;
            hexadecimalResult.append(hexMap.get(remainder));
            decimalNumber = decimalNumber / 16;
        }

        return hexadecimalResult.reverse().toString();
    }

    private static Map<Integer, Character> createHexMap() {
        Map<Integer, Character> hexMap = new HashMap<>();
        hexMap.put(0, '0');
        hexMap.put(1, '1');
        hexMap.put(2, '2');
        hexMap.put(3, '3');
        hexMap.put(4, '4');
        hexMap.put(5, '5');
        hexMap.put(6, '6');
        hexMap.put(7, '7');
        hexMap.put(8, '8');
        hexMap.put(9, '9');
        hexMap.put(10, 'A');
        hexMap.put(11, 'B');
        hexMap.put(12, 'C');
        hexMap.put(13, 'D');
        hexMap.put(14, 'E');
        hexMap.put(15, 'F');
        return hexMap;
    }

}

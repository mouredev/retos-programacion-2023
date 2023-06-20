import java.util.Arrays;
import java.util.Scanner;

public class danieldrv8 {
    public static int convertDecimal2Octal(int n) {
        if (n < 8) {
            return n;
        } else {
            int[] restArr = new int[0];
            int rest = 0;
            int quotient = n;
            while (quotient > 7) {
                rest = quotient % 8;
                quotient = quotient / 8;
                restArr = Arrays.copyOf(restArr, restArr.length + 1);
                restArr[restArr.length - 1] = rest;
            }
            restArr = Arrays.copyOf(restArr, restArr.length + 1);
            restArr[restArr.length - 1] = quotient;
            //Da la vuelta al array
            int[] reversedArr = new int[restArr.length];
            for (int i = 0; i < restArr.length; i++) {
                reversedArr[i] = restArr[restArr.length - 1 - i];
            }
            restArr = reversedArr;
            //Convierte el array a int
            String str = "";
            for (int i = 0; i < restArr.length; i++) {
                str += Integer.toString(restArr[i]);
            }
            int result = Integer.parseInt(str);
            return result;
        }
    }
    public static String convertDec2Hex(int n) {
        if (n < 15) {
            return chngUnit(n);
        } else {
            int[] restArr = new int[0];
            int rest = 0;
            int quotient = n;
            while (quotient > 15) {
                rest = quotient % 16;
                quotient = quotient / 16;
                restArr = Arrays.copyOf(restArr, restArr.length + 1);
                restArr[restArr.length - 1] = rest;
            }
            restArr = Arrays.copyOf(restArr, restArr.length + 1);
            restArr[restArr.length - 1] = quotient;
            String str = "";
            for (int i = 0; i < restArr.length; i++) {
                str += chngUnit(restArr[restArr.length - 1 - i]);
            }
            return str;
        }
    }
    public static String chngUnit(int n) {
        if (n < 10) {
            return ""+n;
        } else {
            switch (n) {
                case 10:
                    return "A";
                case 11:
                    return "B";
                case 12:
                    return "C"; 
                case 13:
                    return "D";
                case 14:
                    return "E";
                case 15:
                    return "F";               
                default:
                    return "";
            }
        } 
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce un número decimal: ");
        int num = sc.nextInt();
        System.out.println("Número convertido a octal: " + convertDecimal2Octal(num));
        System.out.println("Número convertido a hexadecimal: " + convertDec2Hex(num));
        sc.close();
    }
}
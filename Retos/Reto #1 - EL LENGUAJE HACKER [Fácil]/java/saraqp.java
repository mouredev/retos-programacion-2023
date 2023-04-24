import java.util.Scanner;

public class saraqp {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        String userString;
        System.out.print("Introduce una frase a transformar a 'lenguaje hacker': ");
        userString = sc.nextLine();
        do {
            System.out.println("Frase escrita: "+userString+"\nTransformada: "+ transformString(userString)+"\nSi no desea continuar escriba 0 para salir, de lo contrario, escriba otra frase");
            userString = sc.nextLine();
        }while (!userString.equals("0"));


    }
    private static String transformString(String string){
        StringBuilder userStringTransform= new StringBuilder();
        for (int i =0;i<string.length();i++){
            char charact=string.charAt(i);
            switch (charact) {
                case 'a', 'A' -> userStringTransform.append("4");
                case 'b', 'B' -> userStringTransform.append("I3");
                case 'c', 'C' -> userStringTransform.append("[");
                case 'd', 'D' -> userStringTransform.append(")");
                case 'e', 'E' -> userStringTransform.append("3");
                case 'f', 'F' -> userStringTransform.append("ƒ");
                case 'g', 'G' -> userStringTransform.append("&");
                case 'h', 'H' -> userStringTransform.append("#");
                case 'i', 'I' -> userStringTransform.append("1");
                case 'j', 'J' -> userStringTransform.append(";");
                case 'k', 'K' -> userStringTransform.append(">|");
                case 'l', 'L' -> userStringTransform.append("|");
                case 'm', 'M' -> userStringTransform.append("^^");
                case 'n', 'N' -> userStringTransform.append("^/");
                case 'o', 'O' -> userStringTransform.append("0");
                case 'p', 'P' -> userStringTransform.append("|*");
                case 'q', 'Q' -> userStringTransform.append("&");
                case 'r', 'R' -> userStringTransform.append("Я");
                case 's', 'S' -> userStringTransform.append("5");
                case 't', 'T' -> userStringTransform.append("7");
                case 'u', 'U' -> userStringTransform.append("v");
                case 'v', 'V' -> userStringTransform.append("\\/");
                case 'w', 'W' -> userStringTransform.append("Щ");
                case 'x', 'X' -> userStringTransform.append("Ж");
                case 'y', 'Y' -> userStringTransform.append("Ч");
                case 'z', 'Z' -> userStringTransform.append("2");
                case '0' -> userStringTransform.append("()");
                case '1' -> userStringTransform.append("I");
                case '2' -> userStringTransform.append("Z");
                case '3' -> userStringTransform.append("E");
                case '4' -> userStringTransform.append("A");
                case '5' -> userStringTransform.append("S");
                case '6' -> userStringTransform.append("G");
                case '7' -> userStringTransform.append("T");
                case '8' -> userStringTransform.append("B");
                case '9' -> userStringTransform.append("q");
                default -> userStringTransform.append(charact);
            }
        }
        return userStringTransform.toString();
    }
}

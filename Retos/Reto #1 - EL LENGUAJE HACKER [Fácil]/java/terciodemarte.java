import java.util.Scanner;
public class terciodemarte {
    public static void main(String[] args) {

        Scanner lectura = new Scanner(System.in);
        System.out.println("Dime la palabra para traduccir a lenguaje Hacker");
        String palabra = lectura.nextLine();

        String diccionario[] = new String[]{"4", "I3", "[", ")", "3", "|=", "&", "#", "1",
            ",_|", ">|", "1", "^^", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "|/", "2u",
            "><", "j", "2", "L", "R", "E", "A", "S", "b", "T", "B", "g", "o"};

        System.out.println("La palabra en lenguaje Hacker");
        for (int i = 0; i < palabra.length(); i++) {
            switch (palabra.toLowerCase().charAt(i)) {
                case 'a' ->System.out.print(diccionario[0]);
                case 'b' ->System.out.print(diccionario[1]);
                case 'c' ->System.out.print(diccionario[2]);
                case 'd' ->System.out.print(diccionario[3]);
                case 'e' ->System.out.print(diccionario[4]);
                case 'f' ->System.out.print(diccionario[5]);
                case 'g' ->System.out.print(diccionario[6]);
                case 'h' ->System.out.print(diccionario[7]);
                case 'i' ->System.out.print(diccionario[8]);
                case 'j' ->System.out.print(diccionario[9]);
                case 'k' -> System.out.print(diccionario[10]);
                case 'l' -> System.out.print(diccionario[11]);
                case 'm' -> System.out.print(diccionario[12]);
                case 'n' -> System.out.print(diccionario[13]);
                case 'o' -> System.out.print(diccionario[14]);
                case 'p' -> System.out.print(diccionario[15]);
                case 'q' -> System.out.print(diccionario[16]);
                case 'r' -> System.out.print(diccionario[17]);
                case 's' -> System.out.print(diccionario[18]);
                case 't' -> System.out.print(diccionario[19]);
                case 'u' -> System.out.print(diccionario[20]);
                case 'v' -> System.out.print(diccionario[21]);
                case 'w' -> System.out.print(diccionario[22]);
                case 'x' -> System.out.print(diccionario[23]);
                case 'y' -> System.out.print(diccionario[24]);
                case 'z' -> System.out.print(diccionario[25]);
                case '1' -> System.out.print(diccionario[26]);
                case '2' -> System.out.print(diccionario[27]);
                case '3' -> System.out.print(diccionario[28]);
                case '4' -> System.out.print(diccionario[29]);
                case '5' -> System.out.print(diccionario[30]);
                case '6' -> System.out.print(diccionario[31]);
                case '7' -> System.out.print(diccionario[32]);
                case '8' -> System.out.print(diccionario[33]);
                case '9' -> System.out.print(diccionario[34]);
                case '0' -> System.out.print(diccionario[35]);
            }
        }
    }
}

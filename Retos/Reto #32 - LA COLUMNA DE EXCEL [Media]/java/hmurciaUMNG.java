import java.util.Scanner;

public class hmurciaUMNG {

    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);
        String colName = "";
        do {
            System.out.print("Nombre de columna: ");
            colName = scn.nextLine();
            colName = colName.toUpperCase();
        } while (!colName.matches("[A-Z]|[A-Z]{2}|[A-X]{1}[A-F]{1}[A-D]{1}"));
        System.out.println("Nombre columna: " + colName + " y su numero de posicion es "
            + posAsciiChar(colName));
    }

    private static int posAsciiChar(String str) {
        int pos = 0, len = str.length();
        for (int i = 0; i < len; i++) {
            pos += Math.pow(26, len - i - 1) * (str.charAt(i) - '@');
        }
        return pos;
    }
}
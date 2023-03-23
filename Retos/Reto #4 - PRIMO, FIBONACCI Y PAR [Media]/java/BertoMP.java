import java.util.Scanner;

public class reto04_PrimoFibonacciPar {
    public static void main(String[] args) {
        Scanner scEntrada = new Scanner(System.in);

        int intNum;
        String strParImpar;
        String strPrimo;
        String strFibo;

        System.out.print("Dime un número: ");
        intNum = scEntrada.nextInt();
        scEntrada.close();
        
        strPrimo = esPrimo(intNum) ? " es primo," : " no es primo,";
        strFibo = esFibonnacci(intNum) ? " es fibonacci y" : " no es fibonacci y";
        strParImpar = esPar(intNum) ? " es par." : " es impar.";

        System.out.println("El número " + intNum + strPrimo + strFibo + strParImpar);

    }

    private static boolean esPar(int intNum) {
        return intNum % 2 == 0;
    }

    private static boolean esPrimo(int intNum) {
        if (intNum == 0 || intNum == 1) {
            return false;
        }
        for (int intCont = 2; intCont < intNum / 2; intCont++) {
            if (intNum % intCont == 0)
                return false;
        }

        return true;
    }

    private static boolean esFibonnacci(int intNum) {
        int intFibo1 = 0;
        int intFibo2 = 1;
        int intAuxiliar;

        while (intFibo1 + intFibo2 <= intNum) {
            intAuxiliar = intFibo1;
            intFibo1 = intFibo2;
            intFibo2 = intAuxiliar + intFibo1;
            if (intNum == intFibo2) {
                return true;
            }
        }
        return false;
    }
}

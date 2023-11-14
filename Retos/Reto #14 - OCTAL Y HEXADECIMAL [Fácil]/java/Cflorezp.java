package reto14OctalHexadecimal;

import java.util.HashMap;
import java.util.Scanner;

/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
public class Cflorezp {

    public static void main(String[] args) {

        System.out.println("Convertidor de números decimales a Octal y a Hexadecimal");
        System.out.println("*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n");
        System.out.println("Por favor digite el numero que desea convertir: ");
        Scanner input = new Scanner(System.in);
        if (input.hasNextInt()) {
            int numero = input.nextInt();
            System.out.println("El numero decimal es: " + numero);
            System.out.println("El numero representado en octal es: " + decimalAOctal(numero));
            System.out.println("El numero representado en hexadecimal es: " + decimalAHexadecimal(numero));
        } else {
            System.out.println("El valor ingresado no es numérico.");
        }
        input.close();

    }


    public static int decimalAOctal(int numeroAConvertir) {
        String resultado = "";
        int residuo, cociente;
        residuo = numeroAConvertir % 8;
        cociente = numeroAConvertir / 8;
        resultado += residuo;
        for (int i = 0; i < numeroAConvertir; i++) {
            if (cociente > 7) {
                residuo = cociente % 8;
                cociente = cociente / 8;
                resultado += residuo;
            } else {
                resultado += cociente;
                break;
            }
        }
        String invertida = new StringBuilder(resultado).reverse().toString();
        return Integer.parseInt(invertida);
    }

    public static String decimalAHexadecimal(int numeroAConvertir){
        HashMap<Integer, String> tablaHex = new HashMap<>();
        tablaHex.put(0, "0");
        tablaHex.put(1, "1");
        tablaHex.put(2, "2");
        tablaHex.put(3, "3");
        tablaHex.put(4, "4");
        tablaHex.put(5, "5");
        tablaHex.put(6, "6");
        tablaHex.put(7, "7");
        tablaHex.put(8, "8");
        tablaHex.put(9, "9");
        tablaHex.put(10, "A");
        tablaHex.put(11, "B");
        tablaHex.put(12, "C");
        tablaHex.put(13, "D");
        tablaHex.put(14, "E");
        tablaHex.put(15, "F");

        String resultado = "";
        int residuo, cociente;
        residuo = numeroAConvertir % 16;
        cociente = numeroAConvertir / 16;
        resultado += residuo;
        for (int i = 0; i < numeroAConvertir; i++) {
            if (cociente > 15) {
                residuo = cociente % 16;
                cociente = cociente / 16;

                resultado += tablaHex.get(residuo);
            } else {
                resultado += tablaHex.get(cociente);
                break;
            }
        }
        return new StringBuilder(resultado).reverse().toString();
    }
}

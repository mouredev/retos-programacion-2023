/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import java.util.Scanner;

public class reto03_ElGeneradorDeContrasenas {
    public static void main(String[] args) {
        inicio();
    }

    private static String desordenaContrasena(String strContrasena) {
        char[] chrArrCaracteres;
        int intNumeroAleatorio;
        char chrAux;
        chrArrCaracteres = strContrasena.toCharArray();

        for (int intCont = 0; intCont < chrArrCaracteres.length; intCont++) {
            intNumeroAleatorio = (int) (Math.random() * chrArrCaracteres.length);
            chrAux = chrArrCaracteres[intCont];
            chrArrCaracteres[intCont] = chrArrCaracteres[intNumeroAleatorio];
            chrArrCaracteres[intNumeroAleatorio] = chrAux;
        }

        strContrasena = String.valueOf(chrArrCaracteres);

        return strContrasena;
    }

    private static String rellenaContrasena(int intLetrasMayus, int intLetrasMinus, int intNumeros, int intSimbolos) {
        int intNumeroAleatorio;
        String strReturn = "";

        final char[] chrArrLetrasMinusculas = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        final char[] chrArrLetrasMayusculas = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
        final char[] chrArrNumeros = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
        final char[] chrArrSimbolos = {'!', '#', '$', '%', '&', '(', ')', '*', '+'};

        for (int intCont = 0; intCont < intLetrasMayus; intCont++) {
            intNumeroAleatorio = (int) (Math.random() * chrArrLetrasMayusculas.length);
            strReturn += chrArrLetrasMayusculas[intNumeroAleatorio];
        }

        for (int intCont = 0; intCont < intNumeros; intCont++) {
            intNumeroAleatorio = (int) (Math.random() * chrArrNumeros.length);
            strReturn += chrArrNumeros[intNumeroAleatorio];
        }

        for (int intCont = 0; intCont < intSimbolos; intCont++) {
            intNumeroAleatorio = (int) (Math.random() * chrArrSimbolos.length);
            strReturn += chrArrSimbolos[intNumeroAleatorio];
        }

        for (int intCont = 0; intCont < intLetrasMinus; intCont++) {
            intNumeroAleatorio = (int) (Math.random() * chrArrLetrasMinusculas.length);
            strReturn += chrArrLetrasMinusculas[intNumeroAleatorio];
        }

        return strReturn;
    }

    private static int defineLongitud(Scanner scEntrada) {
        int intLongitud;

        System.out.print("Dime la longitud de contraseña que quieres, el mínimo es 8 y el máximo es 16: ");
        intLongitud = scEntrada.nextInt();

        while (intLongitud < 8 || intLongitud > 16) {
            System.out.println("ERROR! Longitud no válida.");
            System.out.print("Dime la longitud de contraseña que quieres, el mínimo es 8 y el máximo es 16: ");
            intLongitud = scEntrada.nextInt();
        }

        return intLongitud;
    }

    private static void inicio() {
        Scanner scEntrada = new Scanner(System.in);

        String strContrasena = "";
        int intLongitud;
        int intLetrasMayus;
        int intNumeros;
        int intSimbolos;
        int intCaracteresTotales;
        int intLetrasMinus;

        intLongitud = defineLongitud(scEntrada);

        System.out.print("¿Cuántas mayúsculas quieres? ");
        intLetrasMayus = scEntrada.nextInt();

        System.out.print("¿Cuántos números quieres? ");
        intNumeros = scEntrada.nextInt();

        System.out.print("¿Cuántos símbolos quieres? ");
        intSimbolos = scEntrada.nextInt();
        scEntrada.close();

        intCaracteresTotales = intLetrasMayus + intNumeros + intSimbolos;

        if (intCaracteresTotales > intLongitud) {
            System.out.println("Los parámetros ingresados son mayores que la longitud definida al inicio");
        } else {
            intLetrasMinus = intLongitud - intCaracteresTotales;
            strContrasena = rellenaContrasena(intLetrasMayus, intLetrasMinus, intNumeros, intSimbolos);
            strContrasena = desordenaContrasena(strContrasena);
        }

        System.out.println(strContrasena);
    }
}

package reto12Viernes13;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Scanner;

/*
 * Programa que detecta si existe un viernes 13 en el mes y el año indicados.
 */
public class Cflorezp {

    public static void main(String[] args) {

        System.out.print("Bienvenido\nPara determinar si el mes del año indicado por usted tiene un viernes 13,\n");

        int anio = validaAnio();
        int mes = validaMes();

        if (hayViernes13(anio, mes)) {
            System.out.println("El mes " + mes + " del año " + anio + " tiene viernes 13");
        } else {
            System.out.println("El mes " + mes + " del año " + anio + " no tiene viernes 13");
        }

    }

    /**
     * Funcion principal que devuelve true si el mes tiene un viernes 13 de lo contrario devuelve false
     */
    public static boolean hayViernes13(int anio, int mes) {
        LocalDate actual = LocalDate.of(anio, mes, 13);
        DayOfWeek dia = actual.getDayOfWeek();
        String nombre = dia.name();
        return nombre.equals("FRIDAY") ? true : false;
    }

    public static int validaAnio() {
        int flag = 0;
        int numero = 0;
        String valor;
        Scanner entradaAnio = new Scanner(System.in);
        do {
            System.out.println("por favor ingrese el año: ");
            valor = entradaAnio.nextLine();
            numero = validaSiEsNumero(valor) ? Integer.parseInt(valor) : 0;
            if (numero > 2999 || numero < 1) {
                System.out.println("!!El año que usted ingreso no es valido!!");
            } else {
                flag = 1;
            }
        } while (flag == 0);
        return numero;
    }

    public static int validaMes() {
        int flag = 0;
        int numero = 0;
        String valor;
        Scanner entradaMes = new Scanner(System.in);
        do {
            System.out.println("por favor ingrese el mes: ");
            valor = entradaMes.nextLine();
            numero = validaSiEsNumero(valor) ? Integer.parseInt(valor) : 0;
            if (numero > 12 || numero < 1) {
                System.out.println("!!El mes que usted ingreso no es valido!!");
            } else {
                flag = 1;
            }
        } while (flag == 0);
        return numero;
    }

    public static boolean validaSiEsNumero(String input) {
        try {
            int num = Integer.parseInt(input);
        } catch (NumberFormatException e) {
            return false;
        }
        return true;
    }
}

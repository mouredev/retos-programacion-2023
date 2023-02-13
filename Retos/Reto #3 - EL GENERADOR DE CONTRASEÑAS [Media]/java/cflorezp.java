package reto3GeneradorDeContrasenas;

import java.util.Scanner;

public class cflorezp {

    public static void main(String[] args) {
        System.out.println("\nLa contraseña generada es: " + generaPassword());
    }

    public static int generaAletaorio8a16() {
        int numero = (int) (Math.random() * (16 - 8 + 1) + 8);
        return numero;
    }

    public static String generaPassword(){
        System.out.println("***** GENERADOR DE CONTRASEÑAS *****\n");
        int opciones = 1;
        Scanner input = new Scanner(System.in);
        System.out.println("Desea incluir mayusculas? Y/N: ");
        String value2 = input.nextLine();
        if(value2.equals("Y") || value2.equals("y")) opciones++;

        System.out.println("Desea incluir numeros? Y/N: ");
        String value3 = input.nextLine();
        if(value3.equals("Y") || value3.equals("y")) opciones++;

        System.out.println("Desea incluir simbolos? Y/N: ");
        String value4 = input.nextLine();
        if(value4.equals("Y") || value4.equals("y")) opciones++;

        int longitudPassword = generaAletaorio8a16();
        int[] combinaciones = posiblesCombinaciones(longitudPassword, opciones);

        char[] cadenaMinusculas = generaCaracteresRandom(generaMinusculas(), combinaciones[0]);
        String password = new String(cadenaMinusculas);

        if(combinaciones.length > 1){
            for(int i = 1; i < combinaciones.length; i++){
                if(value2.equals("Y") || value2.equals("y")){
                    char[] cadenaMayusculas = generaCaracteresRandom(generaMayusculas(), combinaciones[i]);
                    value2 = "ok";
                    password += new String(cadenaMayusculas);
                    continue;
                }
                if(value3.equals("Y") || value3.equals("y")){
                    char[] cadenaNumeros = generaCaracteresRandom(generaNumeros(), combinaciones[i]);
                    value3 = "ok";
                    password += new String(cadenaNumeros);
                    continue;
                }
                if(value4.equals("Y") || value4.equals("y")){
                    char[] cadenaSimbolos = generaCaracteresRandom(generaSimbolos(), combinaciones[i]);
                    value4 = "ok";
                    password += new String(cadenaSimbolos);
                }
            }
        }
        return desordenarString(password);
    }

    public static char[] generaCaracteresRandom(char[] caracteres, int longitud) {
        char[] result = new char[longitud];
        for (int i = 0; i < longitud; i++) {
            int position = (int) (Math.random() * caracteres.length);
            result[i] = caracteres[position];
        }
        return result;
    }

    public static int[] posiblesCombinaciones(int longitud, int combinaciones) {
        int[] result = new int[combinaciones];
        longitud = longitud - combinaciones;
        for (int i = combinaciones - 1; i >= 0; i--) {
            result[i] = 1;
            int provisional = 0;
            if (longitud > 0) {
                if (i == 0) {
                    result[i] += longitud;
                } else {
                    int max = (int) (longitud / i);
                    provisional = (int) (Math.random() * max + 1);
                    result[i] += provisional;
                }
            }
            longitud -= provisional;
        }
        return result;
    }

    public static String desordenarString(String cadena){
        int azar = 0;
        String resultado = "";
        for(int i = cadena.length(); i >= 2; i--){
            azar = (int)(Math.random() * i + 1);
            resultado = resultado + cadena.substring(azar - 1, azar);
            cadena = cadena.substring(0, azar - 1) + cadena.substring(azar, i);
        }
        return resultado + cadena;
    }

    public static char[] generaMinusculas() {
        char[] minusculas = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        return minusculas;
    }

    public static char[] generaMayusculas() {
        char[] mayusculas = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};
        return mayusculas;
    }

    public static char[] generaNumeros() {
        char[] numeros = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'};
        return numeros;
    }

    public static char[] generaSimbolos() {
        char[] simbolos = {'*', '-', '_', ';', '.', ',', '?', '¿', '¡', '!', '$', '#'};
        return simbolos;
    }
}

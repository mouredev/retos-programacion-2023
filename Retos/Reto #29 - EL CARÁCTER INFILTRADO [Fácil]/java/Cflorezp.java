package reto29CaracterInfiltrado;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres.
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 *
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */
public class Cflorezp {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("\nIDENTIFICADOR DE CARACTERES DIFERENTES");
        System.out.println("Escriba la primera cadena de texto: ");
        String cadena1 = input.readLine();
        System.out.println("Escriba la segunda cadena de texto: ");
        String cadena2 = input.readLine();

        if(longitudCadenas(cadena1, cadena2)){
            List<String> resultado = caracteres(cadena1, cadena2);
            System.out.println("Las cadenas y sus caracteres diferentes: ");
            System.out.println(cadena1 + " / " + cadena2 + " -> " + resultado);
        }else{
            System.out.println("Las cadenas NO tienen la misma longitud.");
        }
        input.close();
    }

    public static List<String> caracteres(String cadena1, String cadena2){
        List<String> result = new ArrayList<>();
        for(int i = 0; i < cadena1.length(); i++){
            if(cadena1.charAt(i) != cadena2.charAt(i)){
                result.add(Character.toString(cadena2.charAt(i)));
            }
        }
        return result;
    }

    public static boolean longitudCadenas(String cadena1, String cadena2){
        if(cadena1.length() > cadena2.length() || cadena2.length() > cadena1.length()){
            return false;
        }
        return true;
    }
}

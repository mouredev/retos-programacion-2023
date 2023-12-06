package reto32ColumnaExcel;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */
public class Cflorezp {

    public static void main(String[] args) throws IOException {

        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("\nIngrese las letras para calcularle el numero de la columna en excel: ");
        String input = entrada.readLine();

        if(verificarLetras(input) && input.length() > 0){
            System.out.println(numeroColumna(input));
        }else{
            System.out.println("ERROR: La cadena tiene numeros o esta vacia");
        }

        entrada.close();
    }

    public static int numeroColumna(String input){
        HashMap<String, Integer> characters = new HashMap<>();
        characters.put("A", 1);
        characters.put("B", 2);
        characters.put("C", 3);
        characters.put("D", 4);
        characters.put("E", 5);
        characters.put("F", 6);
        characters.put("G", 7);
        characters.put("H", 8);
        characters.put("I", 9);
        characters.put("J", 10);
        characters.put("K", 11);
        characters.put("L", 12);
        characters.put("M", 13);
        characters.put("N", 14);
        characters.put("O", 15);
        characters.put("P", 16);
        characters.put("Q", 17);
        characters.put("R", 18);
        characters.put("S", 19);
        characters.put("T", 20);
        characters.put("U", 21);
        characters.put("V", 22);
        characters.put("W", 23);
        characters.put("X", 24);
        characters.put("Y", 25);
        characters.put("Z", 26);

        input = input.toUpperCase();
        final int TOTAL_LETRAS = 26;
        int operacion = 0;
        int total = 0;
        if(input.length() == 1){
            total = characters.get(input);
        }else{
            for(int i = 0; i < input.length() - 1; i++){
                operacion = characters.get(String.valueOf(input.charAt(i))) * TOTAL_LETRAS;
                total += operacion;
            }
            total += characters.get(String.valueOf(input.charAt(input.length() - 1)));
        }
        return total;
    }

    public static boolean verificarLetras(String input){
        for(int i = 0; i < input.length(); i++){
            if(Character.isDigit(input.charAt(i))){
                return false;
            }
        }
        return true;
    }
}

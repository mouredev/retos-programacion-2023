package reto3GeneradorDeContrasenas;

import java.util.Scanner;

public class cflorezp {

    public static void main(String[] args){
        /*
        System.out.println("***** GENERADOR DE CONTRASEÑAS *****\n");
        int option = 1;
        Scanner input = new Scanner(System.in);
        System.out.println("Desea incluir mayusculas? Y/N: ");
        String value = input.nextLine();
        if(value.equals("Y") || value.equals("y")) option++;

        System.out.println("Desea incluir numeros? Y/N: ");
        String value2 = input.nextLine();
        if(value2.equals("Y") || value2.equals("y")) option++;

        System.out.println("Desea incluir simbolos? Y/N: ");
        String value3 = input.nextLine();
        if(value3.equals("Y") || value3.equals("y")) option++;

        System.out.println(option);
        System.out.println(generaPasword(generaAletaorio8a16()));

         */
        /*
        int[] data = new int[2];

        int total = 9;
        int num = 2;
        total = total - num;
        for(int i= num-1; i >=0;i--){
            data[i]=1;
            int ls = 0;
            if(total>0){
                if(i==0){
                    data[i] +=total;
                }else{
                    int max = (int)(total/i);
                    ls  = (int)(Math.random()*max+1);
                    data[i] += ls;
                }
            }
            total -= ls;
        }
        //var_dump($data);
        for(int ele : data){
            System.out.println(ele);
        }
    */
        posiblesCombinaciones(16,4);


    }

    public static int generaAletaorio8a16() {
        int numero = (int) (Math.random() * (16 - 8 + 1) + 8);
        return numero;
    }

    public static String generaPasword(int longitud) {
        char[] caracteres = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                '*', '/', '*', '.', '?', '¿', '!', '¡', '-', '_', '+'};

        char[] result = new char[longitud];
        for (int i = 0; i < longitud; i++) {
            int position = (int) (Math.random() * caracteres.length);
            result[i] = caracteres[position];
        }
        return new String(result);

    }

    // NUEVA IMPLEMENTACION

    public static char[] generaMinusculas(){
        char[] minusculas = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        return minusculas;
    }

    public static char[] generaCaracteresRandom(char[] caracteres, int longitud){
        char[] result = new char[longitud];
        for (int i = 0; i < longitud; i++) {
            int position = (int) (Math.random() * caracteres.length);
            result[i] = caracteres[position];
        }
        return result;
    }

    public static int[] posiblesCombinaciones(int longitud, int combinaciones){
        int[] result = new int[combinaciones];
        longitud = longitud - combinaciones;
        for(int i = combinaciones - 1; i >= 0; i--){
            result[i] = 1;
            int provisional = 0;
            if(longitud > 0){
                if(i == 0){
                    result[i] +=longitud;
                }else{
                    int max = (int)(longitud/i);
                    provisional  = (int)(Math.random() * max + 1);
                    result[i] += provisional;
                }
            }
            longitud -= provisional;
        }
        return result;
    }



}

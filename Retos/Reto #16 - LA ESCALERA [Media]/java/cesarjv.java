package org.example;

import java.util.Scanner;


/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *
 */
public class cesarjv 
{
    public static void main( String[] args )
    {

        System.out.println("Bienvenido a la aplicacion para dibujar su escalera");
        System.out.println("Indique el numero de escalones que quiere dibujar (puede ser un numero negativo o positivo): ");
        Scanner sc=new Scanner(System.in);
        int num=sc.nextInt();
        System.out.println("El numero de escalones indicado es: "+num);
        if ((num > 0)) {
            positiveLadder(num);
        } else if (num==0){
            System.out.println("__");
        }
        else {
            negativeLadder(num);
        }
    }

    private static void positiveLadder(int value){
        StringBuilder sb=new StringBuilder();
        for(int i=value;i>=0;i--){
            char[] ch=new char[i];
            String result= new String(ch).replace("", " ");
            if(i==value){
                sb.append(result).append("_").append("\n");
            }
            else {
                sb.append(result).append("_|").append("\n");
            }
        }
        System.out.println(sb);
    }

    private static void negativeLadder(int value){
        value=Math.abs(value);
        StringBuilder sb=new StringBuilder();
        for(int i=0;i<=value;i++){
            char[] ch=new char[i];
            String result= new String(ch).replace("", " ");
            if(i==0){
                sb.append(result).append("_").append("\n");
            }
            else {
                sb.append(result).append("|_").append("\n");
            }
        }
        System.out.println(sb);
    }

}

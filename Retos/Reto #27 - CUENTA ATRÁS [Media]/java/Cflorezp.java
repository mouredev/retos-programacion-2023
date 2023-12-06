package reto27CuentaAtras;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */
public class Cflorezp {

    public static void main(String ...args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("*-*-*- CUENTA REGRESIVA -*-*-*\n");
        System.out.print("Por favor ingrese el numero del cual desea iniciar la cuenta regresiva: ");
        int number = Integer.parseInt(in.readLine());

        System.out.print("Por favor ingrese el intervalo en segundos: ");
        int seconds = Integer.parseInt(in.readLine());

        cuentaAtras(number, seconds);
    }

    public static void cuentaAtras(int number, int seconds){
        if(number > 0 && seconds > 0){
            for(int i = number; i >= 0; i--){
                System.out.println(i);
                try{
                    int interval = seconds * 1000;
                    Thread.sleep(interval);
                }catch (Exception e) {
                    e.printStackTrace ();
                }
            }
        }else{
            System.out.println("El número y los segundos deben ser mayores a cero");
        }
    }

}

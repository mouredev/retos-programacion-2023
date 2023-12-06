package com.exercises;

import java.util.Dictionary;
import java.util.Hashtable;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Mapeo();
        do{
            Scanner input = new Scanner(System.in);
            System.out.println("Ingrese una palabra: ");
            String palabra = input.next();
            int puntos = PuntosPalabra(palabra.toLowerCase());
            System.out.println("Sus puntos son: " + puntos);
            if(puntos >= 100)
            {
                input.close();
                return;
            }
            
        } while(true);
    }

    /*
        * La última semana de 2021 comenzamos la actividad de retos de programación,
        * con la intención de resolver un ejercicio cada semana para mejorar
        * nuestra lógica... ¡Hemos llegado al EJERCICIO 100! Gracias 🙌
        *
        * Crea un programa que calcule los puntos de una palabra.
        * - Cada letra tiene un valor asignado. Por ejemplo, en el abecedario
        *   español de 27 letras, la A vale 1 y la Z 27.
        * - El programa muestra el valor de los puntos de cada palabra introducida.
        * - El programa finaliza si logras introducir una palabra de 100 puntos.
        * - Puedes usar la terminal para interactuar con el usuario y solicitarle
        *   cada palabra.
    */
    public static char[] LowerCaseAlphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'};
    public static Dictionary<Character, Integer> values = new Hashtable<>();
    
    private static void Mapeo()
    {
        for(int i = 0; i < LowerCaseAlphabet.length; i++)
        {
            values.put(LowerCaseAlphabet[i], i+1);
        }
    }

    public static int PuntosPalabra(String palabra)
    {
        char[] letras = palabra.toCharArray();
        int suma = 0;
        for(char letra : letras)
        {
            try{
                suma += values.get(letra);
            } catch(Exception ex)
            {
                return 0;
            }
        }
        return suma;
    }
}

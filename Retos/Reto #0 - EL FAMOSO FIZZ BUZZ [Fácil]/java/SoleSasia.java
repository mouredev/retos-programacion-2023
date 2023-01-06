package com.retosprogramacion2023.reto_0;

/**
 * Reto #0: EL FAMOSO "FIZZ BUZZ"
 * Dificultad: Fácil | Publicación: 26/12/22 | Corrección: 02/01/23
 * Enunciado
 *
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 *
 * @author soles
 */
public class SoleSasia {

    public static void main(String[] args) {
              
        for (int num=1; num<=100; num++){
            if (num % 3 == 0 && num % 5 == 0){
                System.out.println("fizzbuzz");
            } else if (num % 3 == 0){
                System.out.println("fizz");
            } else if (num % 5 == 0){
                System.out.println("buzz");
            } else
                System.out.println(num);
        }
     
        
    }
}

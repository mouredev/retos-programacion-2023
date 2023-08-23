import java.util.Collections;
import java.util.Scanner;

/*
 *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
 *
 * Crea un programa que dibuje una Trifuerza de "Zelda"
 * formada por asteriscos.
 * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
 * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
 *
 * Ejemplo: Trifuerza 2
 * 
 *    *
 *   ***
 *  *   *
 * *** ***
 *
 */

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);
    
    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        int n = josepmonclus.getNumRows();

        josepmonclus.printTrifuerza(n);
    }

    private void printTrifuerza(int n) {
        String caracter = "*";
        String space = " ";

        String[] triangulo = new String[n];
        for(int i = 0; i < n; i++) {
            String lvlActual = "";
            lvlActual = String.join("", Collections.nCopies((i * 2) + 1, caracter));

            triangulo[i] = String.join("", Collections.nCopies((n - 1) - i, space));
            triangulo[i] = triangulo[i] + lvlActual;
        }

        //Triangulo Superior
        for(String lvl : triangulo){
            System.out.println(String.join("", Collections.nCopies(n, space)) + lvl);
        }

        //Triangulos inferiores
        for(int i = 0; i < n; i++){
            System.out.println(triangulo[i] + String.join("", Collections.nCopies(n - i, space)) + triangulo[i]);
        }
    }

    private int getNumRows() {
        int n = 0;

        while(true) {
            System.out.println("Indique el número de filas de los triángulos (n > 0):");
            String line = entrada.nextLine();

            try{
                n = Integer.parseInt(line);
                if( n > 0) {
                    break;
                } else {
                    System.out.println("¡¡Valor incorrecto!!");
                    System.out.println("");
                }
            } catch(Exception e) {
                System.out.println("¡¡Valor incorrecto!!");
                System.out.println("");
            }
        }
        
        return n;
    }
}

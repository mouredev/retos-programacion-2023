import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);
    
    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        int rango = josepmonclus.getRango();

        List<Integer[]> gemelos = josepmonclus.getPrimosGemelos(rango);

        for(Integer[] gemelo : gemelos) {
            System.out.println("(" + gemelo[0] + ", " + gemelo[1] + ")");
        }
    }

    private List<Integer[]> getPrimosGemelos(int rango) {
        List<Integer[]> gemelos = new ArrayList<>();

        List<Integer> primos = new ArrayList<>();

        for(int i = 1; i <= rango; i++) {
            boolean isPrimo = true;

            for(int primo : primos) {
                if(primo != 1 && i % primo == 0) {
                    isPrimo = false;
                }
            }

            if(isPrimo) primos.add(i);
        }

        for(int i = 1; i < primos.size(); i++) {
            if(primos.get(i) - primos.get(i - 1) == 2) {
                gemelos.add(new Integer[]{primos.get(i - 1), primos.get(i)});
            }
        }

        return gemelos;
    }

    private int getRango() {
        int rango = 0;

        while (true) {
            System.out.println("Introduzca el rango a analizar (rango > 0):");

            String sRango = entrada.nextLine();
            
            try {
                rango = Integer.parseInt(sRango);
                
                if(rango > 0) {
                    break;
                } else {
                    throw new Exception();
                }
            } catch(Exception e) {
                System.out.println("¡¡Valor incorrecto!!");
                System.out.println("");
            }
        }
        return rango;
    }
}

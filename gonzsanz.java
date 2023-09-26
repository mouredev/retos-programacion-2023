import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Reto #38
 * 
 * @author gonzsanz
 * @description
 *              Crea una función que encuentre todas las combinaciones de los
 *              números
 *              de una lista que suman el valor objetivo.
 *              - La función recibirá una lista de números enteros positivos
 *              y un valor objetivo.
 *              - Para obtener las combinaciones sólo se puede usar
 *              una vez cada elemento de la lista (pero pueden existir
 *              elementos repetidos en ella).
 *              - Ejemplo: Lista = [1, 5, 3, 2], Objetivo = 6
 *              Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
 *              (Si no existen combinaciones, retornar una lista vacía)
 * 
 */
public class gonzsanz {
    public static void main(String[] args) {

        int numeros[] = { 1, 5, 3, 2 };
        int objetivo = 6;

        List<Integer[]> combinaciones = getSum(numeros, objetivo);

        for (Integer[] combinacion : combinaciones) {
            System.out.println(Arrays.toString(combinacion));
        }

    }

    private static List<Integer[]> getSum(int nums[], int objetivo) {
        List<Integer[]> combinaciones = new ArrayList();

        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                if (nums[i] + nums[j] == objetivo) {
                    Integer[] combinacion = { nums[i], nums[j] };
                    combinaciones.add(combinacion);
                }

                if (nums[i] + nums[j] < objetivo) {
                    int flag = nums[i] + nums[j];
                    if (flag + nums[j + 1] == objetivo) {
                        Integer[] combinacion = { nums[i], nums[j], nums[j + 1] };
                        combinaciones.add(combinacion);
                    }
                }
            }
        }
        return combinaciones;
    }
}
package reto_27;

/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 *
 *
 * @author jesus
 */
public class jesusWay69 {

    public static void main(String[] args) {
  
        intervalo(5, 1);
    }

    public static void intervalo(int cantidadnum, int segundos) {
        for (int i = cantidadnum; i >= 0; i--) {

            System.out.println(i);
            try {

                Thread.sleep(segundos * 1000);

            } catch (Exception e) {
                System.out.println(e);

            }

        }

    }

}

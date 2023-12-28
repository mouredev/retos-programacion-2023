/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 */
public class jmverneri {
    public static void main(String[] args) {

        System.out.println("Cero: ");
        stairs(0);
        System.out.println("Positivo: ");
        stairs(4);
        System.out.println("Negativo: ");
        stairs(-10);
    }

    public static void stairs(int step) {
        if(step < 0) {
            System.out.println("_");
            for(int i = 0; i < Math.abs(step); i++) {
                for(int j = 0; j <= (i  * 2); j++) {
                    System.out.print(" ");
                }
                System.out.println("|_");
            }
        }
        else if(step > 0) {
            for(int j = (step * 2); j > 0; j--) {
                System.out.print(" ");
            }
            System.out.println("_");
            for(int i = (step - 1); i > 0; i--) {
                for(int k = (i * 2) ; k > 0; k--) {
                    System.out.print(" ");
                }
                System.out.println("_|");
            }
            System.out.println("_|");
        }
        else {
            System.out.println("__");
        }
    }
}
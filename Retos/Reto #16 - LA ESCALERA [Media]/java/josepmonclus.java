
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

public class josepmonclus {
    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        // Número de escaleras
        int n = 0;
        
        System.out.println("0 escalones");
        josepmonclus.printStairs(n);

        // Número de escaleras
        n = 5;
        
        System.out.println("5 escalones");
        josepmonclus.printStairs(n);

        // Número de escaleras
        n = -4;

        System.out.println("-4 escalones");
        josepmonclus.printStairs(n);
    }

    private void printStairs(int n) {
        if(n == 0) {
            System.out.println("__");
        } else if(n > 0) {
            int nActual = n;
            // Ascendente de izquierda a derecha
            while (nActual > 0) {
                StringBuilder line = new StringBuilder();
                for(int i = 0; i < nActual - 1; i++) {
                    line.append("  ");
                }

                if(nActual == n) {
                    line.append("_");
                } else {
                    line.append("_|");
                }

                System.out.println(line);

                nActual--;
            }
        } else {
            // Descendiente de izquierda a derecha
            int nActual = 0;
            n = n * -1;

            while (nActual < n) {
                StringBuilder line = new StringBuilder();
                for(int i = 1; i <= nActual - 1; i++) {
                    if(nActual == 1) line.append("");
                    else line.append("  ");
                }

                if(nActual == 0) line.append("_");
                else line.append(" |_");

                System.out.println(line);

                nActual++;
            }
        }
    }
}

public class EspinoLeandroo {


    /*
     * Este código utiliza una semilla inicial para el generador de números 
     * aleatorios y la fórmula (1103515245 * semilla + 12345) % 2147483648
     * para generar números aleatorios. La fórmula produce un número entero 
     * de 32 bits, y se utiliza el operador módulo (%) para asegurarse de que
     * el resultado está dentro del rango deseado de 0 a 100.
     * 
     * Es importante tener en cuenta que los generadores de números aleatorios 
     * pseudoaleatorios no producen números realmente aleatorios, sino que 
     * utilizan una secuencia determinística de valores para generar una 
     * secuencia de números que parecen ser aleatorios
     */


    public static void main(String[] args) {

        long semilla = 54321;
        for (int i = 0; i < 11; i++) {
            semilla = (1103515245 * semilla + 12345) % 2147483648L;
            int randomNum = (int) (semilla % 101);
            System.out.println(randomNum);
          }
    }
}

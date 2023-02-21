public class EspinoLeandroo {


    // Declarar las constantes necesarias para el generador de números pseudoaleatorios
   


    public static void main(String[] args) {

        long semilla = 54321;
        for (int i = 0; i < 11; i++) {
            semilla = (1103515245 * semilla + 12345) % 2147483648L;
            int randomNum = (int) (semilla % 101);
            System.out.println(randomNum);
          }
    }
}

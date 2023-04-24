

public class Dreyg {

    public static void main(String[] args) {
        System.out.println("###############################");
        System.out.println("Reto #4: PRIMO, FIBONACCI Y PAR");
        System.out.println("###############################");
        System.out.println("");
        // Numero / Parametro de entrada - Modificar para pruebas.
        int numIn = 14;

        String esPrimo = esPrimo(numIn);
        String esFibonacci = esFibonacci(numIn);
        String esPar = esPar(numIn);

        System.out.println(esPrimo.concat(esFibonacci).concat(esPar));

    }

    private static String esPrimo(int numIn) {
        boolean esPrimo = true;
        for (int i=2; i<numIn; i++){
            if ((numIn % i) == 0)
                esPrimo = false;
        }
        return (esPrimo == true) ? numIn + " es primo" : numIn + " no es primo";
    }

    private static String esFibonacci(int numIn) {
        return (isFibonacci(numIn)) ? ", fibonacci" : ", no es fibonacci";
    }

    private static boolean isFibonacci(int numIn) {
        Integer[] listaFib = calculatorSeriesFib(numIn);
        boolean isFib = false;
        for(int i=1;i<listaFib.length;i++){
            if (listaFib[i] == numIn)
                isFib = true;
        }
        return isFib;
    }

    private static Integer[] calculatorSeriesFib(int numIn) {
        Integer[] listaFib = new Integer[numIn];
        int num1 = 0, num2 = 1, suma = 1;
        for (int i = 1; i < numIn; i++) {
            suma = num1 + num2; //primero sumamos
            num1 = num2; //Despues, cambiamos la segunda variable por la primera
            num2 = suma; //Por ultimo, cambiamos la suma por la segunda variable
            listaFib[i] = suma;
        }
        return listaFib;
    }

    private static String esPar(int numIn) {
        return ((numIn % 2) == 0) ? " y es par" : " y es impar";
    }

}
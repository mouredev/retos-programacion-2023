public class joshArfDev {
    public static void main(String[] args) {

        System.out.println("FizzBuzz");

        //Inicializando un arreglo de 100 de length
        int rango[] = new int[100];

        //Rellenamos el arreglo del 1 al 100
        for(int i = 0; i < rango.length; i++){
            rango[i] = i + 1;
        }

        // Iteramos sobre el arreglo para imprimir resultados
        for (int numero : rango) {
            if (numero % 3 == 0 && numero % 5 == 0) {
                System.out.println("fizzbuzz");
            }
            else if (numero % 3 == 0) {
                System.out.println("fizz");
            }
            else if (numero % 5 == 0) {
                System.out.println("buzz");
            }
            else {
                System.out.println(numero);
            }
        }

    }
}
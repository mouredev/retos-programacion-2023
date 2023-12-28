public class EspinoLeandroo {

    public static void main(String[] args) {
        int rangoMaximo = 500; // Cambia este valor según tu rango máximo deseado
        encontrarYMostrarParesPrimosGemelos(rangoMaximo);
    }

    public static boolean esPrimo(int numero) {
        if (numero <= 1) {
            return false;
        }
        if (numero <= 3) {
            return true;
        }
        if (numero % 2 == 0 || numero % 3 == 0) {
            return false;
        }
        for (int i = 5; i * i <= numero; i += 6) {
            if (numero % i == 0 || numero % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }

    public static void encontrarYMostrarParesPrimosGemelos(int rangoMaximo) {
        for (int i = 2; i <= rangoMaximo - 2; i++) {
            if (esPrimo(i) && esPrimo(i + 2)) {
                System.out.println("(" + i + ", " + (i + 2) + ")");
            }
        }
    }
}

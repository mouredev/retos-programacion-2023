public class EspinoLeandroo {

    public static void main(String[] args) {
        String texto = "Este es un ejemplo de análisis de texto. Contiene varias oraciones y palabras de diferentes longitudes.";

        int numeroPalabras = 0;
        int longitudTotalPalabras = 0;
        int numeroOraciones = 0;
        String palabraMasLarga = "";

        String[] palabras = texto.split("\\s+");

        for (String palabra : palabras) {
            // Elimina signos de puntuación al final de las palabras

            if (palabra.contains(".") || palabra.contains("!") || palabra.contains("?")) {
                numeroOraciones++;
            }
            
            palabra = palabra.replaceAll("[.,;!?]+$", "");

            numeroPalabras++;
            longitudTotalPalabras += palabra.length();

            if (palabra.length() > palabraMasLarga.length()) {
                palabraMasLarga = palabra;
            }
        }

        double longitudMediaPalabras = (double) longitudTotalPalabras / numeroPalabras;

        System.out.println("Número total de palabras: " + numeroPalabras);
        System.out.println("Longitud media de las palabras: " + longitudMediaPalabras);
        System.out.println("Número de oraciones: " + numeroOraciones);
        System.out.println("Palabra más larga: " + palabraMasLarga);
    }
}

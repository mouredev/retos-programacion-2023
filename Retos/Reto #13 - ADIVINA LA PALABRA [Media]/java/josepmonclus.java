import java.util.Random;
import java.util.Scanner;

/*
 * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
 *   la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
 *     uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
 *     al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

public class josepmonclus {

    private static String[] DICCIONARIO = new String[]{
        "CLAVIJA", "GUITARRA", "TROMPETA", "TAMBOR", "CELULAR", 
        "ORDENADOR", "TELEVISION", "CUCHARA", "TENEDOR", "CUCHILLO", 
        "PLATO", "VASO", "PATINETE", "BICICLETA", "AUTOMOVIL", 
        "CAMION", "MOTOCICLETA", "AVION", "HELICOPTERO", "BARCO", 
        "TREN", "LIBRO", "REVISTA", "PERIODICO", "FOTOGRAFIA"};
    private static int INTENTOS = 10;

    Scanner entrada = new Scanner(System.in);

    public static void main(String[] args) {
        // Seleccionamos la palabra para el juego
        Random random = new Random();
        String palabra = DICCIONARIO[random.nextInt(DICCIONARIO.length)];
        
        josepmonclus josepmonclus = new josepmonclus();
        josepmonclus.runGame(palabra, INTENTOS);
    }

    private void runGame(String palabra, int intentos) {
        System.out.println("Vamos a jugar a adivinar la palabra oculta!");
        System.out.println("Aquí tienes la palabra:");

        String palabraOculta = ocultarPalabra(palabra);

        boolean win = false;
        while(intentos > 0){
            System.out.println(palabraOculta);
            System.out.println("Te quedan " + intentos + " intentos. Escribe una letra o la palabra oculta:");

            String prediccion = entrada.nextLine().toUpperCase();

            palabraOculta = makePrediccion(palabra, palabraOculta, prediccion);

            if(palabra.equals(palabraOculta)) {
                win = true;
                break;
            }

            intentos--;
        }

        System.out.println(win ? "¡Palabra encontrada!" : "¡Palabra no encontrada!");

        System.out.println("Juego terminado!");
    }

    private String makePrediccion(String palabra, String palabraOculta, String prediccion) {

        if(prediccion.length() > 1) {
            // Predicción de la palabra entera
            if(palabra.equals(prediccion)) {
                palabraOculta = palabra;
            }
        } else {
            // Predicción de letra
            char[] arrayOculta = palabraOculta.toCharArray();

            if(palabra.contains(prediccion)){
                for(int i = 0; i < palabra.length(); i++) {
                    if(palabra.charAt(i) == prediccion.toCharArray()[0]){
                        arrayOculta[i] = palabra.charAt(i);
                    }
                }
            }

            StringBuilder sb = new StringBuilder();
            for(char c : arrayOculta){
                sb.append(c);
            }

            palabraOculta = sb.toString();
        }
        

        return palabraOculta;
    }

    private String ocultarPalabra(String palabra) {
        int length = palabra.length();
        long ocultable = Math.round(length * 0.6);

        char[] letras = palabra.toCharArray();

        Random rand = new Random();
        for(int i = 0; i < ocultable; i++) {
            int pos = rand.nextInt(letras.length);
            
            if(letras[pos] != '_'){
                letras[pos] = '_';
            } else {
                i--;
            }
        }

        StringBuilder palabraOculta = new StringBuilder();
        for(char c : letras) {
            palabraOculta.append(c);
        }

        return palabraOculta.toString();
    }
}

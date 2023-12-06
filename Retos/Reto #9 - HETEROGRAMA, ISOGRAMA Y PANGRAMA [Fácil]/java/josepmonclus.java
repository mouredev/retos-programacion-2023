import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);

    String palabra;

    Character[] letrasValidas = new Character[]{
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        josepmonclus.nuevaPalabra();

        System.out.println((josepmonclus.isHeterograma() ? "Si" : "No") + " es un heterograma");
        System.out.println((josepmonclus.isIsograma() ? "Si" : "No") + " es un isograma");
        System.out.println((josepmonclus.isPangrama() ? "Si" : "No") + " es un pangrama");
    }

    private void nuevaPalabra() {
        System.out.println("Introduce la palabra a analizar:");

        palabra = entrada.nextLine();
        palabra = palabra.toUpperCase();
    }

    private boolean isHeterograma() {
        // Heterograma, es una palabra o frase sin letras repetidas
        boolean isHeterograma = true;

        Map<Character, Integer> letras = new HashMap<>();
        for(char c : palabra.toCharArray()){
            if(Arrays.asList(letrasValidas).contains(c)) {
                int repeticiones = letras.get(c) == null ? 0 : letras.get(c);

                letras.put(c, repeticiones + 1);
            }
        }

        for(int n : letras.values()) {
            if (n > 1) {
                isHeterograma = false;
                break;
            } 
        }

        return isHeterograma;
    }

    private boolean isIsograma() {
        // Isograma, es una palabra o frase en la que cada letra aparece el mismo número de veces
        boolean isIsograma = true;

        Map<Character, Integer> letras = new HashMap<>();
        for(char c : palabra.toCharArray()){
            if(Arrays.asList(letrasValidas).contains(c)) {
                int repeticiones = letras.get(c) == null ? 0 : letras.get(c);

                letras.put(c, repeticiones + 1);
            }
        }

        int k = letras.get(palabra.toCharArray()[0]);

        for(int n : letras.values()) {
            if (n != k) {
                isIsograma = false;
                break;
            } 
        }

        return isIsograma;
    }
    
    private boolean isPangrama() {
        // Pagrama, una frase donde aparecen todas las letras del abecedario
        boolean isPangrama = true;

        Map<Character, Integer> letras = new HashMap<>();
        for(char letra : letrasValidas){
            letras.put(letra, 0);
        }

        for(char c : palabra.toCharArray()){
            if(Arrays.asList(letrasValidas).contains(c)) {   
                int repeticiones = letras.get(c);

                letras.put(c, repeticiones + 1);
            }
        }

        for(int n : letras.values()) {
            if(n == 0) {
                isPangrama = false;
                break;
            }
        }

        return isPangrama;
    }
}

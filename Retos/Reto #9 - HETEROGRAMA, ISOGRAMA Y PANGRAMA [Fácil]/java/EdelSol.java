/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un contadorCaracteres, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
package retosMoureDev.heterograma;

import java.text.Normalizer;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class EdelSol {
    
    private int alfabeto[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'};
    private boolean heterograma = false;
    private String textoPurgado = "";
    private HashMap<Character,Integer> numCaracteres = new HashMap<>();
    
    public static void main(String[] args) {
        
        EdelSol reto_9 = new EdelSol();
        
        System.out.println("### Reto #9 Heterograma, Isograma o Pangrama? ###");
        System.out.print("Inserte el texto a valorar >>> ");
        String texto;
        try (Scanner scanner = new Scanner(System.in)) {
            texto = scanner.nextLine().toLowerCase();
        }
        
        reto_9.setTextoPurgado(reto_9.quitaDiacriticos(texto));
        reto_9.contadorCaracteres(reto_9.getTextoPurgado());
        
        System.out.println(reto_9.getNumCaracteres());
        
        reto_9.heterograma();
        reto_9.isograma();
        reto_9.pangrama();
    }
    
    /**
     * Reemplazamos todos los caracteres con tildes por 
     * caracteres básicos manteniendo la 'ñ' como caracter básico
     */
    private String quitaDiacriticos(String s) {
        ArrayList<Integer> tilde = new ArrayList<>();
        char sustituto = 'ñ';
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == sustituto) {
                tilde.add(i);
            }
        }
        s = Normalizer.normalize(s, Normalizer.Form.NFD);
        s = s.replaceAll("[\\p{InCombiningDiacriticalMarks}]", "");

        // Recolocamos la 'ñ' en su posición de origen
        if (!tilde.isEmpty()) {
            StringBuilder sb = new StringBuilder(s);
            for (int i = 0; i < tilde.size(); i++) {
                sb.setCharAt(tilde.get(i), sustituto);
                s = sb.toString();
            }
        }

        return s;
    }
    
    /**
     * Contaje de caracteres 
     */
    private HashMap<Character,Integer> contadorCaracteres(String texto) {

        for (int i = 0; i < alfabeto.length; i++) {
            int contador = 0;
            for (int j = 0; j < texto.length(); j++) {
                if (texto.charAt(j) == alfabeto[i]) {
                    contador++;
                }
            }
            if (contador > 0) {
                numCaracteres.put((char)alfabeto[i], contador);
            }
        }
        
        return numCaracteres;
    }
    
    /*
    * Detecta si una cadena de texto es heterograma
    * "palabra o frase que no contiene ninguna letra repetida"
    */
    private void heterograma() {
        boolean estado = false;
        for (Character next : numCaracteres.keySet()) {
            if (numCaracteres.get(next) > 1) {
                estado = true;
                break;
            }             
        }
        if (estado) {
            System.out.println("El texto insertado tiene NO es heterograma.");
        } else {
            heterograma = true;
            System.out.println("El texto insertado tiene la propiedad de HETEROGRAMA.");
        }
        
    }
    
    /*
    * Función para detectar si una cadena de texto es isograma suponiendo que
    * es una "palabra o frase que contiene alguna letra repetida"
    * (No he encontrado una fuente con la que me entere de lo que
    * realmente es un isograma)
    */
    private void isograma() {
        int cont = 1;
        for (Character next : numCaracteres.keySet()) {
            if (numCaracteres.get(next) > 1) {
                cont++;
            }
        }
        if (cont > 1) {
            System.out.println("El texto insertado tiene la propiedad de ISOGRAMA");
        } else {
            System.out.println("El texto NO es un isograma");
        }
    }
    
    /*
    * Función para detectar si una cadena de texto es pangrama
    * "palabra o frase que contiene todas las letras del alfabeto de un idioma"
    * o pangrama perfecto
    * "si cada letra aparece una única vez"
    */
    private void pangrama() {
        if ((numCaracteres.size() == alfabeto.length) && heterograma) {
            System.out.println("El texto insertado tiene la propiedad de PANGRAMA PERFECTO.");
        } else if (numCaracteres.size() == alfabeto.length){
            System.out.println("El texto insertado tiene la propiedad de PANGRAMA.");
        } else {
            System.out.println("El texto insertado NO es un pangrama.");
        }
    }

    public void setTextoPurgado(String textoPurgado) {
        this.textoPurgado = textoPurgado;
    }

    public String getTextoPurgado() {
        return textoPurgado;
    }

    public HashMap<Character, Integer> getNumCaracteres() {
        return numCaracteres;
    }
}

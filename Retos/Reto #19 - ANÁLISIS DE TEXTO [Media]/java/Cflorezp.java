package reto19AnalisisTexto;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Scanner;
import java.util.stream.Collectors;

/*
 * Crea un programa que analice texto y obtenga:
 * - Número total de palabras.
 * - Longitud media de las palabras.
 * - Número de oraciones del texto (cada vez que aparecen un punto).
 * - Encuentre la palabra más larga.
 *
 * Todo esto utilizando un único bucle.
 */
public class Cflorezp {

    public static void main(String[] args) {

        String sentence = "";

        System.out.println("Por favor ingrese sus frases, ¡¡No olvide finalizar cada frase con punto!!");
        Scanner in = new Scanner(System.in);
        sentence = in.nextLine();

        sentence = sentence.concat(" ");

        int words = 0;
        int numOfLetters = 0;
        int numOfSentences = 0;
        int tamanio = 0;
        String largeWord = "";
        List<Character> word = new ArrayList<>();

        for(int i = 0; i < sentence.length(); i++){
            if(sentence.charAt(i) == ' '){
                words++;
                if(word.size() > tamanio){
                    largeWord = word.stream().map(Objects::toString).collect(Collectors.joining());
                    tamanio = word.size();
                }
                word.clear();
            }
            if(sentence.charAt(i) != ' ' && sentence.charAt(i) != '.'){
                numOfLetters++;
                word.add(sentence.charAt(i));
            }
            if(sentence.charAt(i) == '.'){
                numOfSentences++;
            }
         }

        System.out.println("Hay un total de " + words + " palabras.");
        System.out.println("La longitud media de las palabras es de " + numOfLetters / words + " letras.");
        System.out.println("Hay un total de " + numOfSentences + " oraciones.");
        System.out.println("la palabra mas larga es: " + largeWord);

        in.close();

    }
}

package reto24cifradoCesar;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Cflorezp {

    public static void main(String[] args) throws IOException {

        BufferedReader input = new BufferedReader(new InputStreamReader(System.in));

        System.out.println("\nIndique si desea cifrar o descifrar una frase\n " +
                "1 -> cifrar \n 2 -> descifrar");
        int value = Integer.parseInt(input.readLine());

        System.out.print("Ingrese la frase: ");
        String sentence = input.readLine();

        char[] sentenceChars = sentence.toCharArray();
        StringBuilder newSentence = new StringBuilder();


        for(int i = 0; i < sentenceChars.length; i++){
            if(sentenceChars[i] != ' '){
                newSentence.append(cifradoCesar3(value, String.valueOf(sentenceChars[i])));
            }else{
                newSentence.append(sentenceChars[i]);
            }
        }

        String finalSentence = newSentence.toString();
        System.out.println(finalSentence);

    }

    public static String cifradoCesar3(int option, String vowel){
        HashMap<String, String> characters = new HashMap<>();
        characters.put("A", "D");
        characters.put("B", "E");
        characters.put("C", "F");
        characters.put("D", "G");
        characters.put("E", "H");
        characters.put("F", "I");
        characters.put("G", "J");
        characters.put("H", "K");
        characters.put("I", "L");
        characters.put("J", "M");
        characters.put("K", "N");
        characters.put("L", "O");
        characters.put("M", "P");
        characters.put("N", "Q");
        characters.put("O", "R");
        characters.put("P", "S");
        characters.put("Q", "T");
        characters.put("R", "U");
        characters.put("S", "V");
        characters.put("T", "W");
        characters.put("U", "X");
        characters.put("V", "Y");
        characters.put("W", "Z");
        characters.put("X", "A");
        characters.put("Y", "B");
        characters.put("Z", "C");

        if(option == 2){
            for(String key: characters.keySet()){
                if(characters.get(key).equals(vowel.toUpperCase())){
                    return key;
                }
            }
        }
        return  characters.get(vowel.toUpperCase());
    }

    
}

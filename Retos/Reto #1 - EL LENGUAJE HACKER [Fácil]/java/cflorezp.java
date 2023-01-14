package lenguajeHacker;

import java.util.*;

public class cflorezp {

    public static void main(String[] args){

        HashMap<String, String> leetAlphabet = new HashMap<>();
        leetAlphabet.put("A", "4");
        leetAlphabet.put("B", "8");
        leetAlphabet.put("C", "[");
        leetAlphabet.put("D", ")");
        leetAlphabet.put("E", "3");
        leetAlphabet.put("F", "|=");
        leetAlphabet.put("G", "&");
        leetAlphabet.put("H", "#");
        leetAlphabet.put("I", "1");
        leetAlphabet.put("J", ",_|");
        leetAlphabet.put("K", ">|");
        leetAlphabet.put("L", "1");
        leetAlphabet.put("M", "nn");
        leetAlphabet.put("N", "^/");
        leetAlphabet.put("Ñ", "H");
        leetAlphabet.put("O", "0");
        leetAlphabet.put("P", "|*");
        leetAlphabet.put("Q", "(_,)");
        leetAlphabet.put("R", "I2");
        leetAlphabet.put("S", "5");
        leetAlphabet.put("T", "7");
        leetAlphabet.put("U", "(_)");
        leetAlphabet.put("V", "\\/");
        leetAlphabet.put("W", "VV");
        leetAlphabet.put("X", "><");
        leetAlphabet.put("Y", "j");
        leetAlphabet.put("Z", "2");
        leetAlphabet.put("1", "L");
        leetAlphabet.put("2", "R");
        leetAlphabet.put("3", "E");
        leetAlphabet.put("4", "A");
        leetAlphabet.put("5", "S");
        leetAlphabet.put("6", "b");
        leetAlphabet.put("7", "T");
        leetAlphabet.put("8", "B");
        leetAlphabet.put("9", "g");
        leetAlphabet.put("0", "o");

        Scanner inputText = new Scanner(System.in);
        System.out.println("*********************************************************************************" +
                            "\n\t\t\t TRADUCTOR DE LENGUAJE NATURAL A LENGUAJE HACKER" +
                            "\n*********************************************************************************" );
        System.out.println("--> Por favor escriba una palabra o una frase para traducirla: ");
        String value = inputText.nextLine();

        String result = "";
        for(int i = 0; i < value.length(); i++){
            char flag = value.charAt(i);
            result += (flag == ' ') ? " " : leetAlphabet.get(String.valueOf(flag).toUpperCase());
        }
        System.out.print("La traduccion es la siguiente: \n" + result + "\n\nGracias por usar el traductor.");

        inputText.close();
    }
}

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package nameless.react;

import java.util.Arrays;
import java.util.Hashtable;
import java.util.List;
import java.util.stream.Collectors;
import javax.swing.JOptionPane;

/**
 *
 * @author joel
 */
public class NamelessReact {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        hackerLenguaje();
    }
 
    
    public static void hackerLenguaje() {
        Map<String, String> replaceLetters = new HashMap<>() {{
            put("A", "4");
            put("B", "I3");
            put("C", "[");
            put("D", ")");
            put("E", "3");
            put("F", "|=");
            put("G", "&");
            put("H", "#");
            put("I", "1");
            put("J", ",_|");
            put("K", ">|");
            put("L", "1");
            put("M", "/\\/\\");
            put("N", "^/");
            put("O", "0");
            put("P", "|*");
            put("Q", "(_,)");
            put("R", "|2");
            put("S", "5");
            put("T", "7");
            put("U", "(_)");
            put("V", "\\/");
            put("W", "\\/\\/");
            put("X", "><");
            put("Y", "j");
            put("Z", "2");
            put(" ", " ");        
            put("1", "L");        
            put("2", "R");        
            put("3", "E");        
            put("4", "A");        
            put("5", "S");        
            put("6", "b");        
            put("7", "T");        
            put("8", "B");        
            put("9", "g");        
            put("0", "o");        
        }};
        
        
        
        
        List<String> word = Arrays.asList(JOptionPane.showInputDialog("Digite un nombre o palabra: ").split("")).stream()
                            .map(letter -> replaceLetters.containsKey(letter.toUpperCase()) ? replaceLetters.get(letter.toUpperCase()) : letter)
                            .collect(Collectors.toList());
        JOptionPane.showMessageDialog(null, String.join("", word));
    }
}

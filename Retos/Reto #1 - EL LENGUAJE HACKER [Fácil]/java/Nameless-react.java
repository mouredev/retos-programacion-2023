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
        Hashtable<String, String> replaceLetters = new Hashtable<String, String>();
        
        
        
        replaceLetters.put("A", "4");
        replaceLetters.put("B", "I3");
        replaceLetters.put("C", "[");
        replaceLetters.put("D", ")");
        replaceLetters.put("E", "3");
        replaceLetters.put("F", "|=");
        replaceLetters.put("G", "&");
        replaceLetters.put("H", "#");
        replaceLetters.put("I", "1");
        replaceLetters.put("J", ",_|");
        replaceLetters.put("K", ">|");
        replaceLetters.put("L", "1");
        replaceLetters.put("M", "/\\/\\");
        replaceLetters.put("N", "^/");
        replaceLetters.put("O", "0");
        replaceLetters.put("P", "|*");
        replaceLetters.put("Q", "(_,)");
        replaceLetters.put("R", "|2");
        replaceLetters.put("S", "5");
        replaceLetters.put("T", "7");
        replaceLetters.put("U", "(_)");
        replaceLetters.put("V", "\\/");
        replaceLetters.put("W", "\\/\\/");
        replaceLetters.put("X", "><");
        replaceLetters.put("Y", "j");
        replaceLetters.put("Z", "2");
        replaceLetters.put(" ", " ");
        
        
        List<String> word = Arrays.asList(JOptionPane.showInputDialog("Digite un nombre o palabra: ").toUpperCase().split("")).stream().map(letter -> replaceLetters.get(letter)).collect(Collectors.toList());
        JOptionPane.showMessageDialog(null, String.join("", word));
    }
}

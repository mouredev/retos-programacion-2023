import javax.swing.*;
import java.util.Hashtable;
public class AlejandroRS10 {
    public static void main(String[] args) {

        String texto = JOptionPane.showInputDialog("Mensaje a encriptar:").toUpperCase();

        Hashtable diccionario = new Hashtable();
        diccionario.put("A", "4");diccionario.put("B", "8");diccionario.put("C", "{");
        diccionario.put("D", "?");diccionario.put("E", "€");diccionario.put("F", "/=");
        diccionario.put("G", "&");diccionario.put("H", "#");diccionario.put("I", "1");
        diccionario.put("J", "]");diccionario.put("K", "|<");diccionario.put("L", "£");
        diccionario.put("M", "|V|");diccionario.put("N", "И");diccionario.put("Ñ", "И~");
        diccionario.put("O", "Ø");diccionario.put("P", "9");diccionario.put("Q", "?");
        diccionario.put("R", "Я");diccionario.put("S", "5");diccionario.put("T", "7");
        diccionario.put("U", "µ");diccionario.put("V", "|/");diccionario.put("W", "uu");
        diccionario.put("X", "><");diccionario.put("Y", "Ч"); diccionario.put("Z", "2");
        diccionario.put(" ", " ");

        for(int i=0; i<texto.length(); i++){
            System.out.print(diccionario.get(texto.substring(i, i+1)));
        }
    }
}

import javax.swing.JOptionPane;
import java.util.HashMap;
import java.util.Map;

public class Ghuaynamontes {

    public static void main(String[] args) {
        String entrada = JOptionPane.showInputDialog("Ingrese la combinación de pulsaciones T9 separadas por guiones:");
        String resultado = t9ToTexto(entrada);
        JOptionPane.showMessageDialog(null, "Salida: " + resultado);
    }

    public static String t9ToTexto(String entrada) {
        Map<String, String> t9ToTextoMap = getT9ToTextoMap();

        StringBuilder texto = new StringBuilder();
        String[] bloques = entrada.split("-");
        for (String bloque : bloques) {
            texto.append(t9ToTextoMap.get(bloque));
        }

        return texto.toString();
    }

    public static Map<String, String> getT9ToTextoMap() {
        Map<String, String> t9ToTextoMap = new HashMap<>();
        t9ToTextoMap.put("2", "A");
        t9ToTextoMap.put("22", "B");
        t9ToTextoMap.put("222", "C");
        t9ToTextoMap.put("3", "D");
        t9ToTextoMap.put("33", "E");
        t9ToTextoMap.put("333", "F");
        t9ToTextoMap.put("4", "G");
        t9ToTextoMap.put("44", "H");
        t9ToTextoMap.put("444", "I");
        t9ToTextoMap.put("5", "J");
        t9ToTextoMap.put("55", "K");
        t9ToTextoMap.put("555", "L");
        t9ToTextoMap.put("6", "M");
        t9ToTextoMap.put("66", "N");
        t9ToTextoMap.put("666", "O");
        t9ToTextoMap.put("7", "P");
        t9ToTextoMap.put("77", "Q");
        t9ToTextoMap.put("777", "R");
        t9ToTextoMap.put("7777", "S");
        t9ToTextoMap.put("8", "T");
        t9ToTextoMap.put("88", "U");
        t9ToTextoMap.put("888", "V");
        t9ToTextoMap.put("9", "W");
        t9ToTextoMap.put("99", "X");
        t9ToTextoMap.put("999", "Y");
        t9ToTextoMap.put("9999", "Z");
        return t9ToTextoMap;
    }
}

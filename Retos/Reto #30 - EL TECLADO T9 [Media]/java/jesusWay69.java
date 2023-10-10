package reto_30;

import java.util.HashMap;
import java.util.Map;

/**
 * * Los primeros dispositivos móviles tenían un teclado llamado T9 con el que
 * se podía escribir texto utilizando únicamente su teclado numérico (del 0 al
 * 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su representación
 * con letras. - Debes buscar cuál era su correspondencia original. - Cada
 * bloque de pulsaciones va separado por un guión. - Si un bloque tiene más de
 * un número, debe ser siempre el mismo. - Ejemplo: Entrada:
 * 6-666-88-777-33-3-33-888 Salida: MOUREDEV
 *
 * @author jesus
 */
public class jesusWay69 {

    public static void main(String[] args) {

        String keys = "44-33-555-555-666-0-9-666-777-555-3";
        alphabet_hm(keys);

    }

    private static void alphabet_hm(String keys) {
        String text = "";

        Map<String, String> letters_hm = new HashMap<String, String>();
        letters_hm.put("2", "A");
        letters_hm.put("22", "B");
        letters_hm.put("222", "C");
        letters_hm.put("3", "D");
        letters_hm.put("33", "E");
        letters_hm.put("333", "F");
        letters_hm.put("4", "G");
        letters_hm.put("44", "H");
        letters_hm.put("444", "I");
        letters_hm.put("5", "J");
        letters_hm.put("55", "K");
        letters_hm.put("555", "L");
        letters_hm.put("6", "M");
        letters_hm.put("66", "N");
        letters_hm.put("6666", "Ñ");
        letters_hm.put("666", "O");
        letters_hm.put("7", "P");
        letters_hm.put("77", "Q");
        letters_hm.put("777", "R");
        letters_hm.put("7777", "S");
        letters_hm.put("8", "T");
        letters_hm.put("88", "U");
        letters_hm.put("888", "V");
        letters_hm.put("9", "W");
        letters_hm.put("99", "X");
        letters_hm.put("999", "Y");
        letters_hm.put("9999", "Z");
        letters_hm.put("0", " ");
        for (String key : keys.split("-")) {
            if (letters_hm.containsKey(key)) {
               
                
                text = text + letters_hm.get(key);
            }
        }
        
        System.out.println(text);
    }
}

import java.util.HashMap;
import java.util.Map;

/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */
public class AnNavNicolas {

    public static void main(String[] args) {
        System.out.println(mensajeAT9("6-666-88-777-33-3-33-888"));
        System.out.println(mensajeAT9("44-666-555-2-0-6-88-66-3-666-1111"));
    }

    public static String mensajeAT9(String mensaje) {
        String[] spliteMensaje = mensaje.split("-");
        StringBuilder mensajeTexto = new StringBuilder();
        for (String tecla : spliteMensaje) {
            mensajeTexto.append(teclado(Integer.valueOf(tecla.substring(0,1)), Integer.valueOf(tecla.length()-1)));
        }
        return mensajeTexto.toString();
    }

    private static String teclado(Integer numero, Integer pulsacion) {
        Map<Integer, String[]> tecladoT9 = new HashMap<>();
        tecladoT9.put(0, new String[] {" "});
        tecladoT9.put(1, new String[] {",", ".", "?", "!"});
        tecladoT9.put(2, new String[] {"A", "B", "C"});
        tecladoT9.put(3, new String[] {"D", "E", "F"});
        tecladoT9.put(4, new String[] {"G", "H", "I"});
        tecladoT9.put(5, new String[] {"J", "K", "L"});
        tecladoT9.put(6, new String[] {"M", "N", "O"});
        tecladoT9.put(7, new String[] {"P", "Q", "R", "S"});
        tecladoT9.put(8, new String[] {"T", "U", "V"});
        tecladoT9.put(9, new String[] {"W", "X", "Y", "Z"});
        return tecladoT9.get(numero)[pulsacion];
    }

}

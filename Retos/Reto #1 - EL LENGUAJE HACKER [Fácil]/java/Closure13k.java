import javax.swing.JOptionPane;
import java.util.Map;
import java.util.stream.Collectors;

import static java.util.Map.entry;

public class Closure13k {
    /*
     * Escribe un programa que reciba un texto y transforme lenguaje natural a
     * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
     *  se caracteriza por sustituir caracteres alfanuméricos.
     * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
     *   con el alfabeto y los números en "leet".
     *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
     */
    //Método de entrada de datos.
    //Si se cancela la operación, mandará un texto por defecto.
    //Si se envía una cadena vacía o con espacios en blanco, mandará otro texto por defecto.
    private static String solicitarTexto() {
        String textoSolicitado = JOptionPane.showInputDialog("Escríbeme algo:");
        if ((textoSolicitado == null)) return "Cerraste el cuadro de diálogo.";
        if (textoSolicitado.isBlank()) return "No mandaste texto x";
        return textoSolicitado;
    }

    //Método de traducción.
    //Si el caracter que recibe no está en el diccionario, no lo reemplaza.
    private static String traducirCaracter(Character c) {
        String valorTraducido = DICCIONARIO.get(c);
        return valorTraducido != null ? valorTraducido : String.valueOf(c);
    }

    public static void main(String[] args) {
        String textoIntroducido = solicitarTexto();
        String traduccion = textoIntroducido.toUpperCase()
                .chars()
                .mapToObj(c -> traducirCaracter((char) c))
                .collect(Collectors.joining());

        System.out.printf("""
                Texto: %s
                Leet: %s
                """, textoIntroducido, traduccion
        );
    }

    //Diccionario ya preparado.
    private static final Map<Character, String> DICCIONARIO = Map.ofEntries(
            //Letras
            entry('A', "4"),
            entry('B', "I3"),
            entry('C', "["),
            entry('D', ")"),
            entry('E', "3"),
            entry('F', "|="),
            entry('G', "&"),
            entry('H', "#"),
            entry('I', "1"),
            entry('J', ",_|"),
            entry('K', ">|"),
            entry('L', "1"),
            entry('M', "/\\/\\"),
            entry('N', "^/"),
            entry('O', "0"),
            entry('P', "|*"),
            entry('Q', "(_,)"),
            entry('R', "I2"),
            entry('S', "5"),
            entry('T', "7"),
            entry('U', "(_)"),
            entry('V', "\\/"),
            entry('W', "\\/\\/"),
            entry('X', "><"),
            entry('Y', "j"),
            entry('Z', "2"),
            //Números
            entry('1', "L"),
            entry('2', "R"),
            entry('3', "E"),
            entry('4', "A"),
            entry('5', "S"),
            entry('6', "b"),
            entry('7', "T"),
            entry('8', "B"),
            entry('9', "g"),
            entry('0', "o")
    );
}

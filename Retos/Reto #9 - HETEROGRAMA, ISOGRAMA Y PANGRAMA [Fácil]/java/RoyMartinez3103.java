
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */
// Heterograma: No se repite ninguna letra
// Isograma: Cada letra aparece la misma cantidad de veces.
// Pangrama: Contiene todas las letras del abecedario.
public class RoyMartinez3103 {

    public static void main(String args[]) {
        Scanner scan = new Scanner(System.in);
        String cadena;

        System.out.println("=== ¿Es Heterograma, Isograma o Pangrama? ===");
        System.out.println("Ingresa una cadena: ");
        cadena = scan.nextLine();
        esHeterograma(cadena);
        esIsograma(cadena);
        esPangrama(cadena);

    }

    static void esHeterograma(String cadena) {
        Set<Character> unique = new HashSet<>();
        Boolean verify = true;
        for (char i : cadena.toCharArray()) {
            if (!unique.add(i)) {
                verify = false;
                break;
            }
        }
        if (verify) {
            System.out.println("SI es Heterograma");
        } else {
            System.out.println("NO es heterograma");
        }
    }

    static void esIsograma(String cadena) {
        HashMap<Character, Integer> contadorMap = new HashMap<>();
        Boolean verify = true;

        for (char c : cadena.toLowerCase().toCharArray()) {
            if (contadorMap.containsKey(c)) {
                contadorMap.put(c, contadorMap.get(c) + 1);
            } else {
                contadorMap.put(c, 1);
            }
        }
        contadorMap.remove(' ');
        Object[] value = contadorMap.values().toArray();

        for (int i = 0; i < value.length; i++) {
            if (i == 0) {
                continue;
            }
            if (value[i] != value[i - 1]) {
                verify = false;
            }
        }
        if (verify) {
            System.out.println("SI es isograma");
        } else {
            System.out.println("NO es isograma");
        }

    }

    static void esPangrama(String cadena) {
        List<Character> ALFABETO = List.of('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ',', '.');
        Boolean verify = true;

        for (char c : cadena.toUpperCase().toCharArray()) {
            if (!ALFABETO.contains(c)) {
                verify = false;
            }
        }
        if (verify) {
            System.out.println("SI es pangrama");
        } else {
            System.out.println("NO es pangrama");
        }

    }

}

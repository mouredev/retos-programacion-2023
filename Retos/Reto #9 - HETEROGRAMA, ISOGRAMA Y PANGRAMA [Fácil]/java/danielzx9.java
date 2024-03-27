import java.util.HashSet;
import java.util.Set;
// # Reto #9: Heterograma, isograma y pangrama
// #### Dificultad: Fácil | Publicación: 27/02/23 | Corrección: 06/03/23

// ## Enunciado

// ```
// /*
//  * Crea 3 funciones, cada una encargada de detectar si una cadena de
//  * texto es un heterograma, un isograma o un pangrama.
//  * - Debes buscar la definición de cada uno de estos términos.
//  */
// ```
// #### Tienes toda la información extendida sobre los retos de programación semanales en **[retosdeprogramacion.com/semanales2023](https://retosdeprogramacion.com/semanales2023)**.

// Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

// > Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.

public class danielzx9 {

    public static boolean esHeterograma(String texto) {
        Set<Character> caracteres = new HashSet<>();
        for (char c : texto.toCharArray()) {
            if (Character.isLetter(c)) {
                if (caracteres.contains(c)) {
                    return false; 
                }
                caracteres.add(c);
            }
        }
        return true; 
    }
    
    public static boolean esIsograma(String texto) {
        Set<Character> caracteres = new HashSet<>();
        for (char c : texto.toCharArray()) {
            if (Character.isLetter(c)) {
                char letra = Character.toLowerCase(c);
                if (caracteres.contains(letra)) {
                    return false; 
                }
                caracteres.add(letra);
            }
        }
        return true; 
    }
    
    public static boolean esPangrama(String texto) {
        Set<Character> letras = new HashSet<>();
        for (char c : texto.toCharArray()) {
            if (Character.isLetter(c)) {
                letras.add(Character.toLowerCase(c));
            }
        }
        return letras.size() == 26; 
    }
    
        
    public static void main(String[] args) {
        String ejemplo = "valor";
        
        // Prueba de las funciones
        System.out.println("Es Heterograma: " + esHeterograma(ejemplo));
        System.out.println("Es Isograma: " + esIsograma(ejemplo));
        System.out.println("Es Pangrama: " + esPangrama(ejemplo));
    }

    
}

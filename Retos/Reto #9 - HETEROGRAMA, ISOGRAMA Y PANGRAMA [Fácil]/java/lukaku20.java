import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

/**
 * @author lukaku20
 */

public class Retos_de_programacion_9 {

    public static Scanner scan = new Scanner(System.in).useDelimiter("\n");
    public static String[] abecedario = new String[]{"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","v","w","x","y","z"};
    
    public static void main(String[] args) {
        
        System.out.println(" ");
        System.out.println(" Escribe una frase o palabra: ");
        String frase;
        frase = scan.next();
        System.out.println("");
        System.out.println("¿Quieres saber si es: ");
        System.out.println("1. un Pangrama?");
        System.out.println("2. un Isograma?");
        System.out.println("3. un Heterograma?");
        int opcion;
        opcion = scan.nextInt();
        switch(opcion){
            case 1: System.out.println("Es un pangrama: " + esPangrama(frase));
            break;
            case 2: System.out.println("Es un isograma: " + esIsograma(frase));
            break;
            case 3: System.out.println("Es un heterograma: " + esHeterograma(frase));
            break;
            default: System.out.println("Esa opcion no es válida.");
        }
    }
    
    public static boolean esPangrama(String a){
        a = a.toLowerCase();
        for (String abecedario1 : abecedario) {
            if(!a.contains(abecedario1)){
                return false;
            }
        }
        return true;
    }
    
    public static boolean esIsograma(String b) {
    int tamanio = b.length();
    Set<Character> letras = new HashSet<>();
    for (int i = 0; i < tamanio; i++) {
        char letra = b.charAt(i);
        if (letras.contains(letra)) {
            return false;
        }
        letras.add(letra);
    }
    return true;
}

    
    public static boolean esHeterograma(String c) {
    for (int i = 0; i < c.length(); i++) {
        char letra = c.charAt(i);
        // Buscar si la letra aparece más de una vez en la cadena
        if (c.indexOf(letra) != i) {
            return false;
        }
    }
    return true;
}
}

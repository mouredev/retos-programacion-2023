import java.text.Normalizer;
import java.util.HashSet;
import java.util.Scanner;

public class Alvarogtz {

    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        System.out.println("Introduce una frase a evaluar: ");
        String frase = sc.nextLine();

        if (isPangrama(frase)) {
            System.out.println("La frase es pangrama");
        } else {
            System.out.println("La frase NO es pangrama");
        }
        if (isHeterograma(frase)) {
            System.out.println("La frase es heterograma");
        } else {
            System.out.println("La frase NO es heterograma");
        }
        if (isIsograma(frase)) {
            System.out.println("La frase es isograma");
        } else {
            System.out.println("La frase NO es isograma");
        }
    }

    public static boolean isPangrama(String frase){
        HashSet<String> letras = new HashSet();

        for(int i = 0; i< frase.length(); i++) {
            char letra = frase.charAt(i);
            if (Character.toString(letra).matches("[a-z]"))
                letras.add(String.valueOf(letra));
        }

        return letras.size() == 26? true : false;
    }

    public static boolean isHeterograma(String frase){
        boolean heterograma = true;

        for(int i = 0; i< frase.length(); i++) {
            char letra = frase.charAt(i);
            if (Character.toString(letra).matches("[a-z]")) {
                for(int z = i+1; z< frase.length(); z++){
                    char letraComparar = frase.charAt(z);
                    if(Character.toString(letra).matches("[a-z]") && letra == letraComparar) {
                        heterograma = false;
                        break;
                    }
                }
            }

            if(!heterograma)
                break;
        }

        return heterograma;
    }

    public static boolean isIsograma(String frase){
        boolean isograma = true;
        int start = 1;
        int veces = 0;
        for(int i = 0; i< frase.length(); i++) {
            veces = 0;
            char letra = frase.charAt(i);
            if (Character.toString(letra).matches("[a-z]")) {
                for(int z = 0; z< frase.length(); z++){
                    char letraComparar = frase.charAt(z);
                    if(Character.toString(letra).matches("[a-z]") && letra == letraComparar) {
                        veces++;
                    }
                }

                if(i == 0)
                    start = veces;
                if(veces != start) {
                    isograma = false;
                    break;
                }
            }
        }
        return isograma;
    }

    public static String quitarCaracteresRaros(String frase) {
        frase = Normalizer.normalize(frase, Normalizer.Form.NFKD).replaceAll("[\u0300-\u0301]", "");
        return frase;
    }
}

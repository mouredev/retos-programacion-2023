package reto9HeterogramaIsogramaPangrama;

import java.util.*;
import java.util.stream.Collectors;
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 */
public class Cflorezp {

    public static void main(String[] args) {

        System.out.println("*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*");
        System.out.println("Software para identificar si una cadena de texto es un " +
                "Heterograma, un Isograma y un Pangrama");
        System.out.println("*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n");
        Scanner input = new Scanner(System.in);
        System.out.println("Por favor ingrese una cadena de texto");
        String value = input.nextLine();

        heterograma(value);
        isograma(value);
        pangrama(value);

        input.close();
    }

    public static void heterograma(String text){
        boolean verification = true;
        Set<Character> flag = new HashSet<>();
        for(char c : text.toCharArray()){
            if(!flag.add(c)){
                verification = false;
                break;
            }
        }
        if(verification){
            System.out.println("La cadena de texto ingresada es un Heterograma");
        }else{
            System.out.println("La cadena de texto ingresada no es un Heterograma");
        }
    }

    public static void isograma(String text){
        Map<Character, Long> countCharacters = text.chars()
                .mapToObj(c -> (char) c)
                .collect(Collectors.groupingBy(c -> c, Collectors.counting()));

        boolean equals = countCharacters.values().stream().distinct().limit(2)
                .count() <= 1;

        if(equals){
            System.out.println("La cadena de texto es un Isograma");
        }else{
            System.out.println("La cadena de texto no es un Isograma");
        }

    }

    public static void pangrama(String text){
        String[] alphabet = {"A", "B", "C", "D", "E", "F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"};
        boolean verification = true;
        for(String c: alphabet){
            if(!text.toUpperCase().contains(c)){
                verification = false;
                break;
            }
        }
        if(verification){
            System.out.println("La cadena de texto es un Pangrama");
        }else{
            System.out.println("La cadena de texto no es un Pangrama");
        }
    }
}

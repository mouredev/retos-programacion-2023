package reto15Aurebesh;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/*
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
 * Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
 */
public class Cflorezp {

    public static void main(String[] args) {
        System.out.println("**********************************************");
        System.out.println("Bienvenido al traductor de Español a Aurebesh\n");
        System.out.print("Escribe la palabra o frase que quieres traducir: ");

        Scanner input = new Scanner(System.in);
        String traducir = input.nextLine();

        System.out.println("Traducción: \n" + caracterAurebesh(traducir.toLowerCase()));

    }

    public static String caracterAurebesh(String frase){
        Map<String, String> aurebesh = new HashMap<>(){{
            put("a", "aurek"); put("b", "besh"); put("c", "cresh"); put("d", "dorn");
            put("e", "esk"); put("f", "forn"); put("g", "grek"); put("h", "herf");
            put("i", "isk"); put("j", "jenth"); put("k", "krill"); put("l", "leth");
            put("m", "merm"); put("n", "nern"); put("o", "osk"); put("p", "peth");
            put("q", "qek"); put("r", "resh"); put("s", "senth"); put("t", "trill");
            put("u", "usk"); put("v", "vev");    put("w", "wesk"); put("x", "xesh");
            put("y", "yirt"); put("z", "zerek");   put("ae", "enth"); put("ch","cherek");
            put("eo", "onith"); put("kh", "krenth"); put("oo", "orenth"); put("sh", "sen");
            put("th", "thesh"); put("gn", "nen"); put(" ", " "); put("ñ", "ñ");
        }};

        String duo = "";
        String provisional = "";
        StringBuilder creacionFrase = new StringBuilder();
        for(int i = 0; i < frase.length(); i++){
            if(i + 1 < frase.length()){
                duo = frase.substring(i, i + 2);
                provisional = aurebesh.get(duo);
                if(provisional == null){
                    duo = frase.substring(i, i + 1);
                    provisional = aurebesh.get(duo) == null ? duo : aurebesh.get(duo);
                    creacionFrase.append(provisional);
                }
                else{
                    creacionFrase.append(provisional);
                    i++;
                }
            }else{
                duo = frase.substring(i, i + 1);
                provisional = aurebesh.get(duo);
                creacionFrase.append(provisional);
            }
        }
        return creacionFrase.toString();
    }
}



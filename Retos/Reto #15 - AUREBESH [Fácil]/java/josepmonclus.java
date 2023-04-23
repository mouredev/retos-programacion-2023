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

public class josepmonclus {

    Scanner entrada = new Scanner(System.in);
    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        String toTranslate = "The"; //josepmonclus.getTextToTranslate();
        boolean aurebesh = false; //josepmonclus.getLanguageOfText();

        String translated = josepmonclus.transalteText(toTranslate.toLowerCase(), aurebesh);

        System.out.println("Texto traducido:");
        System.out.println(translated);
    }

    private String transalteText(String toTranslate, boolean aurebesh) {
        Map<String, String> dictAurebesh = getDictAurebesh();
        StringBuilder translated = new StringBuilder();

        int index = 0;

        if(aurebesh) {
            // Translate from aurebesh
            while (index < toTranslate.length()) {
                boolean done = false;
                //for
            }
        } else {
            // Translate to aurebesh
            while (index < toTranslate.length()) {
                if(index + 2 < toTranslate.length() && dictAurebesh.containsKey(toTranslate.substring(index, index + 2))) {
                    translated.append(dictAurebesh.get(toTranslate.substring(index, 2)));
                    index = index + 2;
                } else if(dictAurebesh.containsKey(Character.toString(toTranslate.charAt(index)))) {
                    translated.append(dictAurebesh.get(Character.toString(toTranslate.charAt(index))));
                    index++;
                } else {
                    translated.append(toTranslate.charAt(index));
                    index++;
                }
            }
        }


        return translated.toString();
    }

    private String getTextToTranslate() {
        System.out.println("Introduce el texto que quieres traducir:");

        return entrada.nextLine();
    }

    private boolean getLanguageOfText() {
        while(true){
            System.out.println("El texto es Aurebesh? [S/N]");
            String answer = entrada.nextLine();

            if(answer.toUpperCase().equals("S")){
                return true;
            } else if(answer.toUpperCase().equals("N")) {
                return false;
            } else {
                System.out.println("Respuesta incorrecta!");
            }
        }
    }

    private Map<String,String> getDictAurebesh() {
        Map<String, String> dictAurebesh = new HashMap<>();
        dictAurebesh.put("a", "aurek");
        dictAurebesh.put("b", "besh");
        dictAurebesh.put("c", "cresh");
        dictAurebesh.put("ch", "cherek");
        dictAurebesh.put("d", "dorn");
        dictAurebesh.put("e", "esk");
        dictAurebesh.put("ae", "enth");
        dictAurebesh.put("eo", "onith");
        dictAurebesh.put("f", "forn");
        dictAurebesh.put("g", "grek");
        dictAurebesh.put("h", "herf");
        dictAurebesh.put("i", "isk");
        dictAurebesh.put("j", "jenth");
        dictAurebesh.put("k", "krill");
        dictAurebesh.put("kh", "krenth");
        dictAurebesh.put("l", "lenth");
        dictAurebesh.put("m", "mern");
        dictAurebesh.put("n", "nern");
        dictAurebesh.put("ng", "nen");
        dictAurebesh.put("o", "osk");
        dictAurebesh.put("oo", "orenth");
        dictAurebesh.put("p", "peth");
        dictAurebesh.put("q", "qek");
        dictAurebesh.put("r", "resh");
        dictAurebesh.put("s", "senth");
        dictAurebesh.put("sh", "shen");
        dictAurebesh.put("t", "trill");
        dictAurebesh.put("th", "thesh");
        dictAurebesh.put("u", "usk");
        dictAurebesh.put("v", "vev");
        dictAurebesh.put("w", "wesk");
        dictAurebesh.put("x", "xesh");
        dictAurebesh.put("y", "yirt");
        dictAurebesh.put("z", "zerek");

        return dictAurebesh;
    }
}

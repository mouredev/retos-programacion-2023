import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
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

        boolean test = true;

        if(!test) {
            String toTranslate = josepmonclus.getTextToTranslate();
            boolean aurebesh = josepmonclus.getLanguageOfText();

            String translated = josepmonclus.transalteText(toTranslate.toLowerCase(), aurebesh);

            System.out.println("Texto traducido:");
            System.out.println(translated);
        } else {
            String toTranslate = "The Mouredev";
            String translated = josepmonclus.transalteText(toTranslate.toLowerCase(), false);

            System.out.println("Texto traducido:");
            System.out.println(translated);

            translated = josepmonclus.transalteText(translated, true);

            System.out.println("Texto tranducido:");
            System.out.println(translated);

            toTranslate = "Qué te ha parecido el reto? A mí me ha gustado mucho! Mañana sigue practicando.";
            translated = josepmonclus.transalteText(toTranslate.toLowerCase(), false);

            System.out.println("Texto traducido:");
            System.out.println(translated);

            translated = josepmonclus.transalteText(translated, true);

            System.out.println("Texto tranducido:");
            System.out.println(translated);
        }
    }

    private String transalteText(String toTranslate, boolean aurebesh) {
        Map<String, String> dictAurebesh = getDictAurebesh();
        StringBuilder translated = new StringBuilder();

        int index = 0;

        if(aurebesh) {
            // Translate from aurebesh
            while (index < toTranslate.length()) {
                int i = 6;
                boolean done = false;
                while(!done) {
                    if(index + i < toTranslate.length() && dictAurebesh.containsValue(toTranslate.substring(index, index + i))) {
                        for(Entry<String, String> e : dictAurebesh.entrySet()) {
                            if(e.getValue().equals(toTranslate.substring(index, index + i))) {
                                translated.append(e.getKey());
                                done = true;
                                break;
                            }
                        }
                    }
                    
                    if(i == 1 && !done) {
                        translated.append(toTranslate.substring(index, index + i));
                        done = true;
                    }
                    if(!done) i--;
                }

                index = index + i;
            }
        } else {
            // Translate to aurebesh
            while (index < toTranslate.length()) {
                if(index + 2 < toTranslate.length() && dictAurebesh.containsKey(toTranslate.substring(index, index + 2))) {
                    translated.append(dictAurebesh.get(toTranslate.substring(index, index + 2)));
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

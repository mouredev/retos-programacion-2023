import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

public class ycanas {
    public static String aurebeshTranslator(String text, boolean aurebesh) {
        Map <String, String> dictAurebesh = new LinkedHashMap <String, String>(){{
            put("a", "aurek");  put("b", "besh");    put("c", "cresh");
            put("d", "dorn");   put("e", "esk");     put("f", "forn");
            put("g", "grek");   put("h", "herf");    put("i", "isk");
            put("j", "jenth");  put("k", "krill");   put("l", "leth");
            put("m", "merm");   put("n", "nern");    put("o", "osk");
            put("p", "peth");   put("q", "qek");     put("r", "resh");
            put("s", "senth");  put("t", "trill");   put("u", "usk");
            put("v", "vev");    put("w", "wesk");    put("x", "xesh");
            put("y", "yirt");   put("z", "zerek");   put("ae", "enth");
            put("eo", "onith"); put("kh", "krenth"); put("oo", "orenth");
            put("sh", "sen");   put("th", "thesh");  put("gn", "nen");
        }};

        String translate = "";
        text = text.toLowerCase();
        int length = text.length();

        if (aurebesh) {
            translate = text;

            for (Map.Entry <String, String> map: dictAurebesh.entrySet()) {
                translate = translate.replace(map.getValue(), map.getKey());
            }
        }

        else {
            int index = 0;
            String search = "";

            while (index < length) {
                if (index < length - 1) {
                    search = text.substring(index, index + 2);
                }

                if (!dictAurebesh.containsKey(search)) {
                    search = String.valueOf(text.charAt(index));
                    index = index - 1;
                }

                translate += dictAurebesh.getOrDefault(search, search);
                index = index + 2;
                search = "";
            }
        }

        return translate;
    }

    public static void main(String[] args) {
        String aurebesh = aurebeshTranslator("Hola mundo desde Aurebesh", false);
        String spanish  = aurebeshTranslator(aurebesh, true);

        System.out.println(aurebesh + " - " + spanish);
    }
}

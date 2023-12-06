import java.util.HashMap;
import java.util.Map;

public class Aurebesh {

    public String translateToAurebesh(String sentence) {

        Map<String, String> alphabetMap = createAlphabetMap();
        StringBuilder res = new StringBuilder();
        String[] arr = sentence.split("");

        for (String s : arr) {
            if (!alphabetMap.containsKey(s)) {
                res.append(s);
                continue;
            }
            res.append(alphabetMap.get(s));
        }

        return res.toString();

    }

    public String translateFromAurebesh(String sentence) {

        Map<String, String> alphabetMap = createAlphabetMap();

        for (Map.Entry <String, String> map: alphabetMap.entrySet()) {
            sentence = sentence.replace(map.getValue(), map.getKey());
        }

        return sentence;

    }

    private static Map<String, String> createAlphabetMap(){
        Map<String, String> alphabet = new HashMap<>();
        alphabet.put("a", "aurek"); alphabet.put("b", "besh"); alphabet.put("c", "cresh"); alphabet.put("d", "dorn");
        alphabet.put("e", "esk"); alphabet.put("f", "forn"); alphabet.put("g", "grek"); alphabet.put("h", "herf");
        alphabet.put("i", "isk"); alphabet.put("j", "jenth"); alphabet.put("k", "krill"); alphabet.put("l", "leth");
        alphabet.put("m", "merm"); alphabet.put("n", "nern"); alphabet.put("o", "osk"); alphabet.put("p", "peth");
        alphabet.put("q", "qek"); alphabet.put("r", "resh"); alphabet.put("s", "senth"); alphabet.put("t", "trill");
        alphabet.put("u", "usk"); alphabet.put("v", "vev"); alphabet.put("w", "wesk"); alphabet.put("x", "xesh");
        alphabet.put("y", "yirt"); alphabet.put("z", "zerek");
        return alphabet;
    }

}

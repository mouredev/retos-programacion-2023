import java.util.HashMap;

class Bramenn {

    
    public static void main(String[] args){
        System.out.println(translateTextToHackerLanguage("LEET"));
    }

    public static String translateTextToHackerLanguage(String text){
        HashMap<String, String> hackerDictionary = new HashMap<String, String>();
        hackerDictionary.put("a", "4");
        hackerDictionary.put("b", "I3");
        hackerDictionary.put("c", "[");
        hackerDictionary.put("d", ")");
        hackerDictionary.put("e", "3");
        hackerDictionary.put("f", "|=");
        hackerDictionary.put("g", "&");
        hackerDictionary.put("h", "#");
        hackerDictionary.put("i", "1");
        hackerDictionary.put("j", ",_|");
        hackerDictionary.put("k", ">|");
        hackerDictionary.put("l", "1");
        hackerDictionary.put("m", "/\\/\\");
        hackerDictionary.put("n", "^/");
        hackerDictionary.put("o", "0");
        hackerDictionary.put("p", "|*");
        hackerDictionary.put("q", "(_,)");
        hackerDictionary.put("r", "I2");
        hackerDictionary.put("s", "5");
        hackerDictionary.put("t", "7");
        hackerDictionary.put("u", "(_)");
        hackerDictionary.put("v", "\\/");
        hackerDictionary.put("w", "\\/\\/");
        hackerDictionary.put("x", "><");
        hackerDictionary.put("y", "j");
        hackerDictionary.put("z", "2");
        hackerDictionary.put(" ", " ");
        
        String translation = "";
        
        for (char letter: text.toLowerCase().toCharArray()){
            translation += hackerDictionary.get(String.valueOf(letter));
        }

        return translation;

    }
}
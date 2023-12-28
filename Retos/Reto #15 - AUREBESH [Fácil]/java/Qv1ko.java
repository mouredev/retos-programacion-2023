import java.util.HashMap;
import java.util.Map;

public class Qv1ko {

    public static void main(String[] args) {
        String aurebeshText=aurebeshTranslator("May the force be with you!",true);
        System.out.println(aurebeshText);
        System.out.println(aurebeshTranslator(aurebeshText,false));
    }//main

    private static String aurebeshTranslator(String text,boolean toAurebesh) {
        text=text.toLowerCase();
        String translateText="";
        Map<String,String> aurebeshMap=new HashMap<String,String>() {
            {put("a","aurek");put("b","besh");put("c","cresh");put("d","dorn");put("e","esk");put("f","forn");put("g","grek");put("h","herf");put("i","isk");put("j","jenth");put("k","krill");put("l","leth");put("m","mern");put("n","nern");put("o","osk");put("p","peth");put("q","qek");put("r","resh");put("s","senth");put("t","trill");put("u","usk");put("v","vev");put("w","wesk");put("x","xesh");put("y","yirt");put("z","zerek");put("ae","enth");put("ch","cherek");put("eo","onith");put("kh","krenth");put("ng","nen");put("oo","orenth");put("sh","shen");put("th","thesh");}
        };
        Map<String,String> charsMap=new HashMap<String,String>();
        for(Map.Entry<String,String> entry:aurebeshMap.entrySet()) {
            charsMap.put(entry.getValue(),entry.getKey());
        }
        if(toAurebesh) {
            int charPosition=0;
            while(charPosition<text.length()) {
                String oneChar=Character.toString(text.charAt(charPosition));
                String twoChars="";
                if(charPosition<text.length()-1) {
                    twoChars=oneChar+Character.toString(text.charAt(charPosition+1));
                }
                if(aurebeshMap.containsKey(twoChars)) {
                    translateText+=aurebeshMap.get(twoChars);
                    charPosition+=2;
                } else {
                    translateText+=(aurebeshMap.containsKey(oneChar))? aurebeshMap.get(oneChar):Character.toString(text.charAt(charPosition));
                    charPosition++;
                }
            }
        } else {
            for(Map.Entry<String,String> entry:charsMap.entrySet()) {
                text=text.replaceAll(entry.getKey(),entry.getValue());
            }
            translateText=text;
        }
        return translateText;
    }//aurebeshTranslator

}//class

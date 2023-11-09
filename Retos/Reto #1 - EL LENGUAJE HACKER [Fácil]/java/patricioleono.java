import java.util.HashMap;
import java.util.Map;
public class patricioleono {
    public static void main(String[] args){
    Map<Character, String> hackerLang = new HashMap<>();

    hackerLang.put('A', "4");
    hackerLang.put('B', "|3");
    hackerLang.put('C', "[");
    hackerLang.put('D', ")");
    hackerLang.put('E', "3");
    hackerLang.put('F', "|=");
    hackerLang.put('G', "&");
    hackerLang.put('H', "#");
    hackerLang.put('I', "1");
    hackerLang.put('J', ",_|");
    hackerLang.put('K', ">|");
    hackerLang.put('L', "1");
    hackerLang.put('M', "/\\/\\");
    hackerLang.put('N', "^/");
    hackerLang.put('O', "0");
    hackerLang.put('P', "|*");
    hackerLang.put('Q', "(_,)");
    hackerLang.put('R', "|2");
    hackerLang.put('S', "5");
    hackerLang.put('T', "7");
    hackerLang.put('U', "(_)");
    hackerLang.put('V', "\\/");
    hackerLang.put('W', "\\/\\/");
    hackerLang.put('X', "><");
    hackerLang.put('Y', "j");
    hackerLang.put('Z', "2");

    String inputData = "Resuelto por Patricio Leon";
    String outputData = "";

    String inputUpper = inputData.toUpperCase();
    for (int i = 0; i < inputUpper.length(); i++){
        char indice = inputUpper.charAt(i);
        outputData += hackerLang.containsKey(indice) ? hackerLang.get(indice) : indice;

        System.out.println(outputData);
    }
        System.out.println(hackerLang);

    }
}

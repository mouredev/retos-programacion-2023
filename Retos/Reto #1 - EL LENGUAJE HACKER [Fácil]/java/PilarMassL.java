import java.util.HashMap;
import java.util.Optional;

public class PilarMassL {

    public static void main(String [] args){

        HashMap<String, String> hackAlphabet = new HashMap<>();
        hackAlphabet.put("a","4");
        hackAlphabet.put("b","I3");
        hackAlphabet.put("c","[");
        hackAlphabet.put("d",")");
        hackAlphabet.put("e","3");
        hackAlphabet.put("f","|=");
        hackAlphabet.put("g","&");
        hackAlphabet.put("h","#");
        hackAlphabet.put("i","1");
        hackAlphabet.put("j",",_|");
        hackAlphabet.put("k",">|");
        hackAlphabet.put("l","1");
        hackAlphabet.put("m","/\\/\\");
        hackAlphabet.put("n","^/");
        hackAlphabet.put("o","0");
        hackAlphabet.put("p","|*");
        hackAlphabet.put("q","(_,)");
        hackAlphabet.put("r","I2");
        hackAlphabet.put("s","5");
        hackAlphabet.put("t","7");
        hackAlphabet.put("u","(_)");
        hackAlphabet.put("v","\\/");
        hackAlphabet.put("w","\\/\\/");
        hackAlphabet.put("x","><");
        hackAlphabet.put("y","j");
        hackAlphabet.put("z","2");


        String inputText= "Hola mi nombre es Pilar, mucho gusto !";
        StringBuilder resultText = new StringBuilder();
        for (int j = 0; j < inputText.length(); j++) {
            final String key =  String.valueOf(inputText.toLowerCase().charAt(j));
            Optional.ofNullable(hackAlphabet.get(key))
                    .ifPresentOrElse(
                            resultText::append,
                            () -> resultText.append(key)
                    );
        }

        System.out.println(resultText);
    }

}

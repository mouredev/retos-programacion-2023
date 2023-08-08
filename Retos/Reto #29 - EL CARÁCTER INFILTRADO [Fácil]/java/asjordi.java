import java.util.ArrayList;

public class InfiltratedCharacter {

    public static ArrayList<String> find(String strOne, String strTwo){

        if (strOne.length() != strTwo.length()) throw new IllegalArgumentException("Both strings must be the same length");

        ArrayList<String> infiltratedCharacteres = new ArrayList<>();

        for (int i = 0; i < strOne.length(); i++) {
            if (strOne.charAt(i) != strTwo.charAt(i)) infiltratedCharacteres.add(Character.toString(strTwo.charAt(i)));
        }

        return infiltratedCharacteres;

    }

}

import java.util.*;
import java.lang.String;

class Magdielina {

    public static void main(String[] args) {
        System.out.println(getInfiltratorChacarters("Me llamo Magdiel Linares","Me llamo Magdiel Linares"));
    }

    private static List<Character> getInfiltratorChacarters(String text1, String text2){
        List<Character> infiltratorCharacters = new ArrayList<>();
        if(text1 != null && text2 != null && text1.length() == text2.length()) {
            int length = text1.length();
            for (int i = 0; i < length; i++){
                if (text1.charAt(i) != text2.charAt(i)){
                    infiltratorCharacters.add(text1.charAt(i));
                }
            }
        }
        return infiltratorCharacters;
    }
}
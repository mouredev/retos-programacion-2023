import java.util.Map;
import java.util.HashMap;

public class Qv1ko {

    public static void main(String[] args) {
        heterogram("the big dwarf only jumps");
        isogram("copycopycopy");
        pangram("Waxy and quivering, jocks fumble the pizza");
    }//main

    private static void heterogram(String str) {
        boolean isHeterogram=true;
        for(int letterNumber:lettersCounter(str).values()) {
            if(letterNumber!=1) {
                isHeterogram=false;
                break;
            } 
        }
        System.out.println((isHeterogram)? "The string \""+str+"\" is a heterogram":"The string \""+str+"\" is not a heterogram");
    }//heterogram

    private static void isogram(String str) {
        boolean isIsogram=true;
        int lettersValue=0;
        for(int letterNumber:lettersCounter(str).values()) {
            lettersValue=(lettersValue==0)? letterNumber:lettersValue;
            if(letterNumber!=lettersValue) {
                isIsogram=false;
                break;
            } 
        }
        System.out.println((isIsogram)? "The string \""+str+"\" is an isogram":"The string \""+str+"\" is not an isogram");
    }//isogram

    private static void pangram(String str) {
        boolean isPangram=true;
        isPangram=(lettersCounter(str).size()!=26)? false:true;
        System.out.println((isPangram)? "The string \""+str+"\" is a pangram":"The string \""+str+"\" is not a pangram");
    }//pangram

    private static Map<Character,Integer> lettersCounter(String str) {
        str=str.toLowerCase();
        Map<Character,Integer> letters=new HashMap<Character,Integer>();
        for(int i=0;i<str.length();i++) {
            if(Character.isLetter(str.charAt(i))) {
                if(letters.containsKey(str.charAt(i))) {
                    letters.put(str.charAt(i),letters.get(str.charAt(i))+1);
                } else {
                    letters.put(str.charAt(i),1);
                }
            }
        }
        return letters;
    }//lettersCounter

}//class
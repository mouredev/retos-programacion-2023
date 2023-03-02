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
        for(int i=0;i<str.length();i++) {
            if(Character.isLetter(str.charAt(i))) {
                for(int j=i+1;j<str.length();j++) {
                    if(Character.isLetter(str.charAt(j))) {
                        isHeterogram=(str.charAt(i)==str.charAt(j))? false:true;
                        if(!isHeterogram) {
                            break;
                        }
                    }
                }
            }
            if(!isHeterogram) {
                break;
            }
        }
        System.out.println(isHeterogram? "The string \""+str+"\" is a heterogram":"The string \""+str+"\" is not a heterogram");
    }//heterogram

    private static void isogram(String str) {
        Map<Character,Integer> letters=new HashMap<Character,Integer>();
        boolean isIsogram=true;
        for(int i=0;i<str.length();i++) {
            if(Character.isLetter(str.charAt(i))) {
                if(letters.containsKey(str.charAt(i))) {
                    letters.put(str.charAt(i),letters.get(str.charAt(i))+1);
                } else {
                    letters.put(str.charAt(i),1);
                }
            }
        }
        for(int i=0;i<str.length()-1;i++) {
            if(Character.isLetter(str.charAt(i))) {
                if(!(letters.get(str.charAt(i))>1&&letters.get(str.charAt(i))==letters.get(str.charAt(i+1)))) {
                    isIsogram=false;
                    break;
                }
            }
        }
        System.out.println(isIsogram? "The string \""+str+"\" is an isogram":"The string \""+str+"\" is not an isogram");
    }//isogram

    private static void pangram(String str) {
        String alphabet="abcdefghijklmnopqrstuvwxyz",letters="";
        boolean addLetter=true;
        for(int i=0;i<str.length();i++) {
            if(Character.isLetter(str.charAt(i))) {
                for(int j=0;j<letters.length();j++) {
                    if(str.toLowerCase().charAt(i)==letters.charAt(j)) {
                        addLetter=false;
                        break;
                    } else {
                        addLetter=true;
                    }
                }
                letters+=(addLetter)? str.toLowerCase().charAt(i):"";
            }
        }
        System.out.println((alphabet.length()==letters.length())? "The string \""+str+"\" is a pangram":"The string \""+str+"\" is not a pangram");
    }//pangram

}//class
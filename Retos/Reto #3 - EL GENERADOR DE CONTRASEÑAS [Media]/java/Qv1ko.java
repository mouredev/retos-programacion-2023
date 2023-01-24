import java.util.ArrayList;

public class Qv1ko {

    public static void main(String[] args) {
        passwordGenerator(21,true,false,false);
    }//main

    private static void passwordGenerator(int length,boolean uppercase,boolean numbers,boolean symbols) {
        String password="";
        length=(length<8)? 8:(length>16)? 16:length;
        ArrayList<Character> characters=new ArrayList<Character>();
        for(int i=97;i<=122;i++) {
            characters.add((char)i);
        }
        if(uppercase) {
            for(int i=65;i<=90;i++) {characters.add((char)i);}
        }
        if(numbers) {
            for(int i=48;i<=57;i++) {characters.add((char)i);}
        }
        if(symbols) {
            for(int i=33;i<=47;i++) {characters.add((char)i);}
            for(int i=58;i<=64;i++) {characters.add((char)i);}
            for(int i=91;i<=96;i++) {characters.add((char)i);}
            for(int i=123;i<=126;i++) {characters.add((char)i);}
        }
        for(int i=0;i<length;i++) {
            password+=characters.get((int)(Math.random()*characters.size()));
        }
        System.out.println(password);
    }//passwordGenerator

}//class
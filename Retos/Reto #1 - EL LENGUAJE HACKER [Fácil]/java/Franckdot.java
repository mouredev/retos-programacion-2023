package lenguaje_haker;

import java.util.Hashtable;
import java.util.Scanner;

public class Franckdot {
    public static void main(String[] args) {
        Scanner newScan = new Scanner(System.in);
        System.out.println("Ingrese un texto:");
        String newString = newScan.nextLine().toUpperCase();
        int j = 1;
        
        Hashtable newBase = new Hashtable();
        
        newBase.put("A", "4");
        newBase.put("B", "I3");
        newBase.put("C", "[");
        newBase.put("D", ")");
        newBase.put("E", "3");
        newBase.put("F", "|=");
        newBase.put("G", "&");
        newBase.put("H", "#");
        newBase.put("I", "1");
        newBase.put("J", ",_|");
        newBase.put("K", ">|");
        newBase.put("L", "1");
        newBase.put("M", "/\\/\\");
        newBase.put("N", "^/");
        newBase.put("Ñ", "^/");
        newBase.put("O", "0");
        newBase.put("P", "|*");
        newBase.put("Q", "(_,)");
        newBase.put("R", "I2");
        newBase.put("S", "5");
        newBase.put("T", "7");
        newBase.put("U", "(_)");
        newBase.put("V", "\\/");
        newBase.put("W", "\\/\\/");
        newBase.put("X", "><");
        newBase.put("Y", "j");
        newBase.put("Z", "2");
        newBase.put("0", "o");
        newBase.put("1", "L");
        newBase.put("2", "R");
        newBase.put("3", "E");
        newBase.put("4", "A");
        newBase.put("5", "S");
        newBase.put("6", "b");
        newBase.put("7", "T");
        newBase.put("8", "B");
        newBase.put("9", "g");
        newBase.put(" ", " ");
       
        for(int i=0; i<newString.length(); i++){
            if(j <= newString.length()){
                System.out.print(newBase.get(newString.substring(i, j)));
            } 
            j++;
        }
        System.out.println(" ");
    }
}

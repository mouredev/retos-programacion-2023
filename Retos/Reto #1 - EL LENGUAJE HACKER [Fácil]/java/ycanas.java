import java.util.HashMap;
import java.util.Map;

public class ycanas{
    public static String toLeet(String natural){
        String leet = "";

        Map <Character, String> data = new HashMap <Character, String> ();
        
        data.put('a', "4");
        data.put('b', "I3");
        data.put('c', "[");
        data.put('d', ")");
        data.put('e', "3");
        data.put('f', "|=");
        data.put('g', "&");
        data.put('h', "#");
        data.put('i', "1");
        data.put('j', ",_|");
        data.put('k', ">|");
        data.put('l', "1");
        data.put('m', "/\\/\\");
        data.put('n', "^/");
        data.put('o', "0");
        data.put('p', "|*");
        data.put('q', "(_,)");
        data.put('r', "I2");
        data.put('s', "5");
        data.put('t', "7");
        data.put('u', "(_)");
        data.put('v', "\\/");
        data.put('w', "\\/\\/");
        data.put('x', "><");
        data.put('y', "j");
        data.put('z', "2");

        for(char letter: natural.toCharArray()){
            if(data.containsKey(letter)){
                leet += data.get(letter);
            }
            
            else{leet += letter;}
        }

        return leet;
    }
    
    public static void main(String[] args){
        String hacker = toLeet("hola mundo desde java.");
        System.out.println(hacker);
    }
}

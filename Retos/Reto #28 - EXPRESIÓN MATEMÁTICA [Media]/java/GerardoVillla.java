
package retos;

import java.util.regex.Pattern;
import java.util.regex.Matcher;
/**
 *
 * @author luism
 */
public class GerardoVillla {
    public static void main(String[] args) {
        System.out.println("Status = " + isValidExpression("2 a 2"));
        System.out.println("Status = " + isValidExpression("5 + 6 / 7 - 4"));
        System.out.println("Status = " + isValidExpression("2 + ..22"));
        System.out.println("Status = " + isValidExpression("-2 * -1.22"));
        
    }
    
    public static boolean isValidExpression(String s){
        
        String regex = "-?\\d+(?:\\.\\d+)?\\s*[+\\-*/%]\\s*-?\\d+(?:\\.\\d+)?";

        
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(s);
        
        if(matcher.find()){
            return true;
        }else{
            return false;
        }
    }
}

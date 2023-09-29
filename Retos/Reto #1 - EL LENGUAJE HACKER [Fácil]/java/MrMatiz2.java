import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class MrMatiz2 {

    public static void main(String[] args) {
        Map hackerLanguage = initializeHackerLanguage();
        Scanner reader = new Scanner(System.in);
        System.out.print("Introduce una frase: ");
        String texto = reader.nextLine().toUpperCase();
        System.out.print("Frase en lenguaje hacker: ");
        for (int i = 0; i < texto.length(); i++) {
            System.out.print(hackerLanguage.get(texto.charAt(i)));
        }
    }


    public static Map initializeHackerLanguage(){
        Map<Character, String> hackerLanguage = new HashMap<>();
        hackerLanguage.put('A',"4");
        hackerLanguage.put('B',"I3");
        hackerLanguage.put('C',"[");
        hackerLanguage.put('D',")");
        hackerLanguage.put('E',"3");
        hackerLanguage.put('F',"|=");
        hackerLanguage.put('G',"&");
        hackerLanguage.put('H',"#");
        hackerLanguage.put('I',"1");
        hackerLanguage.put('J',",_|");
        hackerLanguage.put('K',">|");
        hackerLanguage.put('L',"1");
        hackerLanguage.put('M',"/\\/\\");
        hackerLanguage.put('N',"^/");
        hackerLanguage.put('O',"0");
        hackerLanguage.put('P',"|*");
        hackerLanguage.put('Q',"(_,)");
        hackerLanguage.put('R',"I2");
        hackerLanguage.put('S',"5");
        hackerLanguage.put('T',"7");
        hackerLanguage.put('U',"(_)");
        hackerLanguage.put('V',"\\/");
        hackerLanguage.put('W',"\\/\\/");
        hackerLanguage.put('X',"><");
        hackerLanguage.put('Y',"j");
        hackerLanguage.put('Z',"2");
        hackerLanguage.put('0',"o");
        hackerLanguage.put('1',"L");
        hackerLanguage.put('2',"R");
        hackerLanguage.put('3',"E");
        hackerLanguage.put('4',"A");
        hackerLanguage.put('5',"S");
        hackerLanguage.put('6',"b");
        hackerLanguage.put('7',"T");
        hackerLanguage.put('8',"B");
        hackerLanguage.put('9',"g");
        hackerLanguage.put(' '," ");
        return hackerLanguage;
    }
}

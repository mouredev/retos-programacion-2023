import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Alvarogtz {

    public static void main (String[] args){

        Map leetTable = getLeetTable();

        Scanner userInput = new Scanner(System.in);
        System.out.println("Introduce una frase: ");

        String alphabeticPhrase = userInput.nextLine().toUpperCase();

        for(int i = 0; i< alphabeticPhrase.toCharArray().length; i++){
            System.out.print(leetTable.get(alphabeticPhrase.toCharArray()[i]));
        }

    }

    private static Map getLeetTable() {

        Map table = new HashMap();

        table.put('A',"4");
        table.put('B',"|3");
        table.put('C',"{");
        table.put('D',"|}");
        table.put('E',"£");
        table.put('F',"|=");
        table.put('G',"[");
        table.put('H',"#");
        table.put('I',"|");
        table.put('J',"_|");
        table.put('K',"1<");
        table.put('L',"|_");
        table.put('M',"|V|");
        table.put('N',"/V");
        table.put('O',"()");
        table.put('P',"|O");
        table.put('Q',"9");
        table.put('R',"12");
        table.put('S',"$");
        table.put('T',"+");
        table.put('U',"|_|");
        table.put('V',"\\/");
        table.put('W',"(/\\)");
        table.put('X',"%");
        table.put('Y'," ¥");
        table.put('Z',"7_");
        table.put('0', "C");
        table.put('1', "L");
        table.put('2', "Z");
        table.put('3', "E");
        table.put('4', "h");
        table.put('5', "S");
        table.put('6', "b");
        table.put('7', "T");
        table.put('8', "B");
        table.put('9', "g");
        table.put(' ', " ");

        return table;
    }
}

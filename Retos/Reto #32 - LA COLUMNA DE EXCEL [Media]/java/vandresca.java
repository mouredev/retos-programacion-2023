import java.util.HashMap;
import java.util.Scanner;

public class vandresca{

    static HashMap<String, Integer> alphabet;

    public static void main(String[] args) {
        loadAlphabet();
        String column = requestColumn();
        print(findNumberColumn(column));
    }

    public static long findNumberColumn(String column){
        long numberColumn = 0;
        int columnSize = column.length();
        for(int i=0; i<columnSize; i++){
            if(i == columnSize -1){
                numberColumn +=findPosition(column.charAt(i));
            }else{
                numberColumn += findPosition(column.charAt(i))* Math.pow(alphabet.size(),columnSize-1-i);
            }
        }
        return numberColumn;
    }

    public static int findPosition(Character letterColumn){
        return alphabet.get(letterColumn.toString());
    }

    public static void loadAlphabet(){
        alphabet = new HashMap<String, Integer>();
        int index = 1;
        for(Character c = 'A'; c<='Z'; c++){
            alphabet.put(c.toString(),index);
            index++;
        }
    }

    public static String requestColumn(){
        print("Introduce la columna:");
        Scanner scanner = new Scanner(System.in);
        String column = scanner.nextLine();
        while(!column.matches("[A-Z]+")){
            print("Columna incorrecta, vuelve a introducirla:");
            column = scanner.nextLine();
        }
        scanner.close();
        return column;
    }

    public static void print(Object object){
        System.out.println(String.valueOf(object));
    }
}
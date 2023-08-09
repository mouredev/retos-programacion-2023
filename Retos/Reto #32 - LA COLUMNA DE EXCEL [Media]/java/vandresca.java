import java.util.Scanner;

public class vandresca{

    static String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String column = scanner.nextLine();
        int alphabet_size = alphabet.length();
        int column_size = column.length();

        int numberColumn = 0;
        for(int i=0; i<column_size; i++){
            if(i == column_size -1){
                numberColumn +=findPosition(column.charAt(i));
            }else{
                numberColumn += findPosition(column.charAt(i))* Math.pow(alphabet_size,column_size-i-1);
            }
        }

        System.out.println(numberColumn);
    }

    public static int findPosition(Character letterColumn){
        return alphabet.indexOf(letterColumn) + 1;
    }
}

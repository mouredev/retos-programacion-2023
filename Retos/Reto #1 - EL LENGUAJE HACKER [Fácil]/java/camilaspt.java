import java.util.Scanner;

public class camilaspt {

    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);
        String texto = read.next();
        String leetSpeak[] = {"4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|",
                ">|", "1", " M ", "^/", "0", "|*", "(_,)", "I2", "5",
                "7", "(_)", "V", "W", "><", "j", "2"};
        String abc[]        = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                "W", "X", "Y", "Z"};
        int j = 0;

        for (int i = 0; i < texto.length(); i++){
            String letra = texto.substring(i,i+1).toUpperCase(); //

            if(letra.equals(" ")){
                System.out.print(" ");
            } else {
                while (!letra.equals(abc[j]) && j < 25) { //$ != A
                    j = j + 1;
                }
                if (letra.equals(abc[j])) {
                    System.out.print(leetSpeak[j]);
                }
            }
            j = 0;
        }
    }

}
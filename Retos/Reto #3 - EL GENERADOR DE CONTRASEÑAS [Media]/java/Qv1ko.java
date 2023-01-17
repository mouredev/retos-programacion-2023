import java.util.Arrays;
import java.util.Scanner;

public class Qv1ko {

    public static void main(String[] args) {
        passwordGenerator();
    }//main

    private void passwordGenerator() {
        String password="";
        for(int i=0;i<passwordSize();i++) {

        }
        return password;
    }//passwordGenerator

    private int passwordSize() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Longuitud de la contrasena (8-16): ");
        int passSize=sc.nextInt();sc.nextLine();
        sc.close();
        return (passSize<8||passSize>16)? 8:passSize;
    }//passwordSize

    private boolean capitalLetters() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Capital letters (On/Off): ");
        String selection=sc.nextLine();
        sc.close();
        return (selection.equalsIgnoreCase("on"))? true:false;
    }//capitalLetters

    private boolean numbers() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Numbers (On/Off): ");
        String selection=sc.nextLine();
        sc.close();
        return (selection.equalsIgnoreCase("on"))? true:false;
    }//numbers

    private boolean symbols() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Symbols (On/Off): ");
        String selection=sc.nextLine();
        sc.close();
        return (selection.equalsIgnoreCase("on"))? true:false;
    }//symbols

}//class
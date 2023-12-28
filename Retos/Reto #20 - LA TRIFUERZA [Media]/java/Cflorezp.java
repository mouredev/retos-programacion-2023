package reto20LaTrifuerza;

import java.util.Scanner;

public class Cflorezp {

    public static void main(String[] args) {


        Scanner input = new Scanner(System.in);
        System.out.println("Cuantas filas desea por triangulo: ");
        String numberOfRows = input.nextLine();
        if(validationOfNumber(numberOfRows)){
            drawTriforce(Integer.parseInt(numberOfRows));
        }

        input.close();
    }

    public static boolean validationOfNumber(String number){
        if(number.equals("0") || number.equals("1") || !number.matches("[0-9]+") ){
            System.out.println("El valor ingresado no es valido!!");
            return false;
        }
        return true;
    }

    public static void drawTriforce(int n){
        String star = "*";
        int middle = ((4 * n) / 2) + 1;
        int middleSecond = (middle + 1)  / 2;
        int middleThird = middleSecond;
        int dif = (2 * n) ;
        String starSecond = "*";
        String thirdStar = "*";

        for(int i = 0; i< n; i++){
            for(int j = 1; j<= (4 * n); j++){
                if(j == middle){
                    System.out.print(star);
                    star = star.concat("**");
                    middle -= 1;
                }else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }

        for(int i = 0; i< n; i++){
            for(int j = 1; j<= (4 * n); j++){
                if(j == middleSecond){
                    System.out.print(starSecond);
                    starSecond = starSecond.concat("**");
                    middleSecond -= 1;
                }else if(j == (middleThird + dif)){
                    System.out.print(thirdStar);
                    thirdStar = thirdStar.concat("**");
                    middleThird -= 3;
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}

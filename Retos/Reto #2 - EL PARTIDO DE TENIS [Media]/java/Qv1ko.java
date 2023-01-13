import java.util.Scanner;

public class Qv1ko {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String point="";
        int player1=0,player2=0;
        do {
            do {
                System.out.print("Who got the point (P1 or P2): ");
                point=sc.nextLine();
            } while(!(point.equalsIgnoreCase("P1")||point.equalsIgnoreCase("P2")));
            if(point.equalsIgnoreCase("P1")) {
                player1++;
            } else {
                player2++;
            }
            System.out.println(scoreboard(player1,player2));
        } while(!((player1>3&&player1>player2+1)||(player2>3&&player2>player1+1)));
        sc.close();
    }//main

    private static String scoreboard(int player1,int player2) {
        String scoreboard="";
        if(player1>3&&player1==player2) {
            return "Deuce";
        } if(player1>3&&player2==(player1-1)) {
            return "Advantage P1";
        } if(player2>3&&player1==(player2-1)) {
            return "Advantage P2";
        } if(player1>3&&player2<(player1-1)) {
            return "Won the P1";
        } if(player2>3&&player1<(player2-1)) {
            return "Won the P2";
        } else {
            switch(player1) {
                case 0: scoreboard+="Love";break;
                case 1: scoreboard+="15";break;
                case 2: scoreboard+="30";break;
                case 3: scoreboard+="40";break;
            }
            scoreboard+=" - ";
            switch(player2) {
                case 0: scoreboard+="Love";break;
                case 1: scoreboard+="15";break;
                case 2: scoreboard+="30";break;
                case 3: scoreboard+="40";break;
            }
            return scoreboard;
        }
    }//scoreboard

}//class
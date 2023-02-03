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
            } while(!(point.equalsIgnoreCase("p1")||point.equalsIgnoreCase("p2")));
            player1+=(point.equalsIgnoreCase("p1"))? 1:0;
            player2+=(point.equalsIgnoreCase("p2"))? 1:0;
            scoreboard(player1,player2);
        } while(Math.abs(player1-player2)<2||player1<4&&player2<4);
        sc.close();
    }//main

    private static void scoreboard(int player1,int player2) {
        String[] values=new String[]{"Love","15","30","40"};
        boolean end=false;
        if(player1>=3&&player2>=3) {
            if(Math.abs(player1-player2)<2) {
                System.out.println((player1==player2)? "Deuce":(player1>player2)? "Advantage P1":"Advantage P2");
            } else {
                end=true;
            }
        } else {
            if(player1<4&&player2<4) {
                System.out.println(values[player1]+" - "+values[player2]);
            } else {
                end=true;
            }
        }
        System.out.println((end)? (player1>player2)? "Won the P1":"Won the P2":"");
    }//scoreboard

}//class
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;




public class UO276244 {

    public static void main(String[] args){
        System.out.println("Introduce secuencia:");

        String entradaPuntos = "";

        Scanner scanner = new Scanner(System.in);

        entradaPuntos = scanner.nextLine ();
        String[] matchPoints  = entradaPuntos
                .substring(1, entradaPuntos.length() - 1)
                .split(","); //eliminamos los [....] y dividimos por comas



        MatchGame match = new MatchGame(matchPoints, new Player(), new Player());

        match.init();


    }


}



class Player{

    public int points = 0;

    public void addPoint(){
        if(points == 30){
            points += 10;
        }else{
            points += 15;
        }
    }


    public String toString(){
        return points == 0 ? "Love" : ""+points;
    }

}




class MatchGame{

    private String points[];
    private String adFor = "";
    private Player p1;
    private Player p2;

    public MatchGame(String[] matchPoints, Player p1, Player p2){
        this.points = matchPoints;

        this.p1 = p1;
        this.p2 = p2;

    }


    public void init(){

        String winFor = "";
        for(String pointFor : points) {

            if(!adFor.isEmpty()){ //Si ya hay jugador con ventaja

                if(adFor.equals(pointFor)){ //Si el jugador con ventaja sigue marcando
                    winFor = adFor;
                    break;
                }else{ //Si el jugador con ventaja pierde el punto
                    adFor = "";
                    System.out.println("Deuce");
                }


            }
            else if(p1.points == 40 && p2.points==p1.points){ //Estan en empate y hay punto

                adFor = pointFor;
                System.out.println("Ventaja para " + pointFor);

            }else { //No hay ventaja y no estan en empate, juego normal

                switch (pointFor.trim()){
                    case "P1": p1.addPoint(); break;
                    case "P2": p2.addPoint(); break;
                }


                if(p1.points == 40 && p2.points == 40){ //Si empatan a 40
                    System.out.println("DEUCE");
                }else{
                    System.out.println(p1.toString() + " - " + p2.toString());
                }

            }


        }


        System.out.println(winFor.isEmpty() ? "No hay ganador" : "Ganador: " + winFor);

    }

}






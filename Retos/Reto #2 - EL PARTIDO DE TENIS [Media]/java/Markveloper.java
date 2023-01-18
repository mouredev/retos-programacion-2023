import java.util.ArrayList;
import java.util.Scanner;
public class Markveloper {
    public static void main(String[] args) {
        String[] points = new String[] {"Love", "15", "30", "40", "Ventaja", "Ha ganado"};
        ArrayList<String> P1 = new ArrayList<>();
        ArrayList<String> P2 = new ArrayList<>();
        boolean ganador = false;
        Scanner sc = new Scanner(System.in);
        int contP1 = 0;
        int contP2 = 0;
        P1.add(points[0]);
        P2.add(points[0]);
        while(!ganador){
            System.out.println("¿Quien ha anotado?");
            String anotador = sc.next();
            if(anotador.equalsIgnoreCase("P1")){
                    contP1 +=1;
                    P1.add(points[contP1]);
            }
            if(anotador.equalsIgnoreCase("P2")){
                    contP2 +=1;
                    P2.add(points[contP2]);
            }
            if((P1.get(P1.size() - 1).equalsIgnoreCase(P2.get(P2.size() - 1))) && (contP1 > 2 && contP2 > 2)){
                System.out.println("Deuce");
                contP1 = 3;
                contP2 = 3;
                P1.add(points[contP1]);
                P2.add(points[contP2]);
            }else if(!ganador){
                if (P1.contains("Ha ganado")){
                    System.out.println("Ha ganado P1");
                    ganador = true;
                }else if(P2.contains("Ha ganado")){
                    System.out.println("Ha ganado P2");
                    ganador = true;
                }else{
                    System.out.println(P1.get(P1.size() - 1) + " - " + P2.get(P2.size() - 1));
                }
            }
        }
    }
}

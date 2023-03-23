import java.util.Scanner;

public class EspinoLeandroo {

    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        Scanner sc = new Scanner(System.in);

        int p1 = 0;
        int p2 = 0;

        while (true) {
            String p = sc.nextLine();

            if (p.equals("P1")) {
                p1++;
            } else if (p.equals("P2")) {
                p2++;
            } else {
                System.out.println("invalid input");
            }

            if(p1 == 3 && p2 == 3){
                System.out.println("Deuce");
            }else if(p1 <= 3 && p2 <= 3){
                System.out.println(espinoLeandroo.convertPoint(p1) + " - " + espinoLeandroo.convertPoint(p2));
            }else{
                if(p1 - 1 == p2){
                    System.out.println("Ventaja P1");
                }else if(p2 - 1 == p1){
                    System.out.println("Ventaja P2");
                }else{
                    if(p1 > p2){
                        System.out.println("Ha ganado el P1");
                        break;
                    }else if(p2 > p1){
                        System.out.println("Ha ganado el P2");
                        break;
                    }else{
                        System.out.println("Deuce");
                    }
                }
            }
        }

    }

    private String convertPoint(int points){
        String text = "";

        switch (points) {
            case 0:
                text = "Love";
                break;
            case 1:
                text = "15";
                break;
            case 2:
                text = "30";
                break;
            case 3:
                text = "40";
                break;
            default:
                break;
        }
        return text;
    }

}
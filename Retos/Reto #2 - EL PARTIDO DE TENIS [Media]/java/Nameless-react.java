public class NamelessReact {

    public static void main(String[] args) {
        partidoTenis("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1");
    }

    public static void partidoTenis(String ...points) {
        String stateOne = "Love";
        String stateTwo = "Love";
        
        
        int playerOne = 0;
        int playerTwo = 0;
        
        
        for (int i = 0; i < points.length; i++) {
            if (!points[i].equals("P2") && !points[i].equals("P1")) {
                System.out.println("La entrada registrada de puntaje no es valida");
                continue;
            }
            

            int pointsOne = playerOne;
            int pointsTwo = playerTwo;
            
            
            
            if (points[i].equals("P1")) {
                playerOne += pointsOne == 30 ? 10 : 15;
                stateOne = playerOne > 40 ? "Ventaja P1" : String.valueOf(playerOne);
            } else if (points[i].equals("P2")) {
                playerTwo += pointsTwo == 30 ? 10 : 15;
                stateTwo = playerTwo > 40 ? "Ventaja P2" : String.valueOf(playerTwo);
            }  
            
            
            
            if (playerOne == playerTwo && playerTwo >= 40 && playerOne >= 40) {
                System.out.println("Deuce");
                continue;
            }
            
            if(points[i].equals("P1") && pointsOne > 40) {
                if (playerOne - playerTwo >= 30) {
                    System.out.println("Ha ganado el P1");
                    return;
                }
                
                
                System.out.println(stateOne);
                continue;
                
            } else if (points[i].equals("P2") && pointsTwo > 40) {
                if (playerTwo - playerOne >= 30) {
                    System.out.println("Ha ganado el P2");
                    return;
                }
                
                
                System.out.println(stateTwo);
                continue;
            }
            
            
            
            
            
            if (stateOne.equals("Ventaja P1") || stateTwo.equals("Ventaja P2")) {
                System.out.println(stateOne.equals("Ventaja P1") ? "Ventaja P1" : "Ventaja P2");
                continue;
            }
            System.out.println(stateOne + " - " + stateTwo);
        }
    }
}
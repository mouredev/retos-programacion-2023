public class JuanMA0190 {
    /*
    * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
    * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
    * gane cada punto del juego.
    * 
    * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
    * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
    *   15 - Love
    *   30 - Love
    *   30 - 15
    *   30 - 30
    *   40 - 30
    *   Deuce
    *   Ventaja P1
    *   Ha ganado el P1
    * - Si quieres, puedes controlar errores en la entrada de datos.   
    * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
    */
    public static void main(String[] args) {
       String[] points = {"Love", "15", "30", "40", "Ventaja ", "Ha Ganado el "};
       String[] sequences = {"P2", "P1", "P1", "P2", "P2", "P1", "P1", "P2", "P2"};
        if(validateSequences(sequences)){
            if(sequences.length >= 5){
                printMatch(points, sequences);       
            }else{
                System.out.println("No se puede iniciar el partido porque faltan secuencias.");
            }
        }else{
            System.out.println("Se ingreso una entrada invalida");
        }       
    }

    public static void printMatch(String[] points, String[] sequences){
        int pointP1 = 0;
        int pointP2 = 0;
        boolean win = false;

        System.out.println("P1 || P2");
        for (int i = 0; i < sequences.length && !win; i++) {
            if(sequences[i].equals("P1")){
                pointP1++;
            }else if(sequences[i].equals("P2")){
                pointP2++;
            }

            if(pointP1 == 4 && pointP2 == 4){
                pointP1--;
                pointP2--;
            }

            if(pointP1 == 3 && pointP2 ==3){
                System.out.println("Deuce");
                continue;
            } 

            if(pointP1 == 4 || pointP2 == 4){
                System.out.println(pointP1 == 4 ? points[4]+"P1" : points[4]+"P2");
                continue;
            }

            if(pointP1 == 5 || pointP2 == 5){
                System.out.println(pointP1 == 5 ? points[5]+"P1" : points[5]+"P2");
                win = true;
                continue;
            }

            System.out.println(points[pointP1]+" - "+points[pointP2]);
        }
    }

    public static boolean validateSequences(String[] sequences) {
        for (int i = 0; i < sequences.length; i++) {
            if(!sequences[i].equals("P1")){
                if(!sequences[i].equals("P2")){
                   return false;
                }
            } 
        }
        return true;
    }

}

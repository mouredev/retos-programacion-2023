class iago1905 {
    private static String[] partido = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2","P1","P2","P2","P2","P2"};
    private static String[] puntuaciones = {"Love", "15", "30", "40","Deuce","Ventaja " ,"Ha ganado el "};
    static int p1 = 0;
    static int p2 = 0;

    public static void main(String[] args) {
        for (String puntos : partido) {
            if (puntos.equals("P1")) {
                p1++;
            } else {
                p2++;
            }

            //Deuce
            if(p1 == 3 && p2 == 3){
                System.out.println("Deuce");
                continue;
            }

            //Ventaja
            if(p1 > 3 && p1-p2 == 1){
                System.out.println("Ventaja P1");
                continue;
            } else if(p2 > 3 && p2-p1 == 1){
                System.out.println("Ventaja P2");
                continue;
            }

            if (p1 > 3 && p1 == p2) {
                System.out.println("Deuce");
                continue;
            }

            //Ganador
            if (p1 > 4 && p1 > p2) {
                System.out.println("Ha ganado el P1");
                break;
            } else if (p2 > 5 && p2 > p1) {
                System.out.println("Ha ganado el P2");
                break;
            }

            System.out.println(puntuaciones[p1] + " - " + puntuaciones[p2]);
            
        }

        
    }
}

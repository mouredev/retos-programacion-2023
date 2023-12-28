public class camilaspt2 {

    public static void main(String[] args) {

        String partido[] = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
        String puntos[] = {"Love", "15", "30", "40", "Deuce", "Advantage", "Win"};
        int p1 = 0;
        int p2 = 0;
        for ( String point : partido) {
            if (point.equals("P1")){
                p1++;
            } else {
                p2++;
            }
            if (p1 < 3 || p2 < 3){
                if(p1 == 4 || p2 == 4){
                    System.out.println(puntos[6]);
                } else {
                    System.out.println(puntos[p1] + " - " + puntos[p2]);
                }
            } else {
                if (p1 == p2){
                    System.out.println(puntos[4]);
                }
                if (p1-p2 == 1 || p2-p1 == 1){
                    System.out.println(puntos[5]);
                }
                if (p1-p2 == 2 || p2-p1 == 2){
                    System.out.println(puntos[6]);
                }
            }
        }
    }
}
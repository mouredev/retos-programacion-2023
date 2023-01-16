package reto2PartidoTennis;

import java.util.ArrayList;
import java.util.List;

/*
       Mi algoritmo fue creado en base a una secuancia inicial
       ya definida, la funcion se ejecuta con array de strings.
*/
public class cflorezp {

    public static void main(String[] args) {

        String[] result = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};

        partidoTennis(result);
    }

    public static void partidoTennis(String[] result) {

        String[] points = {"Love", "15", "30", "40", "Ventaja", "Ha ganado"};

        List<String> p1 = new ArrayList<>();
        List<String> p2 = new ArrayList<>();

        int iteratorP1 = 0;
        int iteratorP2 = 0;
        p1.add(points[0]);
        p2.add(points[0]);
        for (String s : result) {
            if (s.equals("P1")) {
                iteratorP1 += 1;
                if (iteratorP1 == 4 && iteratorP2 <= 2) {
                    iteratorP1 += 1;
                }
                if (iteratorP2 == 4) {
                    iteratorP2 -= 1;
                    iteratorP1 -= 1;
                }
                p1.add(points[iteratorP1]);
                p2.add(points[iteratorP2]);
            }
            if (s.equals("P2")) {
                iteratorP2 += 1;
                if (iteratorP2 == 4 && iteratorP1 <= 2) {
                    iteratorP2 += 1;
                }
                if (iteratorP1 == 4) {
                    iteratorP1 -= 1;
                    iteratorP2 -= 1;
                }
                p2.add(points[iteratorP2]);
                p1.add(points[iteratorP1]);
            }
        }

        for (int j = 1; j < p1.size(); j++) {
            if (p1.get(j).equals("40") && p2.get(j).equals("40")) {
                System.out.println("Deuce");
            } else if (p1.get(j).equals("Ventaja")) {
                System.out.println(p1.get(j) + " P1");
            } else if (p2.get(j).equals("Ventaja")) {
                System.out.println(p2.get(j) + " P2");
            } else if (p1.get(j).equals("Ha ganado")) {
                System.out.println(p1.get(j) + " el P1");
            } else if (p2.get(j).equals("Ha ganado")) {
                System.out.println(p2.get(j) + " el P2");
            } else {
                System.out.println(p1.get(j) + " - " + p2.get(j));
            }
        }
    }


}

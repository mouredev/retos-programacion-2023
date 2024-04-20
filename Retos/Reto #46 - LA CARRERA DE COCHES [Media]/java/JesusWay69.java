package reto_46;


/*
 * Crea un programa que simule la competición de dos coches en una asphalt.
 * - Los dos coches estarán representados por 🚙 y 🚗. Y la targetLine por 🏁.
 * - Cada asphalt tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
 * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
 * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
 *   🏁____🌲_____🚙
 *   🏁_🌲____🌲___🚗
 * 
 * El juego se desarrolla por turnos de forma automática, y cada segundo
 * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
 * uno de ellos (o los dos a la vez) llega a la targetLine.
 * - Acciones:
 *   - Avanzar entre 1 a 3 posiciones hacia la targetLine.
 *   - Si al avanzar, el coche finaliza en la posición de un árbol,
 *     se muestra 💥 y no avanza durante un turno.
 *   - Cada turno se imprimen las pistas y sus elementos.
 *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
 */
public class JesusWay69 {

    public static void main(String[] args) throws InterruptedException {
        int roadLeight = 100;
        String[] pista1 = new String[roadLeight];
        String[] pista2 = new String[roadLeight];
        String car1 = Character.toString(0x1F699);
        String car2 = Character.toString(0x1F697);
        String tree = Character.toString(0x1F332);
        String targetLine = Character.toString(0x1F3C1);
        String asphalt = "_";
        String[] startRace1 = createRace(pista1, car1, tree, targetLine, asphalt);
        String[] startRace2 = createRace(pista2, car2, tree, targetLine, asphalt);
        carrera(startRace1, startRace2);

    }

    public static String[] createRace(String[] track, String car,
            String tree, String targetLine, String asphalt) throws InterruptedException {

        int treeAmount = (int) (Math.random() * 3 + 1);
        int treePosition = 0;
        track[0] = targetLine;
        for (int i = 1; i <= track.length - 2; i++) {
            track[i] = asphalt;
        }
        track[track.length - 1] = car;
        for (int i = 0; i < treeAmount; i++) {
            treePosition = (int) (Math.random() * track.length + 1);
            track[treePosition] = tree;
        }
        print(track);

        return track;
    }

    public static void print(String[] pista) {
        for (String i : pista) {
            System.out.print(i);
        }
        System.out.println("\n");

    }

    public static void carrera(String[] track1, String[] track2) throws InterruptedException {
        int position1 = track1.length - 1;
        int position2 = track2.length - 1;
        int treePosition1 = 0;
        int treePosition2 = 0;
        boolean crash1 = false;
        boolean crash2 = false;
        while (position1 > 0 && position2 > 0) {
            Thread.sleep(300);
            track1[position1] = "_";
            track2[position2] = "_";

            if (crash1 == true) {
                track1[position1] = Character.toString(0x1F699); //coche1
                treePosition1 = position1;//guardamos la posición del ábol con el que se ha chocado
                crash1 = false;
                
            } else if (crash1 == false) {
                position1 -= (int) (Math.random() * 2 + 1);
                track1[treePosition1] = Character.toString(0x1F332);//volvemos a imprimir el árbol donde estaba
                if (Character.toString(0x1F332).equals(track1[position1])) {
                    track1[position1] = Character.toString(0x1F480);
                } else {
                    track1[position1] = Character.toString(0x1F697); //coche 1 
                }
            }

            if (crash2 == true) {
                track2[position2] = Character.toString(0x1F697); //coche2
                treePosition2 = position2;//guardamos la posición del ábol con el que se ha chocado
                crash2 = false;
            } else if (crash2 == false) {
                position2 -= (int) (Math.random() * 2 + 1);
                track2[treePosition2] = Character.toString(0x1F332);//volvemos a imprimir el árbol donde estaba
                if (Character.toString(0x1F332).equals(track2[position2])) {
                    track2[position2] = Character.toString(0x1F480); //choque
                    crash2 = true;
                } else {
                    track2[position2] = Character.toString(0x1F697); //coche 2
                }
            }

            if (position1 <= 2) {
                track1[1] = Character.toString(0x1F699);
                track1[0] = Character.toString(0x1F3C1);
                System.out.println("\n\n\n\n\n\n\n\n\n\n");
                print(track1);
                print(track2);
                System.out.println("Ganador: Coche1");

                break;

            } else if (position2 <= 2) {
                track2[1] = Character.toString(0x1F697);
                track2[0] = Character.toString(0x1F3C1);
                System.out.println("\n\n\n\n\n\n\n\n\n\n");
                print(track1);
                print(track2);
                System.out.println("Ganador: Coche2");

                break;
            }

            System.out.println("\n\n\n\n\n\n\n\n\n\n");
            print(track1);
            print(track2);

        }

    }

}

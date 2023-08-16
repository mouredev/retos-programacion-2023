import java.util.Scanner;

public class Alvarogtz {

    final static int DERECHA = 1;
    final static int IZQUIERDA = 2;
    final static int ABAJO = 3;
    final static int ROTAR = 4;
    final static int SALIR = 5;

    static int positionX = 0;
    static int positionY = 0;
    static int status = 0;

    public static void main(String args[]){
        boolean fin = false;

        boolean[][] pieza = incluyePieza();

        do {
            pintaJuego(pieza);
            int opcion = pintaMenu();

            switch (opcion){
                case DERECHA:
                    positionX++;
                    if(!comprobarMovimiento())
                        positionX--;
                    pieza = incluyePieza();
                    break;

                case IZQUIERDA:
                    positionX--;
                    if(!comprobarMovimiento())
                        positionX++;
                    pieza = incluyePieza();
                    break;

                case ABAJO:
                    positionY++;
                    if(!comprobarMovimiento())
                        positionY--;
                    pieza = incluyePieza();
                    break;

                case ROTAR:
                    if(status != 3)
                        status++;
                    else
                        status = 0;
                    if(comprobarMovimiento())
                        pieza = incluyePieza();
                    else
                        if(status == 3)
                            status = 0;
                        else
                            status--;
                    break;

                case SALIR:
                    fin = true;
                    break;
            }

            if(((status == 0 || status == 2) && positionY + 1 == 9)
                || ((status == 1 || status == 3) &&  positionY + 2 == 9)) {
                fin = true;
                pintaJuego(pieza);
            }

        }while(fin == false);

        System.out.println("- FIN DEL JUEGO - ");
    }

    private static void pintaJuego(boolean[][] pieza){
        for (int y = 0; y <= pieza.length - 1; y++) {
            for (int x = 0; x <= pieza.length - 1; x++) {
                if(pieza[y][x])
                    System.out.print("\uD83D\uDD33");
                else
                    System.out.print("\uD83D\uDD32");

                if (x == 9)
                    System.out.print("\n");
            }
        }
    }

    private static boolean comprobarMovimiento() {
        if((status == 0 || status == 2) && (positionX + 2 > 9 || positionX < 0 || positionY + 1 > 9))
            return false;
        else if((status == 1 || status == 3) && (positionX + 1 > 9 || positionX < 0 || positionY + 2 > 9))
            return false;
        else
            return true;
    }

    private static boolean[][] incluyePieza() {
        boolean [][] pieza = new boolean[10][10];

        switch (status){
            case 0:
                pieza[positionY][positionX] = true;
                pieza[positionY + 1][positionX] = true;
                pieza[positionY + 1][positionX + 1] = true;
                pieza[positionY + 1][positionX + 2] = true;
            break;
            case 1:
                pieza[positionY][positionX] = true;
                pieza[positionY][positionX + 1] = true;
                pieza[positionY + 1][positionX] = true;
                pieza[positionY + 2][positionX] = true;
                break;
            case 2:
                pieza[positionY][positionX] = true;
                pieza[positionY][positionX + 1] = true;
                pieza[positionY][positionX + 2] = true;
                pieza[positionY + 1][positionX + 2] = true;
                break;
            case 3:
                pieza[positionY][positionX + 1] = true;
                pieza[positionY + 1][positionX + 1] = true;
                pieza[positionY + 2][positionX + 1] = true;
                pieza[positionY + 2][positionX] = true;
                break;
        }

        return pieza;
    }

    public static int pintaMenu(){
        Scanner sc = new Scanner(System.in);
        String opciones = "1: Derecha - 2: Izquierda - 3: Baja - 4: Rota - 5: Salir :";
        boolean opcionCorrecta = false;
        int respuesta = 0;

        while(!opcionCorrecta) {
            System.out.println(opciones);
            try{
                respuesta = sc.nextInt();
                opcionCorrecta = true;
            }catch(Exception e){
                System.out.println("Opcion incorrecta");
            }
        }

        return respuesta;
    }
}

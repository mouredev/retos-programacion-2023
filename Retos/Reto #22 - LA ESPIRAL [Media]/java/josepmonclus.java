/*
 * Crea una función que dibuje una espiral como la del ejemplo.
 * - Únicamente se indica de forma dinámica el tamaño del lado.
 * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
 *
 * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
 * ════╗
 * ╔══╗║
 * ║╔╗║║
 * ║╚═╝║
 * ╚═══╝
 */

public class josepmonclus {

    private static final String horizontal = "═";
    private static final String vertical = "║";
    private static final String topleft = "╔";
    private static final String topright = "╗";
    private static final String botleft = "╚";
    private static final String botright = "╝";

    public static void main(String[] args) {
        josepmonclus josepmonclus = new josepmonclus();

        josepmonclus.doEspiral(2);

        josepmonclus.doEspiral(5);

        josepmonclus.doEspiral(10);

        josepmonclus.doEspiral(25);
    }

    private void doEspiral(int lado) {
        String[][] espiral = new String[lado][lado];

        // Direccion puede ser R (to Right), L (to Left), T (to Top), B (to Bottom), empezamos en (0,0) hacia la derecha (R)
        String direccion = "R";

        int row = 0;
        int col = 0;

        while(!isEspiralCompletada(espiral)) {
            switch (direccion) {
                case "R":
                    if (col + 1 == espiral.length || espiral[row][col + 1] != null) {
                        espiral[row][col] = topright;
                        direccion = "B";
                        row++;
                    } else {
                        espiral[row][col] = horizontal;
                        col++;
                    }

                    break;
                case "B":
                    if (row + 1 == espiral.length || espiral[row + 1][col] != null) {
                        espiral[row][col] = botright;
                        direccion = "L";
                        col--;
                    } else {
                        espiral[row][col] = vertical;
                        row++;
                    }

                    break;
                case "L":
                    if(col == 0 || espiral[row][col - 1] != null) {
                        espiral[row][col] = botleft;
                        direccion = "T";
                        row--;
                    } else {
                        espiral[row][col] = horizontal;
                        col--;
                    }

                    break;
                case "T":
                    if(row == 0 || espiral[row - 1][col] != null) {
                        espiral[row][col] = topleft;
                        direccion = "R";
                        col++;
                    } else {
                        espiral[row][col] = vertical;
                        row--;
                    }
                    break;
                default:
                    break;
            }
        }

        printEspiral(espiral);
    }

    private void printEspiral(String[][] espiral) {
        for(int i = 0; i < espiral.length; i++) {
            StringBuilder sb = new StringBuilder();

            for(int j = 0; j < espiral.length; j++) {
                sb.append(espiral[i][j]);
            }

            System.out.println(sb);
        }
    }

    private boolean isEspiralCompletada(String[][] espiral) {
        boolean isCompletada = true;

        for(int i = 0; i < espiral.length; i++) {
            for(int j = 0; j < espiral.length; j++) {
                if(espiral[i][j] == null) {
                    isCompletada = false;
                    break;
                }
            }
        }
        
        return isCompletada;
    }
}
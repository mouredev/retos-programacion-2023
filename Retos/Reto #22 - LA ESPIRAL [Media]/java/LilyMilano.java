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

class Spiral {
    public static void main(String[] args) {
        int sideLength = 5;
        char[][] matrix = new char[sideLength][sideLength];

        int rowStart = 0;
        int rowEnd = sideLength - 1;
        int colStart = 0;
        int colEnd = sideLength - 1;
        char symbol = '═';

        while (rowStart <= rowEnd && colStart <= colEnd) {
            // Draw top row
            for (int i = colStart; i <= colEnd; i++) {
                matrix[rowStart][i] = symbol;
            }
            rowStart++;

            // Draw right column
            for (int i = rowStart; i <= rowEnd; i++) {
                matrix[i][colEnd] = symbol;
            }
            colEnd--;

            // Draw bottom row
            if (rowStart <= rowEnd) {
                for (int i = colEnd; i >= colStart; i--) {
                    matrix[rowEnd][i] = symbol;
                }
                rowEnd--;
            }

            // Draw left column
            if (colStart <= colEnd) {
                for (int i = rowEnd; i >= rowStart; i--) {
                    matrix[i][colStart] = symbol;
                }
                colStart++;
            }

            // Change symbol for the next iteration
            switch (symbol) {
                case '═':
                    symbol = '║';
                    break;
                case '║':
                    symbol = '╗';
                    break;
                case '╗':
                    symbol = '╔';
                    break;
                case '╔':
                    symbol = '╝';
                    break;
                case '╝':
                    symbol = '╚';
                    break;
                case '╚':
                    symbol = '═';
                    break;
            }
        }

        // Print the matrix
        for (int i = 0; i < sideLength; i++) {
            for (int j = 0; j < sideLength; j++) {
                System.out.print(matrix[i][j]);
            }
            System.out.println();
        }
    }
}
public class Triforce {

    public static void main(String[] args) {
        print(3);
    }

    public static void print(int rows){
        for (int row = 0; row < rows * 2; row++) {
            if (row < rows) {
                String startSpace = " ".repeat(((2 * rows) - 1) - row);
                String printRow = "*".repeat((2 * (row + 1)) - 1);
                System.out.println(startSpace + printRow);
            } else {
                int currentRow = row - rows;
                String startSpace = " ".repeat((rows - currentRow) - 1);
                String middleSpace = " ".repeat((2 * (rows - currentRow)) - 1);
                String printRow = "*".repeat((2 * (currentRow + 1)) - 1);
                System.out.println(startSpace + printRow + middleSpace + printRow);
            }
        }
    }
}

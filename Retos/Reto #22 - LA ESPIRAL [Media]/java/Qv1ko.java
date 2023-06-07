public class Qv1ko {

    public static void main(String[] args) {
        spiral(5);
    }

    private static void spiral(int side) {
        String spiral = "";
        boolean horizontal = true;
        for (int row = 0; row < side; row++) {
            spiral = "";
            for (int column = 0; column < side; column++) {
                if (row + column == side - 1) {
                    spiral += (column >= row) ? "╗" : "╚";
                    horizontal = (column < row) ? true : false;
                } else if (row - column == 1 && row <= (side / 2)) {
                    spiral += "╔";
                    horizontal = true;
                } else if (row == column && row >= (side / 2)) {
                    spiral += "╝";
                    horizontal = false;
                } else {
                    spiral += (horizontal) ? "═" : "║";
                }
            }
            System.out.println(spiral);
        }
    }

}

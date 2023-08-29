public class Spiral {

    public static void createSpiral(int size){

        String spiral;
        boolean horizontal = true;

        for (int i = 0; i < size; i++) {

            spiral = "";

            for (int j = 0; j < size; j++) {
                if (i + j == size - 1) {
                    spiral += (j >= i) ? "╗" : "╚";
                    horizontal = (j < i);
                } else if (i - j == 1 && i <= (size / 2)) {
                    spiral += "╔";
                    horizontal = true;
                } else if (i == j && i >= (size / 2)) {
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

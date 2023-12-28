public class Qv1ko {

    public static void main(String[] args) {
        triforce(3);
    }

    private static void triforce(int rows) {
        String content = "", leftSpace = "", midSpace = "";
        int contentLoop = 0, spaceLoop = 0, currentRow = 0;
        for (int i = 0; i <= (rows * 2); i++) {
            leftSpace = "";
            content = "";
            if (i <= rows) {
                spaceLoop = (2 * (rows + 1)) - 1 - i;
                while (spaceLoop > 0) {
                    leftSpace += " ";
                    spaceLoop--;
                }
                contentLoop = (2 * i) - 1;
                while (contentLoop > 0) {
                    content += "*";
                    contentLoop--;
                }
                System.out.println(leftSpace + content);
            } else {
                midSpace = " ";
                currentRow = i - rows;
                spaceLoop = (2 * (rows + 1)) - 1 - i;
                while (spaceLoop > 0) {
                    leftSpace += " ";
                    spaceLoop--;
                }
                spaceLoop = 2 * (rows - currentRow);
                while (spaceLoop > 0) {
                    midSpace += " ";
                    spaceLoop--;
                }
                contentLoop = (2 * currentRow) - 1;
                while (contentLoop > 0) {
                    content += "*";
                    contentLoop--;
                }
                System.out.println(leftSpace + content + midSpace + content);
            }
        }
    }

}

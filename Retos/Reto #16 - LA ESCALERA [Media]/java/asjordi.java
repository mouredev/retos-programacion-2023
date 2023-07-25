public class Stairs {

    public static void main(String[] args) {

        Stairs s = new Stairs();
        int num = 10;

        if (num >= 0) System.out.println(s.createFromRight(num));
        if (num < 0) System.out.println(s.createFromLeft(num));

    }

    private final StringBuilder stair = new StringBuilder();
    private final String blankSpace = " ";

    public String createFromRight(int num){

        if (num == 0) return "__";

        String stairRight = "_| ";

        this.stair.append(this.blankSpace.repeat((num * 2))).append("_\n");

        for (int i = num - 1; i >= 0; i--) {
            this.stair.append(this.blankSpace.repeat((i * 2))).append(stairRight).append("\n");
        }

        return this.stair.toString();

    }

    public String createFromLeft(int num){

        String stairLeft = " |_";
        num = Math.abs(num);

        this.stair.append("_\n");

        for (int i = 0; i < num; i++) {
            this.stair.append(this.blankSpace.repeat((i * 2))).append(stairLeft).append("\n");
        }

        return this.stair.toString();

    }

}

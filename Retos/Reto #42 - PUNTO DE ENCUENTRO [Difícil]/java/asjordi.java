public class MeetingPoint {

    public static void main(String[] args) {
        String res1 = MeetingPoint.collision(
                new double[]{0, 0},
                new double[]{1, 1},
                new double[]{1, 2},
                new double[]{0, 1}
        );

        String res2 = MeetingPoint.collision(
                new double[]{2, 0},
                new double[]{0, 1},
                new double[]{0, 2},
                new double[]{1, 0}
        );

        String res3 = MeetingPoint.collision(
                new double[]{0, 0},
                new double[]{10, 5},
                new double[]{100, 50},
                new double[]{-5, -2.5}
        );

        System.out.println(res1);
        System.out.println(res2);
        System.out.println(res3);
    }

    public static String collision(double[] positionA, double[] speedA, double[] positionB, double[] speedB) {

        double xa = positionA[0];
        double ya = positionA[1];
        double xb = positionB[0];
        double yb = positionB[1];
        double sxa = speedA[0];
        double sya = speedA[1];
        double sxb = speedB[0];
        double syb = speedB[1];
        double tx = 0;
        double ty = 0;
        double time = 0;
        double x = 0;
        double y = 0;

        if ((sxa - sxb) == 0) {
            if (xa == xb) tx = 0;
            else return "Objects are not intercepted.";
        } else {
            tx = (xb - xa) / (sxa - sxb);
        }

        if ((sya - syb) == 0) {
            if (ya == yb) ty = 0;
            else return "Objects are not intercepted.";
        } else {
            ty = (yb - ya) / (sya - syb);
        }

        if (tx == ty) {
            time = tx;
            x = xa + sxa * tx;
            y = ya + sya * ty;
            return String.format("The objects intersect at the point ({%f}, {%f}) and in time {%f}.", x, y, time);
        } else {
            return "Objects are not intercepted.";
        }
    }

}

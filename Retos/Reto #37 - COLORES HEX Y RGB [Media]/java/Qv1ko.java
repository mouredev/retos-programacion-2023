public class Qv1ko {

    public static void main(String[] args) {

        toHex(55, 235, 55);
        toRGB("#37EB37");

    }

    private static void toHex(int red, int green, int blue) {

        System.out.println(String.format("#%02x%02x%02x", red, green, blue));

    }

    private static void toRGB(String hex) {

        int red = Integer.valueOf(hex.substring(1, 3), 16);
        int green = Integer.valueOf(hex.substring(3, 5), 16);
        int blue = Integer.valueOf(hex.substring(5, 7), 16);

        System.out.println("r: " + red + ", g: " + green + ", b: " + blue);

    }

}

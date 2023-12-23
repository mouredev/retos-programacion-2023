import java.util.ArrayList;
import java.util.List;

public class Convert {

    public static void main(String[] args) {
        System.out.println(toHEX(19, 162, 214));
        System.out.println(toRGB("#13a2d6"));

    }

    public static String toRGB(String hex){
        List<String> pos = new ArrayList<>();
        hex = hex.replace("#", "");

        if (hex.length() != 6) throw new IllegalArgumentException("Invalid length");

        for (int i = 0; i < hex.length(); i += 2) pos.add(hex.substring(i, Math.min(hex.length(), i + 2)));

        return String.format("r: %d, g: %d, b: %d",
                Integer.parseInt(pos.get(0), 16),
                Integer.parseInt(pos.get(1), 16),
                Integer.parseInt(pos.get(2), 16));
    }

    public static String toHEX(int r, int g, int b){
        return "#" +
                Integer.toHexString(r) +
                Integer.toHexString(g) +
                Integer.toHexString(b);
    }
}

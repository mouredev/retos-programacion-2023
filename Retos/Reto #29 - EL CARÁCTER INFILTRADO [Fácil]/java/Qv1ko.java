import java.util.ArrayList;

public class Qv1ko {

    public static void main(String[] args) {
        infiltrating("The infiltrated character", "The infiltr4ted-character");
    }

    private static void infiltrating(String base, String str) {

        ArrayList<String> infiltrators = new ArrayList<String>();

        if (base.length() == str.length()) {

            for (int i = 0; i < base.length(); i++) {

                if (base.charAt(i) != str.charAt(i)) {
                    infiltrators.add(Character.toString(str.charAt(i)));
                }

            }

        }

        System.out.println(infiltrators);

    }

}

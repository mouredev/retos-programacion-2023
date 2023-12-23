public class AnNavNicolas {
    public static void main(String[] args) {

        String text = "sol";
        permutar(text, "");

    }

    public static void permutar(String text, String response) {

        if (text.isBlank() || text.length() < 1) {
            System.out.println(response);
            return;
        }

        for (int i = 0; i < text.length(); i++) {
            String current_letter = String.valueOf(text.charAt(i));
            String left = text.substring(0, i);
            String rigth = text.substring(i + 1);
            permutar(left + rigth, response + current_letter);
        }
    }
}

public class Qv1ko {

    public static void main(String[] args) {
        encrypt("Lorem ipsum dolor sit amet.", 6);
        decrypt("gjmzh dknph yjgjm ndo vhzo.", 21);
    }

    private static void encrypt(String text, int number) {
        String result = "";
        char[] letters = text.toLowerCase().toCharArray();
        for(char letter : letters) {
            result += (char)((letter < 97 || letter > 122)? letter : (letter + number > 122)? letter + number - 26 : letter + number);
        }
        System.out.println(result);
    }

    private static void decrypt(String cesar, int number) {
        String result = "";
        char[] letters = cesar.toLowerCase().toCharArray();
        for(char letter : letters) {
            result += (char)((letter < 97 || letter > 122)? letter : (letter - number < 97)? letter - number + 26 : letter - number);
        }
        System.out.println(result);
    }

}
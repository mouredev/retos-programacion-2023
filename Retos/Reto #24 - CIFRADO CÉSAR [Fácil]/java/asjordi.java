public class CaesarCipher {

    public static final String ALPHABET = "abcdefghijklmnopqrstuvwxyz";

    public static String encrypt(String text, int shift){
        text = text.toLowerCase();
        StringBuilder encryptStr = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            int pos = ALPHABET.indexOf(text.charAt(i));
            int encryptPos = (shift + pos) % 26;
            char encryptChar = ALPHABET.charAt(encryptPos);
            encryptStr.append(encryptChar);
        }

        return encryptStr.toString();
    }

    public static String decrypt(String text, int shift){
        text = text.toLowerCase();
        StringBuilder decryptStr = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            int pos = ALPHABET.indexOf(text.charAt(i));
            int decryptPos = (pos - shift) % 26;

            if (decryptPos < 0) decryptPos = ALPHABET.length() + decryptPos;
            char decryptChar = ALPHABET.charAt(decryptPos);

            decryptStr.append(decryptChar);
        }

        return decryptStr.toString();
    }

}

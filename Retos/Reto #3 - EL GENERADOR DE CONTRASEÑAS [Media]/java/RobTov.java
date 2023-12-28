import java.util.Random;

class RobTov {
    public static void main(String[] args) {
        System.out.println(passwordGenerator(8, false, false, false));
        System.out.println(passwordGenerator(9, true, false, false));
        System.out.println(passwordGenerator(10, false, true, false));
        System.out.println(passwordGenerator(11, false, false, true));
        System.out.println(passwordGenerator(12, true, true, false));
        System.out.println(passwordGenerator(13, true, false, true));
        System.out.println(passwordGenerator(14, false, true, true));
        System.out.println(passwordGenerator(16, true, true, true));
        System.out.println(passwordGenerator(7, true, true, true));

    }

    public static String passwordGenerator(int len, boolean up, boolean dig, boolean sym) {
        if (len < 8 || len > 16) {
            throw new IllegalArgumentException("Debe de tener entre 8 y 16 caracteres.");
        }

        final String digits = "0123456789";
        final String symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
        final String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        StringBuilder psswrd = new StringBuilder();
        String valList = alphabet.toLowerCase();

        if (up)
            valList += alphabet;
        if (dig)
            valList += digits;
        if (sym)
            valList += symbols;

        for (int i = 0; i < len; i++) {
            int index = new Random().nextInt(valList.length());
            psswrd.append(valList.charAt(index));
        }

        return psswrd.toString();
    }
}
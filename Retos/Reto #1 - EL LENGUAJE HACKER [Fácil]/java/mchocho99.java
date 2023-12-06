    private static final Map<Character,String> DICTIONARY = new HashMap<>() {{
        put('A', "4");
        put('B', "I3");
        put('C', "[");
        put('D', ")");
        put('E', "3");
        put('F', "|=");
        put('G', "&");
        put('H', "#");
        put('I', "1");
        put('J', ",_|");
        put('K', ">|");
        put('L', "£");
        put('M', "/\\/\\");
        put('N', "^/");
        put('O', "0");
        put('P', "|*");
        put('Q', "(_,)");
        put('R', "I2");
        put('S', "5");
        put('T', "7");
        put('U', "(_)");
        put('V', "\\/");
        put('W', "\\/\\/");
        put('X', "><");
        put('Y', " j");
        put('Z', "2");
        put('0', "o");
        put('1', "L");
        put('2', "R");
        put('3', "E");
        put('4', "A");
        put('5', "S");
        put('6', "b");
        put('7', "T");
        put('8', "B");
        put('9', "g");
        put(' ', " ");
    }};

    public static void reto1 (String text) {
        /*
         * Escribe un programa que reciba un texto y transforme lenguaje natural a
         * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
         *  se caracteriza por sustituir caracteres alfanuméricos.
         * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
         *   con el alfabeto y los números en "leet".
         *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
         */
        String upperText = text.toUpperCase();
        for (int i = 0; i < upperText.length(); i++) {
            System.out.print(DICTIONARY.get(upperText.charAt(i)));
        }
    }

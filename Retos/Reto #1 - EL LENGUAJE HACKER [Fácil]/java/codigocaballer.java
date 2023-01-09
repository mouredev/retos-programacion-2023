import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class codigocaballer {
    public static final String TestInputText = "abcdefghijklmnñopqrstuvwxyz1234567890=?¿_:,<ºª!|·#$~%&¬/()+*ç-";
    public static final String TestBasicOutputText = "4bcd3fgh1jklmnñ0pqrst(_)vwxyzLREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*ç-";

    public static final String TestAdvancedOutputText = "@!3<[)e|=_(_+#!_||<|_]\\/[[\\]ñ[]|º9125']['|_|\\/\\_:_/><\\/-/_LREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*ç-";

    public static final String TestIntermediateOutputText = "4I3[|)3ph6#1]|<1/\\/\\|\\|ñ0|>0_I257(_)\\/\\/\\/><j2LREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*ç-";    

    public static final String TestFullRetardOutputText = "/\\!3©|}€phgee1-1!_||{|_]\\/[<\\>ñoh|º212es†µ|/'×\\|/7_LREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*ç-";

    public static final String TestInputTextUpper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890=?¿_:,<ºª!|·#$~%&¬/()+*Ç-";
    public static final String TestBasicOutputUpper = "4bcd3fgh1jklmnÑ0pqrst(_)vwxyzLREASbTBgo=?¿_:,<ºª!|·#$~%&¬/()+*Ç-";

    public static final Map<String, String> leetNumbers = Stream.of(new String[][] {
            { "1", "L" }, { "2", "R" }, { "3", "E" }, { "4", "A" },
            { "5", "S" }, { "6", "b" }, { "7", "T" }, { "8", "B" },
            { "9", "g" }, { "0", "o" },
    }).collect(Collectors.toMap(data -> data[0], data -> data[1]));

    public static final Map<String, String> leetAlphabetBasic = Stream.of(new String[][] {
            { "a", "4" }, { "e", "3" }, { "i", "1" }, { "o", "0" }, { "u", "(_)" }
    }).collect(Collectors.toMap(data -> data[0], data -> data[1]));

    public static final Map<String, String> leetAlphabetAdvanced = Stream.of(new String[][] {
            { "a", "@" }, { "b", "!3" }, { "c", "<" }, { "d", "[)" }, { "e", "e" }, { "f", "|=_" },
            { "g", "(_+" }, { "h", "#" }, { "i", "!" }, { "j", "_|" }, { "k", "|<" }, { "l", "|_" },
            { "m", "]\\/[" }, { "n", "[\\]" }, { "\u00F1", "\u00F1" }, { "o", "[]" }, { "p", "|\u00BA" },
            { "q", "9" },
            { "r", "12" }, { "s", "5" }, { "t", "']['" }, { "u", "|_|" }, { "v", "\\/" }, { "w", "\\_:_/" },
            { "x", "><" }, { "y", "\\/" }, { "z", "-/_" }
    }).collect(Collectors.toMap(data -> data[0], data -> data[1]));

    public static final Map<String, String> leetAlphabetIntermediate = Stream.of(new String[][] {
            { "a", "4" }, { "b", "I3" }, { "c", "[" }, { "d", "|)" }, { "e", "3" }, { "f", "ph" },
            { "g", "6" }, { "h", "#" }, { "i", "1" }, { "j", "]" }, { "k", "|<" }, { "l", "1" },
            { "m", "/\\/\\" }, { "n", "|\\|" }, { "\u00F1", "\u00F1" }, { "o", "0" }, { "p", "|>" },
            { "q", "0_" },
            { "r", "I2" }, { "s", "5" }, { "t", "7" }, { "u", "(_)" }, { "v", "\\/" }, { "w", "\\/\\/" },
            { "x", "><" }, { "y", "j" }, { "z", "2" }
    }).collect(Collectors.toMap(data -> data[0], data -> data[1]));

    public static final Map<String, String> leetAlphabetFullRetard = Stream.of(new String[][] {
            { "a", "/\\" }, { "b", "!3" }, { "c", "\u00A9" }, { "d", "|}" }, { "e", "\u20AC" },
            { "f", "ph" },
            { "g", "gee" }, { "h", "1-1" }, { "i", "!" }, { "j", "_|" }, { "k", "|{" }, { "l", "|_" },
            { "m", "]\\/[" }, { "n", "<\\>" }, { "\u00F1", "\u00F1" }, { "o", "oh" }, { "p", "|\u00BA" },
            { "q", "2" },
            { "r", "12" }, { "s", "es" }, { "t", "\u2020" }, { "u", "\u00B5" }, { "v", "|/" },
            { "w", "\'" },
            { "x", "\u00D7" }, { "y", "\\|/" }, { "z", "7_" }
    }).collect(Collectors.toMap(data -> data[0], data -> data[1]));

    static void test() {
        System.out.println(String.format("TestBasic Lower: ¿Passed Test? %s",
                codigocaballer.translate(TestInputText, leetAlphabetBasic, leetNumbers).equals(TestBasicOutputText)));
        System.out.println(String.format("TestBasic Upper: ¿Passed Test? %s\n",
                codigocaballer.translate(TestInputTextUpper, leetAlphabetBasic, leetNumbers)
                        .equals(TestBasicOutputUpper)));

        System.out.println(String.format("TestAdvanced Lower: ¿Passed Test? %s",
                codigocaballer.translate(TestInputText, leetAlphabetAdvanced, leetNumbers)
                        .equals(TestAdvancedOutputText)));
        System.out.println(String.format("TestIntermediate Lower: ¿Passed Test? %s",
                codigocaballer.translate(TestInputText, leetAlphabetIntermediate, leetNumbers)
                        .equals(TestIntermediateOutputText)));

        System.out.println(String.format("TestFullRetard Lower: ¿Passed Test? %s",
                codigocaballer.translate(TestInputText, leetAlphabetFullRetard, leetNumbers)
                        .equals(TestFullRetardOutputText)));
    }

    static String translate(String inputText, Map<String, String> leetAlphabet, Map<String, String> leetNumbers) {
        String leetChar = "", result = "";
        String inputString = "";
        char inputChar;

        for (int i = 0; i < inputText.length(); i++) {
            inputChar = inputText.charAt(i);
            inputString = String.valueOf(inputChar);

            try {
                if (inputChar >= 48 && inputChar <= 57)
                    leetChar = leetNumbers.get(inputString);
                else if (inputChar >= 65 && inputChar <= 90) {
                    inputString = inputString.toLowerCase().substring(0);
                    leetChar = leetAlphabet.get(inputString);
                } else if (inputChar >= 97 && inputChar <= 122)
                    leetChar = leetAlphabet.get(inputString);
                else
                    leetChar = inputString;

                if (leetChar == null)
                    leetChar = inputString;

            } catch (Exception e) {
                leetChar = inputString;
            }
            result += leetChar;
        }
        return result;
    }

    public static void main(String[] args) {
        String text = "", textLevel = "";
        Boolean validText = false, validLevel = false;

        System.out.println(
                "---------------------------------\n|TEXT TO HACKER LANGUAGE ENCODER|\n---------------------------------\n");

        codigocaballer.test();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        do {
            System.out.print("\nInsert a plain text to transform to Leet Mixed Level: ");
            try {
                text = br.readLine();
            } catch (IOException e) {

            }
            validText = (text.length() > 0);
            if (!validText)
                System.out.println("ERROR: Please insert a valid text\n");
        } while (!validText);

        int level = 0;
        do {
            System.out.println("\nInsert the encoding level to transform to Leet Mixed Level: ");
            System.out.println("1.-Basic Level\t       2.-Advanced Level");
            System.out.println("3.-Intermediate Level\t4.-FullRetard Level\n");
            try {
                textLevel = br.readLine();
            } catch (IOException e) {

            }

            try {
                level = Integer.parseInt(textLevel);
            } catch (final NumberFormatException e) {
                level = -1;
            }

            validLevel = level > 0 && level <= 4;
            if (!validLevel)
                System.out.println("ERROR: Please insert a valid level\n");
        } while (!validLevel);

        Map<String, String> leetAlphabet = null;
        switch (level) {
            case 1:
                leetAlphabet = leetAlphabetBasic;
                break;
            case 2:
                leetAlphabet = leetAlphabetAdvanced;
                break;
            case 3:
                leetAlphabet = leetAlphabetIntermediate;
                break;
            case 4:
                leetAlphabet = leetAlphabetFullRetard;
                break;
        }

        System.out.println("Encoded Text:\n" + codigocaballer.translate(text, leetAlphabet, leetNumbers));
    }
}
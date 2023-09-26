import java.text.NumberFormat;

public class Magdielina {
    public static void main(String[] args) {
        String[] abacus = {"0---00000000",
                "000---000000",
                "---000000000",
                "00---0000000",
                "0000000---00",
                "000000000---",
                "---000000000"};
        System.out.println("Result: " + readAbacus(abacus));
    }

    private static String readAbacus(String[] abacus) {
        if (abacus != null && abacus.length == 7) {
            int number = 0;
            int m = 1000000;
            for (String element : abacus) {
                if((element.length() == 12) && element.contains("---") && element.replace("---", "").equals("000000000")) {
                    number = number + (element.substring(0, element.indexOf("---")).length() * m);
                    m /= 10;
                } else {
                    return "Abacus is incorrect";
                }
            }
            return  NumberFormat.getInstance().format(number);
        } else {
            return "Abacus has incorrect size";
        }
    }
}
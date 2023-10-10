import java.util.HashMap;

public class Qv1ko {

    public static void main(String[] args) {
        System.out.println(excelColumn("AYK"));
    }

    private static int excelColumn(String column) {

        int number = 0;
        String[] letters = column.split("");
        HashMap<String, Integer> value = new HashMap<String, Integer>();
        value.put("A", 1);
        value.put("B", 2);
        value.put("C", 3);
        value.put("D", 4);
        value.put("E", 5);
        value.put("F", 6);
        value.put("G", 7);
        value.put("H", 8);
        value.put("I", 9);
        value.put("J", 10);
        value.put("K", 11);
        value.put("L", 12);
        value.put("M", 13);
        value.put("N", 14);
        value.put("O", 15);
        value.put("P", 16);
        value.put("Q", 17);
        value.put("R", 18);
        value.put("S", 19);
        value.put("T", 20);
        value.put("U", 21);
        value.put("V", 22);
        value.put("W", 23);
        value.put("X", 24);
        value.put("Y", 25);
        value.put("Z", 26);

        for (int i = letters.length - 1; i >= 0; i--) {
            number += (i != letters.length - 1) ? value.get(letters[i]) * Math.pow(26, (letters.length - 1 - i)) : value.get(letters[i]);
        }

        return number;

    }

}

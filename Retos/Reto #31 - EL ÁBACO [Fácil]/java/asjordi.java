import java.text.DecimalFormat;

public class Abacus {

    public static String calculate(String[] numbers){

        if (numbers.length != 7) throw new IllegalArgumentException("The length should be 7");

        StringBuilder completeNum = new StringBuilder();
        DecimalFormat df = new DecimalFormat("###,###,###");

        for (String num : numbers){
            if (num.length() == 12 && num.contains("---") && num.replace("---", "").equals("OOOOOOOOO")){
                String n = num.substring(0, num.lastIndexOf("-") - 2);
                completeNum.append(n.length());
            } else {
                throw new IllegalArgumentException("Incorrect row format in: " + num);
            }
        }

        return df.format(Integer.parseInt(completeNum.toString()));

    }

}

public class Qv1ko {

    public static void main(String[] args) {
        decimalConverter(21);
    }//main

    private static void decimalConverter(int decimal) {
        int number=decimal;
        String octal="";
        String hex="";
        char[] hexValues={'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
        while(number>0) {
            octal=number%8+octal;
            number/=8;
        }
        octal=(octal.equals(""))? "0":octal;
        System.out.println(decimal+" in octal is "+octal);
        number=decimal;
        while(number>0) {
            hex=hexValues[number%16]+hex;
            number/=16;
        }
        hex=(hex.equals(""))? "0":hex;
        System.out.println(decimal+" in hex is 0x"+hex);
    }//decimalConverter

}//class

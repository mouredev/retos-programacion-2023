public class Qv1ko {

    public static void main(String[] args) {
        decimalConverter(21);
    }//main

    private static void decimalConverter(int decimal) {
        int number=decimal;
        String octal="";
        String hex="";
        while(number>0) {
            octal=(int)(number%8)+octal;
            number/=8;
        }
        if(octal.equals("")) {
            octal="0";
        }
        System.out.println(decimal+" in octal is "+octal);
        number=decimal;
        while(number>0) {
            switch((int)(number%16)) {
                case 10 -> hex="A"+hex;
                case 11 -> hex="B"+hex;
                case 12 -> hex="C"+hex;
                case 13 -> hex="D"+hex;
                case 14 -> hex="E"+hex;
                case 15 -> hex="F"+hex;
                default -> hex=(int)(number%16)+hex;
            }
            number/=16;
        }
        if(hex.equals("")) {
            hex="0";
        }
        System.out.println(decimal+" in hex is 0x"+hex);
    }//decimalConverter

}//class

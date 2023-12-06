public class ycanas {
    public int decimal = 0;
    private char hexadecimal [] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    public ycanas(int decimal) {
        this.decimal = decimal;
    }

    public String sdivision(int divisor) {
        int number = this.decimal;
        String convertion = "";

        while (number >= 1) {
            int value = number % divisor;
            convertion = divisor == 16 ? Integer.toString(value) + ',' + convertion : Integer.toString(value) + convertion;
    
            number = number / divisor;
        }

        return convertion;
    }

    public String toHexadecimal(){
        String number [] = sdivision(16).split(",");
        String hexadecimal = "";

        for (String value: number) {
            int position = Integer.parseInt(value);
            hexadecimal = hexadecimal + this.hexadecimal[position];
        }

        return hexadecimal;
    }

    public int toOctal(){
        return Integer.parseInt(sdivision(8));
    }

    public static void main(String[] args){
        ycanas cvn1 = new ycanas(362);
        ycanas cvn2 = new ycanas(110);
        ycanas cvn3 = new ycanas(47);

        System.out.println("Decimal: " + cvn1.decimal + ", Hexadecimal: " + cvn1.toHexadecimal() + ", Octal: " + cvn1.toOctal());
        System.out.println("Decimal: " + cvn2.decimal + ", Hexadecimal: " + cvn2.toHexadecimal() + ", Octal: " + cvn2.toOctal());
        System.out.println("Decimal: " + cvn3.decimal + ", Hexadecimal: " + cvn3.toHexadecimal() + ", Octal: " + cvn3.toOctal());
    }
}

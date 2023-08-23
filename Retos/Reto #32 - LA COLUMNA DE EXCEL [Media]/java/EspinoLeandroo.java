public class EspinoLeandroo {

    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        espinoLeandroo.excelColumn("A");
        espinoLeandroo.excelColumn("Z");
        espinoLeandroo.excelColumn("AA");
        espinoLeandroo.excelColumn("CA");
        espinoLeandroo.excelColumn("ZYX");
        espinoLeandroo.excelColumn("AYK");
        espinoLeandroo.excelColumn("");

    }

    public void excelColumn(String input){
        int column = 0;

        if(!input.isBlank()){
            input = input.toUpperCase();
            for(int i = 0; i < input.length(); i++){
                column += (input.charAt(i) - 64) * (Math.pow(26, (input.length()-1-i)));
            }        
            System.out.println(input + " => " + column);
        }        
    }
}


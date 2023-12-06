public class EspinoLeandroo {

    String[] t9 = {" ", ",.?!", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"};
    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        System.out.println(espinoLeandroo.t9_to_text("0-555-33-2-66-3-777-666-1111"));
        System.out.println(espinoLeandroo.t9_to_text(""));
        System.out.println(espinoLeandroo.t9_to_text("2222"));
        System.out.println(espinoLeandroo.t9_to_text("6-666-88-777-33-0-3-33-888"));
        System.out.println(espinoLeandroo.t9_to_text("6-676-88-777-33-3-33-888"));
        System.out.println(espinoLeandroo.t9_to_text("6-6a6-88-777-33-3-33-888"));
            

    }

    public String t9_to_text(String input){
        String message = "";

        if(input != null && !input.isEmpty()){
            String[] sequences = input.split("-");

            for (String number_sequence : sequences) {
                int number = Integer.parseInt(number_sequence.charAt(0)+"");

                if(number_sequence.length() <= t9[number].length()){
                    message = message.concat(t9[number].charAt(number_sequence.length()-1)+"");
                }else{
                    message = "Error!\tInvalid sequence";
                }
            }
        }else{
            message = "Error!\tInvalid Input";
        }

        
        
        return message;
    }
}

import java.util.ArrayList;
import java.util.List;

public class EspinoLeandroo {

    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        espinoLeandroo.infiltratedCharacters("Me llamo mouredev", "Me llemo mouredov");
        espinoLeandroo.infiltratedCharacters("Me llamo.Brais Moure", "Me llamo brais moure");
        espinoLeandroo.infiltratedCharacters("Me llamo.Brais Moure", "Me llamo brais moure ");

    }

    public void infiltratedCharacters(String input1, String input2){
        List<String> infiltratedCharacters = new ArrayList<>();

        if(input1.length() == input2.length()){

            for(int i = 0; i < input1.length(); i++){
                if(input1.charAt(i) != input2.charAt(i)){
                    infiltratedCharacters.add(input2.charAt(i) + "");
                }
            }        
            System.out.println(infiltratedCharacters);
        }        
    }
}


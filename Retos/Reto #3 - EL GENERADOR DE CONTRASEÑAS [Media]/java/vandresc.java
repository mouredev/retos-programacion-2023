import java.util.*;

/**
 * Programa que genere una contraseña en la que se pueda:
 * - Elegir si tiene 8 o 16 carácteres
 * - Elegir si se quiere que tenga mayúsculas
 * - Elegir si se quiere que tenga números
 * - Elegir si se quiere que tenga simbolos
 */
public class vandresc {

    private static final String LOWERCASE = "abcdefghijklmnopqrstuvwxyz";
    private static final String UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final String NUMBERS = "0123456789";
    private static final String SYMBOLS = "!@#$%^&*()_+-=[]|,./?><";


    public static class Params{
        public Boolean hasLength16;
        public Boolean hasUpperCase;
        public Boolean hasNumbers;
        public Boolean hasSymbols;
    }

    public static void main(String[] args) {
        Params params = new Params();
        params.hasLength16 = true;
        params.hasUpperCase = true;
        params.hasNumbers = true;
        params.hasSymbols = true;
        showPassword(generatePassword(params));
    }

    private static String generatePassword(Params params) {
        String sourceChars = getSourceChars(params);
        int length = (params.hasLength16)? 16 : 8;
        String password = "";
        for(int i=0; i<length; i++){
            password += randomChar(sourceChars);
        }
        return password;
    }
    private static String getSourceChars(Params params){


        StringBuilder sourceChars = new StringBuilder(LOWERCASE);
        if(params.hasUpperCase){
            sourceChars.append(UPPERCASE);
        }
        if(params.hasNumbers){
            sourceChars.append(NUMBERS);
        }
        if(params.hasSymbols){
            sourceChars.append(SYMBOLS);
        }
        List<String> source = Arrays.asList(sourceChars.toString());
        Collections.shuffle(source);
        return source.get(0);
    }

    private static String randomChar(String sourceChars){
        Random rd = new Random();
        int randomInt = rd.nextInt(sourceChars.length());
        return String.valueOf(sourceChars.charAt(randomInt));
    }

    private static void showPassword(String password){
        System.out.println(password);
    }
}


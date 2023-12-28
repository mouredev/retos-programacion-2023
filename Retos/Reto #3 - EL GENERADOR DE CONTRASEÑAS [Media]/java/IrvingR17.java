import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class IrvingR17 {
    
    public static void main(String[] args) throws Exception {
    
        final PassGenerator passGenerator = new PassGenerator("A1AAAaA-");
        passGenerator.generatePassword();
    }

    static class PassGenerator {

            private String input = "";
            private PassValidator validator = new PassValidator();

            public PassGenerator(String input) {
                this.input = input;
            }

            public void generatePassword() {
                if(validator.validateLength(this.input) && validator.validateUpperCase(this.input) && validator.validateLowerCase(this.input)
                   && validator.validateNumber(this.input) && validator.validateSpecial(this.input)) {
                    System.out.println("Contrasena valida");
                } else {
                    System.out.println("Contrasena no valida");
                }
            }
        }

    static class PassValidator {

        public Boolean validateLength(String input) {
            if(!input.isEmpty() && (input.length() >= 8 && input.length() <= 16)) {
                return true;
            } else {
                return false;
             }
       }

        public Boolean validateUpperCase(String input) {
            Pattern p = Pattern.compile("[A-Z]");
            Matcher m = p.matcher(input);
            Boolean b = m.find();
            
            return b;
        }

        public Boolean validateLowerCase(String input) {
            Pattern p = Pattern.compile("[a-z]");
            Matcher m = p.matcher(input);
            Boolean b = m.find();
                
            return b;
        }

        public Boolean validateNumber(String input) {
            Pattern p = Pattern.compile("[0-9]");
            Matcher m = p.matcher(input);
            Boolean b = m.find();
                
            return b;
        }

        public Boolean validateSpecial(String input) {
            Pattern p = Pattern.compile("[^A-Za-z0-9]");
            Matcher m = p.matcher(input);
            Boolean b = m.find();
            
            return b;
        }
    }
}


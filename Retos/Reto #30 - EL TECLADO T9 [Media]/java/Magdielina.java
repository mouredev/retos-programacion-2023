import java.util.regex.*;
class Magdielina {
    public static void main(String[] args) {
        System.out.println(getMessage("6-2-4-3-444-33-555-0-55-33-999-22-666-2-777-3"));
    }

    public static String getMessage(String numbers){
        char c = ' ';
        String[] blocks = numbers.split("-");
        StringBuilder message = new StringBuilder();

        for (String block : blocks) {
            char character = block.charAt(0);
            Pattern pattern = Pattern.compile("[^"+ character +"]");
            Matcher matcher = pattern.matcher(block);
            if(matcher.find()) {
                return "Invalid block found";
            }

            int add = block.length() - 1;
            if(add < 3 || (add == 3 && character == '9')){
                switch (character) {
                    case '2': c = 'A'; break;
                    case '3': c = 'D'; break;
                    case '4': c = 'G'; break;
                    case '5': c = 'J'; break;
                    case '6': c = 'M'; break;
                    case '7': c = 'P'; break;
                    case '8': c = 'T'; break;
                    case '9': c = 'W'; break;
                    case '0': c = ' '; break;
                    default: return "Invalid character found!";
                }
                message.append((char)(c + add));
            } else {
                return "Invalid block found";
            }
        }
        return message.toString();
    }
}
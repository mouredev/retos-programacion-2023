import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.atomic.AtomicReference;
import java.util.stream.Collectors;
import javax.swing.JOptionPane;


class NamelessReact {

    public Optional<List<String>> passwordGenerator() {
        AtomicReference<String> characters = new AtomicReference<>("abcdefghijklmnopqrstuvwxyz");
        byte length = 0;
        
        do {
            length = Byte.parseByte(JOptionPane.showInputDialog("Digite la longitud que desea que tenga la constraseña entre 8 y 16 caracteres: "));
        } while (length < 8 || length > 16);
        
        
        List<String> password = Arrays.asList("*".repeat(length).split(""));
        
        String upperCaseletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String numbers = "0123456789";
        String symbols = "!$%&()=/?¿¡:,;_-|@#+*{}[]^\\ñ";
        
        
        
        char containsLetters = JOptionPane.showInputDialog("¿Desea que su contraseña contenga letras mayúsculas?"
                + "\n s) si"
                + "\n n) no").toLowerCase().charAt(0);
        
        characters.set(containsLetters == 's' ? characters.get() + upperCaseletters : "");
        
        char containsNumbers = JOptionPane.showInputDialog("¿Desea que su contraseña contenga números?"
                + "\n s) si"
                + "\n n) no").toLowerCase().charAt(0);
        
        characters.set(containsNumbers == 's' ? characters.get() + numbers : "");
        
        char containsSymbols = JOptionPane.showInputDialog("¿Desea que su contraseña contenga símbolos?"
                + "\n s) si"
                + "\n n) no").toLowerCase().charAt(0);
        
        characters.set(containsSymbols == 's' ? characters.get() + symbols : "");
        
        
        if (characters.get().toString().length() == 0) {
            JOptionPane.showMessageDialog(null, "No se puede generar una contraseña sin caracteres");
            return Optional.empty();
        }
        
      
        
        List<String> newPassword = password.stream().map(letter -> String.valueOf(characters.get().toString().charAt((int) Math.floor(Math.random() * characters.toString().length()))))
                .collect(Collectors.toList());
        
        return Optional.of(newPassword);
    }
}

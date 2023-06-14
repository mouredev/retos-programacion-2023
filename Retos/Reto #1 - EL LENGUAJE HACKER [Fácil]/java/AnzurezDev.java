import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class AnzurezDev {
    private static final  Map<String, String> alphabet = constMap();

    private static Map<String, String> constMap() {
        Map<String, String> map = new HashMap<>();

        map.put( "A", "4" );
        map.put( "B", "I3" );
        map.put( "C", "[" );
        map.put( "D", ")" );
        map.put( "E", "3" );
        map.put( "F", "|=" );
        map.put( "G", "&" );
        map.put( "H", "#" );
        map.put( "I", "1" );
        map.put( "J", ",_|" );
        map.put( "K", ">|" );
        map.put( "L", "1" );
        map.put( "M", "/\\/\\" );
        map.put( "N", "^/" );
        map.put( "O", "0" );
        map.put( "P", "|*" );
        map.put( "Q", "(_,)" );
        map.put( "R", "I2" );
        map.put( "S", "5" );
        map.put( "T", "7" );
        map.put( "U", "(_)" );
        map.put( "V", "\\/" );
        map.put( "W", "\\/\\/" );
        map.put( "X", "><" );
        map.put( "Y", "j" );
        map.put( "Z", "2" );
        map.put( "1", "L" );
        map.put( "2", "R" );
        map.put( "3", "E" );
        map.put( "4", "A" );
        map.put( "5", "S" );
        map.put( "6", "b" );
        map.put( "7", "T" );
        map.put( "8", "B" );
        map.put( "9", "g" );
        map.put( "0", "o" );

        return Collections.unmodifiableMap( map );
    }

    public static void leetLang( Object objText ) {
        String text      = objText.toString();
        String output    = "";
        String letters[] = text.toUpperCase().split( "" );

        for ( String letter : letters )
            output += alphabet.get( letter ) == null ? letter : alphabet.get( letter );

        System.out.println( output );
    }

    public static void main(String[] args) {
        leetLang( "This is the hacker language" );
    }
}
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */
public class joelsempere {
    public static final Integer BASE_16 = 16;
    Pattern hexPattern;
    Map<String,Integer> hexValues;
    public joelsempere() {
        this.hexPattern = Pattern.compile('^#?[0-9A-Fa-f]+$');
        this.hexValues = new Map<String,Integer>{
            '1' => 1, '2' => 2, '3' => 3, '4' => 4, '5' => 5,
            '6' => 6, '7' => 7, '8' => 8, '9' => 9, 'A' => 10,
            'B' => 11, 'C' => 12, 'D' => 13, 'E' => 14, 'F' => 15
        };
    }

    /**
    * @description Convert hexadecimal into rgb,
    * valid only 3 or 6 length and Base64 numbers.
    * The string can include the '#' character.
    * @param hexString hexadecimal string.
    * @return String -> rgb color.
    **/
    public String hexToRgb(String hexString) {
        String input = 'Introduce un valor valido en hexadecimal.';
        hexString = this.removeChar(hexString, '#');
        Boolean correctLength = hexString.length() == 6 || hexString.length() == 3;
        if(this.isHex(hexString) && correctLength) {
            input = this.convertHexToRgb(hexString.toUpperCase());
        }
        return input;
    }

    /**
    * @description Convert rgb into hexadecimal.
    * @param r red color.
    * @param g green color.
    * @param b blue color.
    * @return String -> hex color. 
    **/
    public String rgbToHex(Integer r, Integer g, Integer b) {
        List<String>hexParts = new List<String>{
            this.convertRgbToHex(rgbRangeControl(r)), this.convertRgbToHex(this.rgbRangeControl(g)), this.convertRgbToHex(this.rgbRangeControl(b))
        };
        return '#' + hexParts[0] + hexParts[1] + hexParts[2];
    }

    private boolean isHex(String hexString) {
        return this.hexPattern.matcher(hexString).matches();
    }

    private String removeChar(String hexString, String character) {
       return hexString.substring(0, 1) == character ? hexString.replaceAll(character, '') : hexString;
    }

    private String convertRgbToHex(Integer rgb) {
        String hexCharacters = '0123456789ABCDEF';
        String out = '';
        Integer remainder = 0;
        
        while (rgb > 0) {
            remainder = Math.mod(rgb, BASE_16);
            out = hexCharacters.substring(remainder, remainder + 1) + out;
            rgb = rgb / BASE_16;
        }
        return out.length() == 1 ? '0' + out : out;
    }

    private String convertHexToRgb(String hexString) {
        List<Integer> rgb = new List<Integer>();
        Boolean threeLength = hexString.length() == 3;
        List<String> hexChars = hexString.split('');
        List<String> splitValues = this.splitInPairs(hexChars, threeLength);  
        Integer c1, c2;
        List<String> separatePair = new List<String>();
        for(String pair : splitValues) {
            separatePair = pair.split('');
            rgb.add((this.hexValues.get(separatePair.get(0)) * BASE_16) + this.hexValues.get(separatePair.get(1)));
        }
        
        return new RGB(rgb).show();
    }

    private List<String> splitInPairs(List<String> hexChars, Boolean threeLength) {
        String value = '';
        List<String> values = new List<String>();
        for (String hexChar : hexChars) {
            if(!threeLength) {
                value += hexChar;
                if(value.length() == 2) {
                    values.add(value);
                    value = '';       
                }
            }
            else {
                values.add(hexChar.repeat(2));
            }  
        }
        return values;
    }

    public Integer rgbRangeControl(Integer num) {
        return Math.max(0, Math.min(255, num));    
    }

    public class RGB {
        Integer r;
        Integer g;
        Integer b;
        public RGB(List<Integer> nums) {
            if (nums.size() == 3) {
                this.r = nums.get(0);
                this.g = nums.get(1);
                this.b = nums.get(2);
            }
        }

        public String show() {
            return '(r: ' + r + ', g: ' + g + ', b: ' + b + ')';
        }
    }

    /** Execute Anonymous Window
    *  joelsempere js = new joelsempere();
    *  String hex = js.rgbToHex(50,230,223);
    *  System.debug(hex);
    *  System.debug(js.hexToRgb(hex));
    */
}
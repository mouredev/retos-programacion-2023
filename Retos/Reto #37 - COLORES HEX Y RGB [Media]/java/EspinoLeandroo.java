public class EspinoLeandroo {

    public static String rgbToHex(int r, int g, int b) {
        return String.format("#%02X%02X%02X", r, g, b);
    }    

    public static String hexToRgb(String hex) {
        hex = hex.replace("#", "");
        int bigint = Integer.parseInt(hex, 16);
        int r = (bigint >> 16) & 255;
        int g = (bigint >> 8) & 255;
        int b = bigint & 255;
        return String.format("r: %d, g: %d, b: %d", r, g, b);
    }
    
    public static void main(String[] args) {
        // rgbToHex:
        int r = 250, g = 186, b = 218;
        String hexColor = rgbToHex(r, g, b);
        System.out.println(hexColor);
        // hexToRgb:
        hexColor = "#fabada";
        String rgbColor = hexToRgb(hexColor);
        System.out.println(rgbColor);
    }
}

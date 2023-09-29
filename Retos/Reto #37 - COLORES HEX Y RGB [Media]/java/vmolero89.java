
            /*
             * Crea las funciones capaces de transformar colores HEX
             * a RGB y viceversa.
             * Ejemplos:
             * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
             * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
             */

            public class vmolero89 {

                public static String rgbToHex(int r, int g, int b) {
                    if (r<0||g<0||b<0||r>255||g>255||b>255) try {
                        throw new Exception("[ERROR] Numbers R, G, and B must be from the interval [0-255]");
                    } catch (Exception e) {
                        throw new RuntimeException(e);
                    }

                    String rString = Integer.toHexString(r).toUpperCase();
                    String gString = Integer.toHexString(g).toUpperCase();
                    String bString = Integer.toHexString(b).toUpperCase();

                    while (rString.length() < 2) rString = "0" + rString;
                    while (gString.length() < 2) gString = "0" + gString;
                    while (bString.length() < 2) bString = "0" + bString;

                    return "0x" + rString + gString + bString;
                }

                public static String hexToRGB(String hex) {

                    int r = Integer.parseUnsignedInt(hex.substring(2, 4),16);
                    int g = Integer.parseUnsignedInt(hex.substring(4, 6),16);
                    int b = Integer.parseUnsignedInt(hex.substring(6, 8),16);

                    return "r: " + r + ", g: " + g + ", b: " + b;
                }

                public static void main(String[] args) {
                    System.out.println(rgbToHex(255, 255, 255));
                    System.out.println(hexToRGB("0xFFFFFF"));
                }
            }
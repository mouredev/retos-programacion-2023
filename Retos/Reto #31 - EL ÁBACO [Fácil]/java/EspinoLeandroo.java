public class EspinoLeandroo {

    String[] abaco = {
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO"};

    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        int multiplo = 100000;
        int cuenta = 0;
        for (String linea : espinoLeandroo.abaco) {
            linea = linea.substring(0, linea.indexOf("-"));
            cuenta += linea.length() * multiplo;
            multiplo /= 10;
        }

        System.out.println(cuenta);

    }

}
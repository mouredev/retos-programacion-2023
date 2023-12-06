public class Qv1ko {

    public static void main(String[] args) {
        abacus(new String[]{"O---OOOOOOOO", "OOO---OOOOOO", "---OOOOOOOOO", "OO---OOOOOOO", "OOOOOOO---OO", "OOOOOOOOO---", "---OOOOOOOOO"});
    }

    private static void abacus(String[] numbers) {

        String finalNumber = "";

        int number = 0;

        for(String n : numbers) {

            number = n.split("---")[0].length();
        
            finalNumber += (number > 0) ? number : (finalNumber.length() != 0) ? 0 : "";

        }

        System.out.println(finalNumber);

    }

}

public class ycanas {

    public static String analyzeText(String text) {
        int numberSentences = text.split("\\.").length;

        String search = "[.,:;¿?¡!()]";
        text = text.replaceAll(search, "").toLowerCase();

        String[] words = text.split(" ");
        int numberWords = words.length;

        double mean = 0.0;
        String longestWord = words[0];

        for (String word: words) {
            if (longestWord.length() < word.length())
                longestWord = word;

            mean = word.length() + mean;
        }

        mean = mean / numberWords;

        String output = (
                "\nNúmero total de palabras: " + numberWords +
                "\nLongitud media de palabras: " + mean +
                "\nNúmero de oraciones en el texto: " + numberSentences +
                "\nPalabra mas larga: " + longestWord
        );

        return output;
    }

    public static void main(String[] args) {
        String text = (
                "El término digital se deriva de la forma en que las " +
                "computadoras realizan las operaciones contando " +
                "dígitos. Durante muchos años, las aplicaciones de la " +
                "electrónica digital se limitaron a los sistemas informáticos. " +
                "Hoy día, la tecnología digital tiene aplicación en un amplio " +
                "rango de áreas además de la informática. Aplicaciones como la " +
                "televisión, los sistemas de comunicaciones, de radar, sistemas " +
                "de navegación y guiado, sistemas militares, instrumentación médica, " +
                "control de procesos industriales y electrónica de consumo, usan " +
                "todos ellos técnicas digitales."
        );

        System.out.println(analyzeText(text));
    }
}

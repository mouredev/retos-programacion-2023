import java.util.ArrayList;
import java.util.List;

public class EspinoLeandroo {

    public static List<int[]> encontrarTriplesPitagoricos(int maximo) {
        List<int[]> triples = new ArrayList<>();
        
        for (int a = 1; a <= maximo; a++) {
            for (int b = a; b <= maximo; b++) {
                double c = Math.sqrt(a * a + b * b);
                if (c == (int) c && c <= maximo) {
                    int[] triple = {a, b, (int) c};
                    triples.add(triple);
                }
            }
        }
        
        return triples;
    }

    public static void main(String[] args) {
        int maximo = 100;
        List<int[]> resultado = encontrarTriplesPitagoricos(maximo);
        
        for (int[] triple : resultado) {
            System.out.println("(" + triple[0] + ", " + triple[1] + ", " + triple[2] + ")");
        }
    }
}

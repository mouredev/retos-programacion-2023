import java.util.*;

public class PythagoreanTriples {

    public static List<int[]> find(int limit){
        List<int[]> triples = new LinkedList<>();

        for (int a = 1; a < limit + 1; a++) {
            for (int b = a; b < limit + 1; b++) {
                int squaredCat = (a * a) + (b * b);
                double c = Math.sqrt(squaredCat);
                if (c > limit) break;
                if (c == (int) c) triples.add(new int[]{a, b, (int) c});
            }
        }

        return triples;
    }

}

public class TriplesPitagoricos {
    public static void main(String[] args) {
        List<List<Integer>> resultado = triplesPitagoricos(10);
        resultado.forEach(System.out::println);
    }

    private static List<List<Integer>> triplesPitagoricos(int n) {
        List<List<Integer>> triples = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            for (int j = i; j < n; j++) {
                int z = (int) Math.sqrt(i * i + j * j);
                    if (z <= n && i * i + j * j == z * z) {
                        List<Integer> triple = new ArrayList<>();
                        triple.add(i);
                        triple.add(j);
                        triple.add(z);
                        triples.add(triple);
                    }
            }
        }
        return triples;
    }
}

public class NamelessReact() {
    public static void main(args[]) {
        resultadoJuego(new String[][]{{"🗿","✂️"}, {"✂️","🗿"}, {"✂","📄️"}, {"✂","📄️"}});
    }

    public void resultadoJuego(String[][] marcador) {
        int points1 = 0;
        int points2 = 0;

        Map<String, ArrayList<String>> rules = new HashMap<>(){{
            put("🗿", new ArrayList<>(Arrays.asList("✂️", "🦎")));
            put("📄", new ArrayList<>(Arrays.asList("🗿", "🖖")));
            put("✂️", new ArrayList<>(Arrays.asList("📄", "🦎")));
            put("🦎", new ArrayList<>(Arrays.asList("🖖", "📄")));
            put("🖖", new ArrayList<>(Arrays.asList("🗿", "✂️")));
        }};

        for (int i = 0; i < marcador.length; i++) {
            String player1 = marcador[i][0];
            String player2 = marcador[i][1];

            if (player1.equals(player2)) continue;

            boolean win =  rules.getOrDefault(player2, new ArrayList<>(Arrays.asList("none"))).stream().anyMatch(element -> element.equals(player1));
            if (win) points2 += 1;
            else points1 += 1;
        }
        System.out.println(points1 == points2 ? "Tie" : points1 > points2 ? "Ganador jugador 1" : "Ganador jugador 2");
    }
}
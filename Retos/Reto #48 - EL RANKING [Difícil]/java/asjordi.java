import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Ranking {

    public static void main(String[] args) {
        Ranking ranking = new Ranking();
        System.out.println("Total users: " + ranking.getNumOfUsers());
        System.out.println("Total commits: " + ranking.getTotalCommits());
        System.out.println("--------------------");
        ranking.printRanking();
    }

    private final Gson gson;
    private int totalCommits;
    private final Map<String, Integer> map;

    public Ranking() {
        this.gson = new Gson();
        this.totalCommits = 0;
        this.map = new HashMap<>();
        getAndLoadData();
    }

    public int getTotalCommits() {
        return totalCommits;
    }

    public int getNumOfUsers() {
        return map.size();
    }

    public void printRanking() {
        String[] names = map.keySet().toArray(new String[0]);
        Arrays.sort(names, (a, b) -> map.get(b) - map.get(a));

        for (String name : names) {
            System.out.printf("%s: %d\n", name, map.get(name));
        }
    }

    private void getAndLoadData() {
        final String URL = "https://api.github.com/repos/mouredev/retos-programacion-2023/stats/contributors";

        try {
            HttpResponse<String> getResponse = HttpClient.newHttpClient().send(HttpRequest.newBuilder().uri(new URI(URL)).GET().build(), HttpResponse.BodyHandlers.ofString());

            if (getResponse.statusCode() != 200) throw new RuntimeException("HttpResponseCode: " + getResponse.statusCode());

            JsonArray contributors = gson.fromJson(getResponse.body(), JsonArray.class);

            for (JsonElement contributorElement : contributors) {
                JsonObject contributor = contributorElement.getAsJsonObject();
                String name = contributor.get("author").getAsJsonObject().get("login").getAsString();
                int numOfCommits = contributor.get("total").getAsInt();

                this.totalCommits += numOfCommits;
                map.put(name, numOfCommits);
            }
        } catch (URISyntaxException | IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
    }


}
